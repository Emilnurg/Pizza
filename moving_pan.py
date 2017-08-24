# Подвижная сковорода
# Демонстрирует ввод с помощью мыши

from livewires import games, color


games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """Перемещаемая мышью сковорода"""
    def update(self):
        """Перемещает объект в позицию указателя"""
        self.x = games.mouse.x
        self.y = games.mouse.y

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    # transparent - прозрачность, по умолчанию True, но фон ВСЕГДА =False
    games.screen.background = wall_image
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
        
