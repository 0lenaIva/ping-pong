from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.host = 'localhost'
        self.port = 8080

        self.geometry("300x300")
        CTkLabel(self, text='LOGIN...').pack(padx=10, pady=(50, 15), fill='x')
        self.entry_host = CTkEntry(self, placeholder_text='HOST')
        self.entry_port = CTkEntry(self, placeholder_text='PORT')
        self.submit = CTkButton(self, text='SUBMIT', command=self.open_game)

        self.entry_host.pack(padx=10, pady=15, fill='x')
        self.entry_port.pack(padx=10, pady=15, fill='x')

        self.submit.pack(padx=10, pady=15, fill='x')

    def open_game(self):
        try:
            self.host = self.entry_host.get()
            self.port = int(self.entry_port.get())
            self.destroy()
        except:
            pass