from tkinter import *
          
window = Tk()
window.title("James Python Project")             # 視窗標題


text = Text(window,height=800,width=600)
text.insert(END,"abcdefg")
text.pack()


window.mainloop()