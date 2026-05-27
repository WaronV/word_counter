import tkinter as tk
from logic import ...

class App:
    def __init__(self):
        self.root = tk.Tk() # dlaczego tutaj jest jakies root
        self.root.title("Count Word")

        self. label = tk.Label()
        self.label.pack()

        self.button = tk.Button(self.root, text="Random/Next", command=self.onc_lick)
        self.button.pack()

    def on_click(self):
        data

    def run(self):
        self.root.mainloop()