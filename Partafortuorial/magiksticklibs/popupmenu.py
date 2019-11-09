from .Graphics import Tkinter

class Popup:
    def __init__(self,text):
        # self._words = ["check","you","she","is","donkey"]
        self._words=open("/usr/share/dict/words").read().split("\n")

        self.text = text
        # self.text.tag_configure("bold", font=bold_font)
        self.text.tag_configure("misspelled", foreground="red", underline=True)
        self.functions_binding_key()
        self.functions_configurations()

    def functions_configurations(self):
        self.menu = Tkinter.Menu(self.text.master)
        self.menu.add_command(label = "Copy",command = self.text.storeobj['Copy'])
        self.menu.add_command(label = "Cut",command = self.text.storeobj['Cut'])
        self.menu.add_command(label = "Paste",command = self.text.storeobj['Paste'])
        self.menu.add_separator()
        self.menu.add_command(label = "Select All",command = self.text.storeobj['SelectAll'])
        self.menu.add_separator()
        return


    def functions_binding_key(self):
        self.text.bind("<Button-3>",self.show_menu_)
        self.text.bind("<space>", self.spellcheck_exp_)
        return

    def show_menu_(self,event):
        self.menu.tk_popup(event.x,event.y)
        # self.menu.
        return
    def spellcheck_exp_(self,event):

        # def Spellcheck(self, event):
        '''Spellcheck the word preceeding the insertion point'''
        index = self.text.search(r'\s', "insert", backwards=True, regexp=True)
        print("Reached")
        if index == "":
            index = "1.0"
        else:
            index = self.text.index("%s+1c" % index)
        word = self.text.get(index, "insert")
        if word in self._words:
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        else:
            self.text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))


if __name__ == '__main__':
    root = Tkinter.Tk()
    text = Tkinter.Text()
    text.pack()
    text.storeobj = {'SelectAll':None, "Copy":None, "Cut":None, "Paste":None,}
    Popup(text)
    root.mainloop()
