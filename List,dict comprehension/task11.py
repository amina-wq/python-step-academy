# Реализовать инженерный калькулятор, для всех арифметических действий, 
# включая нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения числа в степени. 
# В ходе решения, допустимо использования модуля math, функции определяемой пользователем, рекурсивной функции и лямбда-функции. 
# Реализуйте диалог с пользователем. 

import customtkinter

class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Калькулятор")
        self.geometry(f'{300}x{400}')

        name_buttons = [
            "n!", "fib", "^", "R", "B",
            "sin", "cos", "tg", "ctg", "pi",
            "7", "8", "9", "+", "*",
            "4", "5", "6", "-", "/",
            "1", "2", "3", ".", "="
        ]

        self.buttons = {name: customtkinter.CTkButton(master=self, text=name, command=self.button_callback) for name in name_buttons}

        for idx, button in enumerate(self.buttons.items()):
            button.grid(row=idx // 5, column=idx % 5) 

        # for idx, button in enumerate(self.buttons):
        #   button.grid(row=idx // 5, column=idx % 5)
        # 1. idx = 0, button = n!, row = 0, column = 0
        # 2. idx = 1, button = fib, row = 0, column = 1
        # 3. idx = 2, button = ^, row = 0, column = 2
        # 4. idx = 3, button = R, row = 0, column = 3
        # 5. idx = 4, button = B, row = 0, column = 4
        # 6. idx = 5, button = sin, row = 1, column = 0
        # 7. idx = 6, button = cos, row = 1, column = 1
        # 8. idx = 7, button = tg, row = 1, column = 2
        # 9. idx = 8, button = ctg, row = 1, column = 3
        # 10. idx = 9, button = pi, row = 1, column = 4
        # 11. idx = 10, button = 7, row = 2, column = 0
        # 12. idx = 11, button = 8, row = 2, column = 1
        # 13. idx = 12, button = 9, row = 2, column = 2
        # 14. idx = 13, button = +, row = 2, column = 3
        # 15. idx = 14, button = *, row = 2, column = 4
        # 16. idx = 15, button = 4, row = 3, column = 0
        # 17. idx = 16, button = 5, row = 3, column = 1
        # 18. idx = 17, button = 6, row = 3, column = 2
        # 19. idx = 18, button = -, row = 3, column = 3
        # 20. idx = 19, button = /, row = 3, column = 4
        # 21. idx = 20, button = 1, row = 4, column = 0
        # 22. idx = 21, button = 2, row = 4, column = 1
        # 23. idx = 22, button = 3, row = 4, column = 2
        # 24. idx = 23, button = ., row = 4, column = 3
        # 25. idx = 24, button = =, row = 4, column = 4

    def button_callback(self):
        ...

if __name__ == "__main__":
    app = App()
    app.mainloop()