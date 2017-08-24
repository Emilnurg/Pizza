# Спрайт-пицца
# Демонстрирует создание спрайта

# Фоновая картинка
# Демонстрирует назначение фоновой картинки для графического экрана

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image = games.load_image("wall.jpg", transparent = False)
# transparent - прозрачность, по умолчанию True, но фон ВСЕГДА =False
games.screen.background = wall_image
pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
games.screen.add(pizza)



games.screen.mainloop() # здесь mainloop заставляет экран обновл 50раз/сек
