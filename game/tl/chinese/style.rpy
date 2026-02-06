# Используем python блок для жесткой замены шрифтов в переменных движка
translate chinese python:
    # Указываем новый путь gui/font/myfont.ttf
    # Это обновит шрифт диалогов
    gui.text_font = "gui/font/myfont.ttf"

    # Это обновит шрифт имен персонажей
    gui.name_text_font = "gui/font/myfont.ttf"

    # Это обновит шрифт кнопок и меню
    gui.interface_text_font = "gui/font/myfont.ttf"

    # На всякий случай для кнопок выбора
    gui.button_text_font = "gui/font/myfont.ttf"
    gui.choice_button_text_font = "gui/font/myfont.ttf"

# Дублируем стилем на случай, если где-то используется прямой стиль, а не gui переменная
translate chinese style default:
    font "gui/font/myfont.ttf"

translate chinese style say_dialogue:
    font "gui/font/myfont.ttf"
