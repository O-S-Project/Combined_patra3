import tkinter as Tkinter
from difflib import get_close_matches # for spelling recommendation


# add thread
class Spellcheck:
    """docstring for Spellcheck."""

    # def __init__(self, text):
    #     # super(Spellcheck, self).__init__()
    #     self.text = text
    #     self._words=open("/usr/share/dict/words").read().split("\n")
    #
    #     self.text.tag_configure("misspelled", foreground="red", underline=True)
    #     #highlight it?
    #
    #     self.functions_binding_key()

    def __init__(self, text,statusbar=None):
        # super(Spellcheck, self).__init__()
        self.text = text
        self._words=open("/usr/share/dict/words").read().split("\n")

        self.text.tag_configure("misspelled", foreground="red", underline=True)
        #highlight it?
        self.statusbar = statusbar
        self.functions_binding_key()


    def functions_binding_key(self):

        self.text.bind("<space>", self.spellcheck_exp_)
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
            # sending word recommendation
            # print(self.text[index:])
            print(self.text.get(index,Tkinter.END))
            str11 = self.text.get(index,Tkinter.END).split("\n") #get last word
            print("put this in exception")
            print(str11[0]) #check incorrect word
            print("put this in exception")
            # self.statusbar.update_status1(str11[0])
            word = str11[0]
            patterns = self._words
            wordrec = get_close_matches(word, patterns)
            # wordrec = closeMatches(patterns, word)
            self.statusbar.update_status1(wordrec)











#chedk
