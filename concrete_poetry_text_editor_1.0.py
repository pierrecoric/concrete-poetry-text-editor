from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
##########
root = Tk (className = " Concrete Poetry Text Editor 1.0")
textArea = scrolledtext.ScrolledText(root, width = 100, height = 100, bg = "white", fg = "black", highlightcolor = "blue", insertbackground = "blue", selectbackground = "blue")
textArea.pack()
##########
vowels = ("a","e","i","o","u","A","E","I","O","U")
counterVersions = 0
textVersions = []
#
#FUNCTIONS:
##########
#
#general functions
##########
def clearEverything():
    textArea.delete("1.0", END)
##########
def savePreviousVersions(newVersion):
    global counterVersions
    textVersions.append(newVersion)
    print(textVersions[counterVersions])
    counterVersions += 1
#
#file functions
##########
def newFile():
    if len(textArea.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("do you want to save your file?"):
            saveFile()
        else:
            clearEverything()
            global counterVersions
            counterVersions = 0
##########
def openFile():
    if messagebox.askyesno("do you want to save your file?"):
        saveFile()
    file = filedialog.askopenfile(parent = root, mode = "rb", title = "select a file")
    if file != None:
        clearEverything()
        contents = file.read()
        textArea.insert("1.0", contents)
        global counterVersions
        counterVersions = 0
        file.close()
##########
def saveFile():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        contents = textArea.get("1.0", END+"-1c")
        file.write(contents)
        file.close()
##########
def findInFile():
    findString = simpledialog.askstring("Find", "Enter Text")
##########
def exitRoot():
    if messagebox.askyesno("Quit","Are you sure?"):
        if messagebox.askyesno("do you want to save your file?"):
            saveFile()
        root.destroy()
##########
def undoAction():
    global counterVersions
    if counterVersions > 0:
        counterVersions -= 1
        newContents = textVersions[counterVersions]
        clearEverything()
        textArea.insert("1.0", newContents)
    else:
        return
#
#concrete functions
##########
def upperEverything():
    if messagebox.askyesno("capitalize everything", "are you sure)"):
        contents = textArea.get("1.0", END+"-1c")
        savePreviousVersions(contents)
        contents = contents.upper()
        clearEverything()
        textArea.insert("1.0", contents)
##########
def findAndReplace():
    findAndReplaceString = simpledialog.askstring("what do you want to replace?", "enter text")
    ReplacementString = simpledialog.askstring("by what?", "enter text")
    contents = textArea.get("1.0", END)
    savePreviousVersions(contents)
    if len(findAndReplaceString) > 0:
        clearEverything()
        textArea.insert("1.0",contents.replace(findAndReplaceString,ReplacementString))
##########
def replaceEveryVowel():
    newContents = ("")
    substitutionVowel = simpledialog.askstring("By what do you want to replace every vowel?", "enter text")
    contents = textArea.get("1.0", END)
    savePreviousVersions(contents)
    clearEverything()
    for char in contents:
        if char in vowels:
            char = char.replace(char,substitutionVowel)
        newContents = (newContents + char)
    textArea.insert("1.0",newContents)
#
#concrete selection menu
##########
def replaceEverySignBy():
    contents = textArea.get("1.0", END)
    savePreviousVersions(contents)
    substitutionElement = simpledialog.askstring("By what do you want to replace every sign?", "enter text")
    replaceSelectionString = ("")
    replaceSelectionString = textArea.selection_get()
    lenghtSelection = len(textArea.selection_get())
    count = 0
    replaceSelectionString = ("")
    while (count < lenghtSelection):
        replaceSelectionString = (replaceSelectionString + substitutionElement)
        count += 1
    contents = (contents.replace(textArea.selection_get(), replaceSelectionString))
    clearEverything()
    textArea.insert("1.0", contents)
#
#help functions
##########
#
#about functions
##########
def about():
    label = messagebox.showinfo("About","concrete poetry text editor")
#
#Menu Options
##########
menu= Menu(root)
root.config(menu=menu)
#
#file menu
##########
fileMenu = Menu(menu)
menu.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="New", command = newFile)
fileMenu.add_command(label="Open", command = openFile)
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_command(labe="Find", command = findInFile)
fileMenu.add_separator
fileMenu.add_command(label="Undo", command = undoAction)
fileMenu.add_separator
fileMenu.add_command(label="Exit", command = exitRoot)
#
#concrete menu
##########
concreteMenu = Menu(menu)
menu.add_cascade(label = "concrete", menu=concreteMenu)
concreteMenu.add_command(label = "capitalize everything", command = upperEverything)
concreteMenu.add_command(label = "find and replace", command = findAndReplace)
concreteMenu.add_command(label = "replace every vowel", command = replaceEveryVowel)
concreteMenu.add_separator
#concrete selection menu
##########
concreteSelectionMenu = Menu(menu)
concreteMenu.add_cascade(label="selection", menu = concreteSelectionMenu)
concreteSelectionMenu.add_command(label = "replace evey sign by", command = replaceEverySignBy)
#
#help menu
##########
helpMenu = Menu(menu)
menu.add_cascade(label="help", menu=helpMenu)
#
#about menu
##########
aboutMenu = Menu(menu)
menu.add_cascade(label="about", menu=aboutMenu)
aboutMenu.add_command(label = "about", command = about)
##########
##########
##########
root.mainloop()
