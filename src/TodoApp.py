try:
    import os
    import sv_ttk
    import tkinter
    import ntkutils
    import webbrowser
    import darkdetect
    from typing import Literal
    from typing_extensions import Self
    from tkinter.__init__ import (Listbox , StringVar)
    from tkinter.ttk import (Notebook , Button , Frame)
    from customtkinter.widgets.ctk_entry import CTkEntry
    from customtkinter.widgets.ctk_button import CTkButton
    
    from Management import Materials

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run The Application') from None

finally:
    ...
    
    

    
    

class TodoApp:
    def __init__(self : Self) -> Literal[None]:
        super(TodoApp , self).__init__()
        self.root = tkinter.Tk()
        self.root.title(string='Todo App')
        self.root.resizable(width=False , height=False)
        self.root.geometry(newGeometry='400x650')
        self.root.iconbitmap(bitmap=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__)) , r'images/icon.ico'))
        self.tabControl = Notebook(master=self.root)
        self.tabTodo = Frame(master=self.tabControl)
        self.tabLang = Frame(master=self.tabControl)
        self.tabAbout = Frame(master=self.tabControl)
        self.tabControl.add(child=self.tabTodo , text='Todo')
        self.tabControl.add(child=self.tabLang , text='Language')
        self.tabControl.add(child=self.tabAbout , text='About')
        self.tabControl.pack(expand=1 , fill=Materials.Alignments.both)
        self.svEntry = StringVar(master=self.tabTodo)
        
        def setBySystemTheme() -> Literal[None]:
            if (darkdetect.isLight()):
                sv_ttk.set_theme(theme=Materials.Themes.light)
                self.btnAdd.configure(bg_color=Materials.Colors.white)
                self.btnPA.configure(bg_color=Materials.Colors.white)
                self.btnEN.configure(bg_color=Materials.Colors.white)
                self.btnGithub.configure(bg_color=Materials.Colors.white)
                self.root.update_idletasks()
            if (darkdetect.isDark()):
                sv_ttk.set_theme(theme=Materials.Themes.dark)
                ntkutils.dark_title_bar(window=self.root)
                self.btnAdd.configure(bg_color=Materials.Colors.dark)
                self.btnPA.configure(bg_color=Materials.Colors.dark)
                self.btnEN.configure(bg_color=Materials.Colors.dark)
                self.btnGithub.configure(bg_color=Materials.Colors.dark)
                self.root.update_idletasks()
                
        def changeAppLanguage(arg : str) -> Literal[None]:
            if (arg == 'PA'):
                self.root.title(string='مدیریت وظایف')
                self.tabControl.add(child=self.tabTodo , text='وظایف')
                self.tabControl.add(child=self.tabLang , text='زبان')
                self.tabControl.add(child=self.tabAbout , text='درباره')
                self.btnAdd.configure(text='کردن اضافه')
                self.btnDelete.configure(text='حذف کردن')
                self.btnPA.configure(text='پارسی')
                self.btnEN.configure(text='انگلیسی')
                self.btnGithub.configure(text='گیتهاب')
            if (arg == 'EN'):
                self.root.title(string='Todo App')
                self.tabControl.add(child=self.tabTodo , text='Todo')
                self.tabControl.add(child=self.tabLang , text='Language')
                self.tabControl.add(child=self.tabAbout , text='About')
                self.btnAdd.configure(text='Add')
                self.btnDelete.configure(text='Delete')
                self.btnPA.configure(text='Persian')
                self.btnEN.configure(text='English')
                self.btnGithub.configure(text='Github')
            
        def aboutClickEvent() -> Literal[None]:
            webbrowser.open(url='https://github.com/shervinbdndev')
                
        def addItems(event=None) -> Literal[None]:
            global item
            item = self.svEntry.get()
            if (item != ''):
                self.listBox.insert(tkinter.END , item)
            self.entryTodo.delete(first=0 , last=tkinter.END)
        
        def deleteItems(event=None) -> Literal[None]:
            if (item != ''):
                self.listBox.delete(first=self.listBox.curselection()[0])
                
        self.entryTodo = CTkEntry(
            master=self.tabTodo ,
            textvariable=self.svEntry ,
            corner_radius=5 ,
            width=330 ,
            height=40 ,
            text_font=(Materials.Font.pop , 15) ,
            justify=Materials.Alignments.left ,
            text_color=Materials.Colors.purple ,
            border_color=Materials.Colors.purple ,
            border_width=2 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
        )
        
        self.entryTodo.place(relx=0.5 , rely=0.1 , anchor=Materials.Alignments.center)
        
        self.listBox = Listbox(
            master=self.tabTodo ,
            width=54 ,
            height=25 ,
            font=(Materials.Font.pop , 8 , Materials.FontWeight.bold) ,
            highlightthickness=1 ,
            highlightcolor=Materials.Colors.purple ,
            highlightbackground=Materials.Colors.purple ,
            bd=1 ,
            border=1 ,
            borderwidth=1 ,
            relief=Materials.Reliefs.groove ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            selectbackground=Materials.Colors.purple ,
            selectborderwidth=1 ,
            selectmode=Materials.Modes.single ,
        )
        
        self.listBox.place(relx=0.5 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnAdd = CTkButton(
            master=self.tabTodo ,
            text='Add' ,
            corner_radius=5 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            width=150 ,
            height=45 ,
            fg_color=Materials.Colors.purple ,
            command=addItems ,
        )
        
        self.btnAdd.place(relx=0.27 , rely=0.91 , anchor=Materials.Alignments.center)
        
        self.btnDelete = Button(
            master=self.tabTodo ,
            text='Delete' ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            width=18 ,
            command=deleteItems ,
        )
        
        self.btnDelete.place(relx=0.73 , rely=0.91 , height=45 , anchor=Materials.Alignments.center)
        
        self.btnPA = CTkButton(
            master=self.tabLang ,
            text='Persian' ,
            corner_radius=5 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            width=150 ,
            height=50 ,
            fg_color=Materials.Colors.purple ,
            command=lambda:changeAppLanguage(arg='PA') ,
        )
        
        self.btnPA.place(relx=0.25 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnEN = CTkButton(
            master=self.tabLang ,
            text='English' ,
            corner_radius=5 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            width=150 ,
            height=50 ,
            fg_color=Materials.Colors.purple ,
            command=lambda:changeAppLanguage(arg='EN') ,
        )
        
        self.btnEN.place(relx=0.73 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnGithub = CTkButton(
            master=self.tabAbout ,
            text='Github' ,
            corner_radius=5 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            width=150 ,
            height=45 ,
            fg_color=Materials.Colors.purple ,
            command=aboutClickEvent ,
        )
        
        self.btnGithub.place(relx=0.5 , rely=0.5 , anchor=Materials.Alignments.center)
                
        setBySystemTheme()
        
        self.root.bind(sequence='<Delete>' , func=deleteItems)
        self.entryTodo.bind(sequence='<Return>' , func=addItems)
        
        self.root.mainloop()
        
        
        

def main() -> Literal[None]:
    TodoApp()
    
    
    

if (__name__ == '__main__' and __package__ is None):
    main()