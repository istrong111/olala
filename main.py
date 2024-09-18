import flet as ft

def main(page: ft.Page):

    # Заголовок страницы
    page.title = "Telegram Clicker Web App"

    # Счетчик
    count = 0

    # Изображение Telegram
    image = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    # Текст для отображения счетчика
    count_text = ft.Text(f"Счетчик: {count}", size=30, weight=ft.FontWeight.BOLD)

    # Функция для увеличения счетчика
    def increase_counter(e):
        nonlocal count
        count += 1
        count_text.value = f"Счетчик: {count}"
        page.update()

    # Кнопка для кликов
    button = ft.ElevatedButton(
        "Кликнуть", 
        on_click=increase_counter, 
        style=ft.ButtonStyle(
            color=ft.colors.WHITE, 
            bgcolor=ft.colors.BLUE_ACCENT,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        width=200,
    )

    # Добавляем содержимое на страницу
    page.add(
        ft.Column(
            [
                image,
                count_text,
                button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# Запуск web-приложения
ft.app(target=main, view=ft.WEB_BROWSER)
