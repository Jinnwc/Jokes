import flet as ft
import random

def main(page: ft.Page):
    page.title = "Stand Up Comedian"

    jokes = [
        "Why did the chicken started running? because the guy was eating chicken.",
        "Anti-gravity book? Can’t put it down.",
        "Why don’t eggs joke? They’d crack up.",
        "I play piano by hand now.",
        "Cheese that isn’t yours? Nacho cheese.",
        "Lifesavers guy? Made a mint.",
        "Atoms? They make up everything!",
        "Construction joke? Still building it.",
        "Drug dealer shoes? I was tripping!",
        "Fish with a bowtie? Sofishticated."
    ]

    joke_text = ft.Text("", text_align="center", size=18)

    bottom_sheet = ft.BottomSheet(
        ft.Container(
            content=ft.Column(
                [joke_text, ft.TextButton("Close", on_click=lambda e: close_bs())],
                alignment="center",
                horizontal_alignment="center"
            ),
            padding=20
        )
    )

    page.overlay.append(bottom_sheet)

    def show_joke(e):
        joke_text.value = random.choice(jokes)
        bottom_sheet.open = True
        page.update()

    def close_bs():
        bottom_sheet.open = False
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Stand Up Comedian", size=22, weight="bold"),
                ft.ElevatedButton("Tell me a joke please", on_click=show_joke)
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        )
    )

ft.app(target=main)

