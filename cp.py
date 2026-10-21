from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

app = Ursina()

# Полностью отключаем весь лишний мыльный мусор из 90-х
window.fps_counter.enabled = False
window.exit_button.enabled = False
mouse.visible = False

# Находим папку с твоими родными текстурами
current_dir = os.path.dirname(os.path.abspath(__file__))
textures_path = os.path.join(current_dir, "textures").replace("\\", "/")

my_grass_image = None

# Автопоиск ТВОЕЙ картинки травы в твоей папке textures
if os.path.exists(textures_path):
    all_files = os.listdir(textures_path)
    for file in all_files:
        if file.lower().endswith(".png") and ("grass" in file.lower() or "top" in file.lower()):
            my_grass_image = os.path.join(textures_path, file).replace("\\", "/")
            break
    # Если по слову grass не нашлось, берем первую попавшуюся картинку из твоей папки
    if not my_grass_image and all_files:
        for file in all_files:
            if file.lower().endswith(".png"):
                my_grass_image = os.path.join(textures_path, file).replace("\\", "/")
                break

# 1. СТРОИМ НАСТОЯЩИЙ ТВЁРДЫЙ ПОЛ 33х33 (Силами Python, чтобы он НЕ пропадал)
my_floor = Entity(
    model='cube',
    scale=(33, 1, 33),
    collider='box',
    y=-0.5
)

# 2. НАКЛАДЫВАЕМ ТВОИ РОДНЫЕ ПИКСЕЛИ И УБИРАЕМ РОЗОВЫЙ ЦВЕТ НАВСЕГДА
if my_grass_image and os.path.exists(my_grass_image):
    my_floor.texture = my_grass_image
    my_floor.texture.tiling = (33, 33)     # Размножаем пиксели в красивую сетку блоков
    my_floor.texture.filtering = 'nearest' # Убиваем мыло, делаем графику чёткой и пиксельной!
    print(f"Твоя текстура успешно наложена: {os.path.basename(my_grass_image)}")
else:
    # Если папка textures пустая, красим в обычный майнкрафтовский зеленый без розовых багов
    my_floor.color = color.lime
    print("Твоя папка textures не найдена рядом с файлом игры!")

# 3. УПРАВЛЕНИЕ ОТ ПЕРВОГО ЛИЦА (Строго ногами из глаз, прыжки на Пробел)
player = FirstPersonController(
    jump_height=1.5,
    speed=8,
    y=2  # Мягко встаем ногами на твой пол
)

# 4. ИДЕАЛЬНЫЙ БЕЛЫЙ КРЕСТИК ИЗ ДВУХ ТОНКИХ ЛИНИЙ
crosshair_h = Entity(parent=camera.ui, model='quad', scale=(0.02, 0.002), color=color.white)
crosshair_v = Entity(parent=camera.ui, model='quad', scale=(0.002, 0.02), color=color.white)

def input(key):
    if key == 'escape':
        quit()

app.run()
