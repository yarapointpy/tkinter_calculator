import tkinter as tk
from tkinter import messagebox


class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('370x390+500+150')
        self.title('Calculator with tkinter')
        self.iconbitmap('calculator.ico')

        self._entry_text = tk.StringVar()

        self._expression = ''

        self._buttons()

        self.mainloop()

    def button_clicked(self, button_pressed):
        self._expression = f'{self._expression}{button_pressed}'
        self._entry_text.set(self._expression)

    def _generate(self):

        try:
            if self._expression:
                # eval evaluates the string expression like an arithmetic expression
                result = str(eval(self._expression))
                self._entry_text.set(result)

        except Exception as e:
            self._expression = f'Error: {e}'
            messagebox.showerror('Warning, an error has occurred', f'Error: {e}.')
            self._clean()
            self._entry.focus()

    def _clean(self):
        self._expression = ''
        self._entry_text.set(self._expression)

    def _buttons(self):
        self._entry = tk.Entry(self, width=60, justify=tk.LEFT, textvariable=self._entry_text)
        self._entry.grid(column=0, row=0, columnspan=4, ipady=10, sticky='NSWE')

        clean = tk.Button(self, text='C', height=4, width=35, bg='lightgrey', command=self._clean)
        clean.grid(column=0, row=1, columnspan=3, sticky='NSWE')

        division = tk.Button(self, text='/', width=15, bg='lightgrey', command=lambda: self.button_clicked('/'))
        division.grid(column=3, row=1, sticky='NSWE')

        multiply = tk.Button(self, text='*', width=15, bg='lightgrey', command=lambda: self.button_clicked('*'))
        multiply.grid(column=3, row=2, sticky='NSWE')

        subtract = tk.Button(self, text='-', width=15, bg='lightgrey', command=lambda: self.button_clicked('-'))
        subtract.grid(column=3, row=3, sticky='NSWE')

        sum = tk.Button(self, text='+', width=15, bg='lightgrey', command=lambda: self.button_clicked('+'))
        sum.grid(column=3, row=4, sticky='NSWE')

        equals = tk.Button(self, text='=', width=15, bg='lightgrey', height=4, command=self._generate)
        equals.grid(column=3, row=5, sticky='NSWE')

        decimal = tk.Button(self, text='.', width=1, bg='lightgrey', height=4, command=lambda: self.button_clicked('.'))
        decimal.grid(column=2, row=5, sticky='NSWE')

        # numbers

        button_zero = tk.Button(self, text='0', width=15, height=4, command=lambda: self.button_clicked(0))
        button_zero.grid(column=0, row=5, sticky='NSWE', columnspan=2)

        button_one = tk.Button(self, text='1', width=1, height=4, command=lambda: self.button_clicked(1))
        button_one.grid(column=0, row=4, sticky='NSWE')

        button_two = tk.Button(self, text='2', width=1, height=4, command=lambda: self.button_clicked(2))
        button_two.grid(column=1, row=4, sticky='NSWE')

        button_three = tk.Button(self, text='3', width=1, height=4, command=lambda: self.button_clicked(3))
        button_three.grid(column=2, row=4, sticky='NSWE')

        button_four = tk.Button(self, text='4', width=1, height=4, command=lambda: self.button_clicked(4))
        button_four.grid(column=0, row=3, sticky='NSWE')

        button_five = tk.Button(self, text='5', width=1, height=4, command=lambda: self.button_clicked(5))
        button_five.grid(column=1, row=3, sticky='NSWE')

        button_six = tk.Button(self, text='6', width=1, height=4, command=lambda: self.button_clicked(6))
        button_six.grid(column=2, row=3, sticky='NSWE')

        button_seven = tk.Button(self, text='7', width=1, height=4, command=lambda: self.button_clicked(7))
        button_seven.grid(column=0, row=2, sticky='NSWE')

        button_eight = tk.Button(self, text='8', width=1, height=4, command=lambda: self.button_clicked(8))
        button_eight.grid(column=1, row=2, sticky='NSWE')

        button_nine = tk.Button(self, text='9', width=1, height=4, command=lambda: self.button_clicked(9))
        button_nine.grid(column=2, row=2, sticky='NSWE')


if __name__ == '__main__':
    calculator = Calculator()
