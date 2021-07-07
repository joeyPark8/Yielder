compositionFilePath = 'C://Users//USER//source//repos//Project28//Project28//data//composition.txt'

def load():
    with open(compositionFilePath):
        pass

def onClicked():
    pass



import tkinter

window = tkinter.Tk()
window.title('Yielder')
window.resizable(False, False)
window.geometry('640x480+300+100')

btn_set_proportion = tkinter.Button(text='hello', command=onClicked)
btn_set_proportion.pack()

window.mainloop()