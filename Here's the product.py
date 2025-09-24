from tkinter import *

window= Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

num1=Entry()
num2=Entry()
def product():

    number1=num1.get()
    number2=num2.get()
    product=number1*number2
    
    text_box.insert(END,product)
    

text_box= Text(height=2)  

btn= Button(text="Product", command=product, height=1)

num1.pack()
num2.pack()
text_box.pack()
text_box.place(y=100)
btn.pack()

window.mainloop()


