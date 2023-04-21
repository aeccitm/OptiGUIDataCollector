from tkinter import *
from PIL import Image, ImageTk

class ImageDisplay:
    def __init__(self, filename):
        self.filename = filename

    def display_image(self):
        root = Tk()
        root.title("Display image")
        img = Image.open(self.filename)
        ima = ImageTk.PhotoImage(img)
        label = Label(root, image=ima)
        label.pack()
        def close_window():
            root.destroy()
        root.after(5000, close_window)
        root.mainloop()


if __name__ == '__main__':
    pass
