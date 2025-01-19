import tkinter as tk
from tkinter import ttk
import math


class HP12C:
    def __init__(self):
        self.stack = [0.0] * 4  # RPN stack (X, Y, Z, T registers)
        self.memory = 0.0
        self.display = "0"
        self.entering = False
        self.decimal_entered = False
        self.decimal_places = 2

    def push(self, value):
        self.stack.pop()  # Remove T
        self.stack.insert(0, float(value))  # Push new value to X

    def enter(self):
        if self.entering:
            self.push(self.stack[0])
        self.entering = False
        self.decimal_entered = False

    def digit(self, num):
        if not self.entering:
            self.display = str(num)
            self.entering = True
        else:
            if self.decimal_entered:
                self.display += str(num)
            else:
                self.display = self.display.rstrip('0').rstrip('.') if '.' in self.display else self.display
                self.display = str(float(self.display + str(num)))
        self.stack[0] = float(self.display)

    def decimal(self):
        if not self.decimal_entered:
            if not self.entering:
                self.display = "0."
                self.entering = True
            else:
                self.display += "."
            self.decimal_entered = True

    def clear_x(self):
        self.stack[0] = 0.0
        self.display = "0"
        self.entering = False
        self.decimal_entered = False

    def operation(self, op):
        self.enter()
        x, y = self.stack[0], self.stack[1]

        if op == '+':
            result = y + x
        elif op == '-':
            result = y - x
        elif op == '*':
            result = y * x
        elif op == '/':
            result = y / x if x != 0 else float('inf')
        elif op == 'sqrt':
            result = math.sqrt(x) if x >= 0 else float('nan')
        elif op == '1/x':
            result = 1 / x if x != 0 else float('inf')
        elif op == '%':
            result = (y * x) / 100
        elif op == 'chs':
            result = -x

        self.stack.pop(0)  # Remove X
        self.stack.insert(0, result)  # Insert result as new X
        self.display = str(result)
        self.entering = False


class HP12CCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("HP 12c Calculator")
        self.calc = HP12C()

        # Display
        self.display_var = tk.StringVar(value="0")
        display = ttk.Entry(root, textvariable=self.display_var, justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

        # Buttons configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0), ('.', 4, 1), ('±', 4, 2),
            ('ENTER', 1, 3), ('+', 2, 3), ('-', 3, 3),
            ('*', 4, 3), ('/', 5, 3),
            ('CLX', 5, 0), ('√x', 5, 1), ('1/x', 5, 2)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            cmd = lambda x=text: self.button_click(x)
            ttk.Button(root, text=text, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        # Configure grid
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def button_click(self, button):
        if button.isdigit():
            self.calc.digit(int(button))
        elif button == '.':
            self.calc.decimal()
        elif button == 'ENTER':
            self.calc.enter()
        elif button == 'CLX':
            self.calc.clear_x()
        elif button == '±':
            self.calc.operation('chs')
        elif button in ['+', '-', '*', '/']:
            self.calc.operation(button)
        elif button == '√x':
            self.calc.operation('sqrt')
        elif button == '1/x':
            self.calc.operation('1/x')

        self.display_var.set(self.calc.display)


def main():
    root = tk.Tk()
    app = HP12CCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()