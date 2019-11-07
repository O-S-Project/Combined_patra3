# #enrixpad is free software: you can redistribute it and/or modify
#
# #it under the terms of the GNU General Public License as published by
#
# #the Free Software Foundation, either version 3 of the License, or
#
# #(at your option) any later version.
#
#
#
#
#
# #This program is distributed in the hope that it will be useful,
#
# #but WITHOUT ANY WARRANTY; without even the implied warranty of
#
# #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#
# #GNU General Public License for more details.
#
#
#
#
#
# #You should have received a copy of the GNU General Public License
#
# #along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#
#
# # -*- coding: cp1252 -*-
#
# from Tkinter import *
#
# import tkFileDialog
#
# import tkMessageBox
#
# from tkColorChooser import askcolor
#
# import datetime
#
# import webbrowser
#
# from tkFileDialog import askopenfilename, asksaveasfilename
#
#
#
#
#
# def line():
#
#     lin = "_" * 60
#
#     text.insert(INSERT,lin)
#
#
#
# def date():
#
#     data = datetime.date.today()
#
#     text.insert(INSERT,data)
#
#
#
# def normal():
#
#     text.config(font = ("Arial", 10))
#
#
#
# def bold():
#
#     text.config(font = ("Arial", 10, "bold"))
#
#
#
# def underline():
#
#     text.config(font = ("Arial", 10, "underline"))
#
#
#
# def italic():
#
#     text.config(font = ("Arial",10,"italic"))
#
#
#
# def font():
#
#     (triple,color) = askcolor()
#
#     if color:
#
#        text.config(foreground=color)
#
#
#
# def kill():
#
#     root.destroy()
#
#
#
# def about():
#
#     pass
#
#
#
# def opn():
#
#     text.delete(1.0 , END)
#
#     file = open(askopenfilename() , 'r')
#
#     if file != '':
#
#         txt = file.read()
#
#         text.insert(INSERT,txt)
#
#     else:
#
#         pass
#
#
#
# def save():
#
#     filename = asksaveasfilename()
#
#     if filename:
#
#         alltext = text.get(1.0, END)
#
#         open(filename, 'w').write(alltext)
#
#
#
# def copy():
#
#     text.clipboard_clear()
#
#     text.clipboard_append(text.selection_get())
#
#
#
# def paste():
#
#     try:
#
#         teext = text.selection_get(selection='CLIPBOARD')
#
#         text.insert(INSERT, teext)
#
#     except:
#
#         tkMessageBox.showerror("Errore","Gli appunti sono vuoti!")
#
#
#
# def clear():
#
#     sel = text.get(SEL_FIRST, SEL_LAST)
#
#     text.delete(SEL_FIRST, SEL_LAST)
#
#
#
# def clearall():
#
#     text.delete(1.0 , END)
#
#
#
# def background():
#
#     (triple,color) = askcolor()
#
#     if color:
#
#        text.config(background=color)
#
#
#
# def about():
#
#     ab = Toplevel(root)
#
#     txt = "Fork me"
#
#     la = Label(ab,text=txt,foreground='blue')
#
#     la.pack()
#
#
#
# def web():
#
#     webbrowser.open('http://www.enrixweb.altervista.org')
#
#
#
#
#
# root = Tk()
#
# root.title("Enrix's pad")
#
# menu = Menu(root)
#
#
#
# filemenu = Menu(root)
#
# root.config(menu = menu)
#
# menu.add_cascade(label="File", menu=filemenu)
#
# filemenu.add_command(label="Apri...", command=opn)
#
# filemenu.add_command(label="Salva...", command=save)
#
# filemenu.add_separator()
#
# filemenu.add_command(label="Esci", command=kill)
#
#
#
# modmenu = Menu(root)
#
# menu.add_cascade(label="Modifica",menu = modmenu)
#
# modmenu.add_command(label="Copia", command = copy)
#
# modmenu.add_command(label="Incolla", command=paste)
#
# modmenu.add_separator()
#
# modmenu.add_command(label = "Cancella selezione", command = clear)
#
# modmenu.add_command(label = "Cancella Tutto", command = clearall)
#
#
#
#
#
#
#
# insmenu = Menu(root)
#
# menu.add_cascade(label="Inserisci",menu= insmenu)
#
# insmenu.add_command(label="Data",command=date)
#
# insmenu.add_command(label="Linea",command=line)
#
#
#
#
#
#
#
#
#
# formatmenu = Menu(menu)
#
# menu.add_cascade(label="Formato",menu = formatmenu)
#
# formatmenu.add_cascade(label="Colore...", command = font)
#
# formatmenu.add_separator()
#
# formatmenu.add_radiobutton(label='Normale',command=normal)
#
# formatmenu.add_radiobutton(label='Grassetto',command=bold)
#
# formatmenu.add_radiobutton(label='Sottolineato',command=underline)
#
# formatmenu.add_radiobutton(label='Corsivo',command=italic)
#
#
#
# persomenu = Menu(root)
#
# menu.add_cascade(label="Personalizza",menu=persomenu)
#
# persomenu.add_command(label="Sfondo...", command=background)
#
#
#
# helpmenu = Menu(menu)
#
# menu.add_cascade(label="?", menu=helpmenu)
#
# helpmenu.add_command(label="Info su Snackepad", command=about)
#
# helpmenu.add_command(label="Website", command = web)
#
# text = Text(root, height=30, width=60, font = ("Arial", 10))
#
#
#
#
#
#
#
#
#
# scroll = Scrollbar(root, command=text.yview)
#
# scroll.config(command=text.yview)
#
# text.config(yscrollcommand=scroll.set)
#
# scroll.pack(side=RIGHT, fill=Y)
#
# text.pack()
#
#
#
#
#
# root.resizable(0,0)
#
# root.mainloop()








import wx
import os.path


class MainWindow(wx.Frame):
    def __init__(self, filename='noname.txt'):
        super(MainWindow, self).__init__(None, size=(400,200))
        self.filename = filename
        self.dirname = '.'
        self.CreateInteriorWindowComponents()
        self.CreateExteriorWindowComponents()

    def CreateInteriorWindowComponents(self):
        ''' Create "interior" window components. In this case it is just a
            simple multiline text control. '''
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

    def CreateExteriorWindowComponents(self):
        ''' Create "exterior" window components, such as menu and status
            bar. '''
        self.CreateMenu()
        self.CreateStatusBar()
        self.SetTitle()

    def CreateMenu(self):
        fileMenu = wx.Menu()
        for id, label, helpText, handler in \
            [(wx.ID_ABOUT, '&About', 'Information about this program',
                self.OnAbout),
             (wx.ID_OPEN, '&Open', 'Open a new file', self.OnOpen),
             (wx.ID_SAVE, '&Save', 'Save the current file', self.OnSave),
             (wx.ID_SAVEAS, 'Save &As', 'Save the file under a different name',
                self.OnSaveAs),
             (None, None, None, None),
             (wx.ID_EXIT, 'E&xit', 'Terminate the program', self.OnExit)]:
            if id == None:
                fileMenu.AppendSeparator()
            else:
                item = fileMenu.Append(id, label, helpText)
                self.Bind(wx.EVT_MENU, handler, item)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File') # Add the fileMenu to the MenuBar
        self.SetMenuBar(menuBar)  # Add the menuBar to the Frame

    def SetTitle(self):
        # MainWindow.SetTitle overrides wx.Frame.SetTitle, so we have to
        # call it using super:
        super(MainWindow, self).SetTitle('Editor %s'%self.filename)


    # Helper methods:

    def defaultFileDialogOptions(self):
        ''' Return a dictionary with file dialog options that can be
            used in both the save file dialog as well as in the open
            file dialog. '''
        return dict(message='Choose a file', defaultDir=self.dirname,
                    wildcard='*.*')

    def askUserForFilename(self, **dialogOptions):
        dialog = wx.FileDialog(self, **dialogOptions)
        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.filename = dialog.GetFilename()
            self.dirname = dialog.GetDirectory()
            self.SetTitle() # Update the window title with the new filename
        else:
            userProvidedFilename = False
        dialog.Destroy()
        return userProvidedFilename

    # Event handlers:

    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, 'A sample editor\n'
            'in wxPython', 'About Sample Editor', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def OnExit(self, event):
        self.Close()  # Close the main window.

    def OnSave(self, event):
        textfile = open(os.path.join(self.dirname, self.filename), 'w')
        textfile.write(self.control.GetValue())
        textfile.close()

    def OnOpen(self, event):
        if self.askUserForFilename(style=wx.OPEN,
                                   **self.defaultFileDialogOptions()):
            textfile = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(textfile.read())
            textfile.close()

    def OnSaveAs(self, event):
        if self.askUserForFilename(defaultFile=self.filename, style=wx.SAVE,
                                   **self.defaultFileDialogOptions()):
            self.OnSave(event)


app = wx.App()
frame = MainWindow()
frame.Show()
app.MainLoop()
