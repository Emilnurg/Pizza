# Ускользающая пицца
# Демонстрирует проверку на соприкосновение спрайтов

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """Перемещаемая мышью сковорода"""
    def update(self):
        """Перемещает объект в позицию указателя"""
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """Проверяет. не соприкоснулись ли сковорода и пицца."""
        for pizza in self.overlapping_sprites: # столкнулась ли пицца со спрайтами класса Pan
            pizza.handle_collide()  #обработка столконовения

class Pizza(games.Sprite):
    """Ускользающая пицца"""
    def handle_collide(self):
        """Перемещает спрайт в случайную позицию на графическом экране"""
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    # transparent - прозрачность, по умолчанию True, но фон ВСЕГДА =False
    games.screen.background = wall_image
    pizza_image = games.load_image("pizza.bmp")
    pizza_x = random.randrange(games.screen.width) # просто рандомное размещение
    pizza_y = random.randrange(games.screen.height)
    pizza = Pizza(image = pizza_image,
                  x = pizza_x,
                  y = pizza_y)
    games.screen.add(pizza)
    pan_image = games.load_image("pan.bmp")
    pan = Pan(image = pan_image,
                         x = games.mouse.x, # где появится(не поведение)
                         y = games.mouse.y,)

    games.screen.add(pan)
              
    games.mouse.is_visible = False # скрыть указатель мышки из виду
              
    games.screen.event_grab = True # не дает курсору выйти за пределы области

    games.screen.mainloop()

#поехали!
if __name__=="__main__":
    main()
        
