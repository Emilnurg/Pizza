# Паника в пиццерии
#Игрок должен ловить падающую пиццу. пока она не достигла земли

from livewires import games, color
import random

games.init(screen_width = 1720, screen_height = 780, fps = 50)

class Pan(games.Sprite):
    """Перемещаемая мышью сковорода"""
    image = games.load_image("pan.bmp") #вынесли из main чтобы не перегрудать

    def __init__(self):
        """ Initialize Pan object and create Text object for score. """
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        
        self.score = games.Text(value = 0, size = 125, color = color.white,
                                top = 4, right = games.screen.width - 100)
        games.screen.add(self.score)
        
    def update(self):
        """Передвигает объект по горизонтали в точку с абсциссой. как у указателя мыши"""
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width: # проверяет не вышла ли кастрюля за правый край
            self.right = games.screen.width

        self.check_catch() # поймал ли игрок один из кругов

    def check_catch(self):
        """Проверяет. поймал ли игрок падающую пиццу"""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 30 # чтобы счет не вылезал за экран
            pizza.handle_caught()  # вызов метода пиццы при перекрытии


    
        

class Pizza(games.Sprite):
    """Круги пиццы. падающие на землю"""
    image = games.load_image("pizza.bmp")
    speed = 3 # скорость падения

    def __init__(self,x, y = 90): # y = 90 - спавн пиццы на уровне рук кулинара
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x,
                                    y = y,
                                    dy = Pizza.speed)

    def update(self): #условие конца игры
        """Проверяет. не коснулась ли нижняя кромка спрайта нижней границы экрана"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """Разрушает объект. пойманный игроком"""
        self.destroy()

    def end_game(self):
        """Конец игры"""
        end_message = games.Message(value = "потрачено",
                                    size = 250,
                                    color = color.white,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """Повар скидывающий пиццу"""
    image = games.load_image("chef.bmp")

    def __init__(self, y = 55, speed = 3, odds_change = 100): # y = 55
        super(Chef, self).__init__(image = Chef.image,
                                    x = games.screen.width/2,
                                    y = y,
                                    dx = speed) # скорость движения покара по горизонтали(равна 2)
        self.odds_change = odds_change # смена направления движения
        self.time_till_drop = 0 # при спауне тут же сбрасывает пиццу
        
        
    def update(self):
        """Определяет. надо пи сменить направление"""
        if self.left < 0:
            self.dx = -self.dx
        elif self.right > games.screen.width: # проверяет не вышла ли кастрюля за правый край
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx 
        self.check_drop()

    def check_drop(self):
        """Уменьшает интервал ожидания на единицу или сбрасывает очередную пиццу
и восстанавливает исходный интервал"""
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            #вне зависимости от скорости падения пиццы "зазор" между падающими кругами
#принимается равным 30 % каждой из них по высоте
            self.time_till_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1
        
def main():
    wall_image = games.load_image("city.jpg", transparent = False)
    # transparent - прозрачность, по умолчанию True, но фон ВСЕГДА =False
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)         
    games.mouse.is_visible = False # скрыть указатель мышки из виду
              
    games.screen.event_grab = True # не дает курсору выйти за пределы области

    #the_score = Pan.check_catch(self)
    #if the_score > 200:
     #   Pizza.speed = 2

    games.screen.mainloop()

#поехали!
if __name__=="__main__":
    main()

            
        
    
