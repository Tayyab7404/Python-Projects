from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        root.title("Captain Music Player")
        root.geometry("320x100")
        root.resizable(0, 0)

        # Buttons
        Load = Button(root, text="LOAD", width=10, font=('Times', 10), command= self.load)
        Load.place(x=20, y=30)
        Play = Button(root, text="PLAY", width=10, font=('Times', 10), command= self.play)
        Play.place(x=120, y=30)
        Stop = Button(root, text="STOP", width=10, font=('Times', 10), command= self.stop)
        Stop.place(x=220, y=30)

        self.music_file = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def stop(self):
        mixer.music.stop()


root = Tk()
App = MusicPlayer(root)
root.mainloop()