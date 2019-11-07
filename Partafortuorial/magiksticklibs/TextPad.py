from .Graphics import Tkinter
from .ConfigSettings import Connect
class TextPad(Tkinter.Text):
    def __init__(self, *args, **kwargs):
        Tkinter.Text.__init__(self, *args, **kwargs)
        self.storeobj = {}
        self.Connect_External_Module_Features()
        self._pack()

    def _pack(self):
        self.pack(expand = True, fill = "both")
        return

    def Connect_External_Module_Features(self):
        Connect(self)

        return


if __name__ == '__main__':
    root = Tkinter.Tk(className = " Test TextPad")
    TextPad(root)
    root.mainloop()
