# Ничего себе результат!
# Демонстрирует отображение текста на графическом экране



from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image = games.load_image("wall.jpg", transparent = False)
# transparent - прозрачность, по умолчанию True, но фон ВСЕГДА =False
games.screen.background = wall_image
pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image,
                     x = games.screen.width/2, #высота окна пополам
                     y = games.screen.height/2,
                     dx = 1,#скорость(положительное - вправо)
                     dy = 1)#скорость(положительное - вниз)
games.screen.add(pizza)
score = games.Text(value = 1756521, # Text передать минимум 5 аргументов
                   size = 60,  # шрифт (высота в пикселях)
                   color = color.black, # константа из модуля color
                   x = 550, # Text - подкласс Sprite
                   y = 30)


won_message = games.Message(value = "Ураааа!",
                            size = 100, # Message - подкласс Text
                            color = color.red,
                            x = games.screen.width/2, #высота окна пополам
                            y = games.screen.height/2,
                            lifetime = 250, #секунд, по умолчанию 0(не разрушается)
                            after_death = games.screen.quit)
games.screen.add(score)
games.screen.add(won_message)
games.screen.mainloop() # здесь mainloop заставляет экран обновл 50раз/сек

