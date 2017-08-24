# Фоновая картинка
# Демонстрирует назначение фоновой картинки для графического экрана

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image = games.load_image("wall.jpg", transparent = False)
# transparent - объяянит позже, но фон ВСЕГДА =False
games.screen.background = wall_image
games.screen.mainloop() # здесь mainloop заставляет экран обновл 50раз/сек
