import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('370x390+500+150')
        self.title('Calculator with tkinter')
        self.iconbitmap('calculator.ico')

        self._entry_text = tk.StringVar(value='...')
        self._entry = tk.Entry(self, width=60, justify=tk.LEFT, textvariable=self._entry_text)
        self._entry.grid(column=0, row=0, columnspan=4, ipady=10, sticky='NSWE')

        self._buttons()

        self.mainloop()

    def button_clicked(self, button_pressed):
        if button_pressed == 17:
            self._entry.delete(0, 'end')
        elif button_pressed == 16:
            self._entry.insert(0, '/')
        elif button_pressed == 15:
            self._entry.insert(0, '*')
        elif button_pressed == 14:
            self._entry.insert(0, '-')
        elif button_pressed == 13:
            self._entry.insert(0, '+')

        elif button_pressed == 12:
            self._entry.insert(0, '')

        elif button_pressed == 11:
            self._entry.insert(0, '.')
        elif button_pressed == 10:
            self._entry.insert(0, '9')
        elif button_pressed == 9:
            self._entry.insert(0, '8')
        elif button_pressed == 8:
            self._entry.insert(0, '7')
        elif button_pressed == 7:
            self._entry.insert(0, '6')
        elif button_pressed == 6:
            self._entry.insert(0, '5')
        elif button_pressed == 5:
            self._entry.insert(0, '4')
        elif button_pressed == 4:
            self._entry.insert(0, '3')
        elif button_pressed == 3:
            self._entry.insert(0, '2')
        elif button_pressed == 2:
            self._entry.insert(0, '1')
        elif button_pressed == 1:
            self._entry.insert(0, '0')

    def _buttons(self):

        # functions

        clean = tk.Button(self, text='C', height=4, width=35, bg='lightgrey', command=lambda: self.button_clicked(17))
        clean.grid(column=0, row=1, columnspan=3, sticky='NSWE')

        division = tk.Button(self, text='/', width=15, bg='lightgrey', command=lambda: self.button_clicked(16))
        division.grid(column=3, row=1, sticky='NSWE')

        multiply = tk.Button(self, text='*', width=15, bg='lightgrey', command=lambda: self.button_clicked(15))
        multiply.grid(column=3, row=2, sticky='NSWE')

        subtract = tk.Button(self, text='-', width=15, bg='lightgrey', command=lambda: self.button_clicked(14))
        subtract.grid(column=3, row=3, sticky='NSWE')

        sum = tk.Button(self, text='+', width=15, bg='lightgrey', command=lambda: self.button_clicked(13))
        sum.grid(column=3, row=4, sticky='NSWE')

        equals = tk.Button(self, text='=', width=15, bg='lightgrey', height=4, command=lambda: self.button_clicked(12))
        equals.grid(column=3, row=5, sticky='NSWE')

        decimal = tk.Button(self, text='.', width=1, bg='lightgrey', height=4, command=lambda: self.button_clicked(11))
        decimal.grid(column=2, row=5, sticky='NSWE')

        # numbers
        zero = tk.Button(self, text='0', width=15, height=4, command=lambda: self.button_clicked(1))
        zero.grid(column=0, row=5, sticky='NSWE', columnspan=2)

        one = tk.Button(self, text='1', width=1, height=4, command=lambda: self.button_clicked(2))
        one.grid(column=0, row=4, sticky='NSWE')

        two = tk.Button(self, text='2', width=1, height=4, command=lambda: self.button_clicked(3))
        two.grid(column=1, row=4, sticky='NSWE')

        three = tk.Button(self, text='3', width=1, height=4, command=lambda: self.button_clicked(4))
        three.grid(column=2, row=4, sticky='NSWE')

        four = tk.Button(self, text='4', width=1, height=4, command=lambda: self.button_clicked(5))
        four.grid(column=0, row=3, sticky='NSWE')

        five = tk.Button(self, text='5', width=1, height=4, command=lambda: self.button_clicked(6))
        five.grid(column=1, row=3, sticky='NSWE')

        six = tk.Button(self, text='6', width=1, height=4, command=lambda: self.button_clicked(7))
        six.grid(column=2, row=3, sticky='NSWE')

        seven = tk.Button(self, text='7', width=1, height=4, command=lambda: self.button_clicked(8))
        seven.grid(column=0, row=2, sticky='NSWE')

        eight = tk.Button(self, text='8', width=1, height=4, command=lambda: self.button_clicked(9))
        eight.grid(column=1, row=2, sticky='NSWE')

        nine = tk.Button(self, text='9', width=1, height=4, command=lambda: self.button_clicked(10))
        nine.grid(column=2, row=2, sticky='NSWE')


calculator = Calculator()
