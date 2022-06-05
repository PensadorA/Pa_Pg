import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from formula import *


class Pa(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        self.s = ttk.Style()
        self.s.configure('Frame1.TFrame', background='#009DAE')
        self.config(style='Frame1.TFrame')
        self.valores_1 = tk.StringVar()
        self.valores_n = tk.StringVar()
        self.valores_r = tk.StringVar()

        # Label termo 1
        self.label_termo_1 = ttk.Label(self, text='Termo 1')
        self.label_termo_1.grid(column=0, row=0, sticky=tk.W, **options)

        # Entry termo 1
        self.entry_termo_1 = ttk.Entry(self, textvariable=self.valores_1)
        self.entry_termo_1.grid(column=1, row=0, sticky=tk.W, **options)

        # Label n termo
        self.label_termo_n = ttk.Label(self, text='Termo 2')
        self.label_termo_n.grid(column=0, row=1, sticky=tk.W, **options)

        # Entry n termo
        self.entry_termo_n = ttk.Entry(self, textvariable=self.valores_n)
        self.entry_termo_n.grid(column=1, row=1, sticky=tk.W, **options)

        # Label razao
        self.label_razao = ttk.Label(self, text='Razão')
        self.label_razao.grid(column=0, row=3, sticky=tk.W, **options)

        # Entry n termo
        self.entry_razao = ttk.Entry(self, textvariable=self.valores_r)
        self.entry_razao.grid(column=1, row=3, sticky=tk.W, **options)

        self.calcular_pa = ttk.Button(self, text='Calcular PA')
        self.calcular_pa.grid(column=3, row=0)
        self.calcular_pa['command'] = self.convert

        self.resultado_pa = ttk.Label(self)
        self.resultado_pa.configure(background='#009DAE')
        self.resultado_pa.grid(column=3, row=1)
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        try:
            resultado = Formulas.pa(
                float(self.valores_1.get()),
                float(self.valores_n.get()),
                float(self.valores_r.get())
            )
            self.resultado_pa['text'] = f'A soma é {resultado}'

        except ValueError as error:
            showerror(title='Error', message=f'{error}')


class Pg(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}

        self.s = ttk.Style()
        self.s.configure('Frame2.TFrame', background='#71DFE7')
        self.config(style='Frame2.TFrame')

        self.valores_1 = tk.StringVar()
        self.valores_n = tk.StringVar()
        self.valores_r = tk.StringVar()

        # Label termo 1
        self.label_termo_1 = ttk.Label(self, text='Termo 1')
        self.label_termo_1.grid(column=0, row=0, sticky=tk.W, **options)

        # Entry termo 1
        self.entry_termo_1 = ttk.Entry(self, textvariable=self.valores_1)
        self.entry_termo_1.grid(column=1, row=0, sticky=tk.W, **options)

        # Label n termo
        self.label_termo_n = ttk.Label(self, text='Termo 2')
        self.label_termo_n.grid(column=0, row=1, sticky=tk.W, **options)

        # Entry n termo
        self.entry_termo_n = ttk.Entry(self, textvariable=self.valores_n)
        self.entry_termo_n.grid(column=1, row=1, sticky=tk.W, **options)

        # Label razao
        self.label_razao = ttk.Label(self, text='Razão')
        self.label_razao.grid(column=0, row=3, sticky=tk.W, **options)

        # Entry n termo
        self.entry_razao = ttk.Entry(self, textvariable=self.valores_r)
        self.entry_razao.grid(column=1, row=3, sticky=tk.W, **options)

        self.calcular_pa = ttk.Button(self, text='Calcular PG')
        self.calcular_pa.grid(column=3, row=0)
        self.calcular_pa['command'] = self.convert

        self.resultado_pg = ttk.Label(self)
        self.resultado_pg.configure(background='#71DFE7')
        self.resultado_pg.grid(column=3, row=1)
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        try:
            resultado = Formulas.pg(
                float(self.valores_1.get()),
                float(self.valores_n.get()),
                float(self.valores_r.get())
            )
            self.resultado_pg['text'] = f'A soma é {resultado}'

        except ValueError as error:
            showerror(title='Error', message=f'{error}')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('PA & PG')
        self.geometry('300x230')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    Pa(app)
    Pg(app)
    app.mainloop()
