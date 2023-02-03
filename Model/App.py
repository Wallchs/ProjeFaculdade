import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Caixa de Ferramentas")
        self.minsize(400, 300)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("Funciona")
