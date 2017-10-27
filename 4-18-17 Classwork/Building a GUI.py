import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.title = self.main_window.title('A Truey GUI')
        self.label = tkinter.Label(self.main_window, text='I am a label!')
        self.label.pack(side='right')
        self.button = tkinter.Button(self.main_window, text='Press me!!')
        self.button.pack()
        tkinter.mainloop()

def main():
    gui = GUI()
main()
