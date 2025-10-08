import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator")
        self.geometry("350x450")
        self.resizable(False, False)
        self.expression = ""
        self.entry = tk.Entry(self, font=("Arial", 20), bd=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="we")
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('.', '0', '=', '+'),
        ]
        for r, row in enumerate(buttons, 1):
            for c, ch in enumerate(row):
                action = (lambda ch=ch: self.on_click(ch))
                b = tk.Button(self, text=ch, font=("Arial", 18), command=action)
                b.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        clear = tk.Button(self, text="C", font=("Arial", 18), command=self.clear)
        clear.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
        back = tk.Button(self, text="⌫", font=("Arial", 18), command=self.backspace)
        back.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)
        par1 = tk.Button(self, text="(", font=("Arial", 18), command=lambda: self.on_click('('))
        par2 = tk.Button(self, text=")", font=("Arial", 18), command=lambda: self.on_click(')'))
        par1.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)
        par2.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def on_click(self, ch):
        if ch == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += ch
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
