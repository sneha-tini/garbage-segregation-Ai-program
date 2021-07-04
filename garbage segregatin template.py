from tkinter import *
from PIL import ImageTk ,Image
root=Tk()
#go to your cmd and type this:pip install pillow
my_img1 = ImageTk.PhotoImage(Image.open("images/plastic.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/dustbin.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/logo.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/truck.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/grabage.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label= Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)
def test():
    print("Hello World")

def forward(n):
    global button_forward
    global button_back
    global my_label

    my_label.grid_forget()
    my_label=Label(image=image_list[n-1])
    button_forward=Button(root,text=">>",command=lambda:forward(n+1))
    button_back=Button(root,text="<<",command=lambda:back(n-1))
    my_label.grid(row=0,colunm=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
def back():
    global button_forward
    global button_back
    global my_label
button_back=Button(root,text="<<",command=back)
button_exit=Button(root,text="Exit Program",command=root.destroy)
button_forward=Button(root,text=">>",command=lambda:forward(2))
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

tkWindow = Tk()

button1 = Button(tkWindow)
button1['command'] = test


root.title("welcome to Garbage segregation program")
label1=Label(root,text="Welcome to our garbage separation AI based program")
label1.grid(row=2,column=0)
button1=Button(root,text="plastic",padx=50,pady=20,fg="black",bg="white",)
button2=Button(root,text="glass",padx=50,pady=20,fg="black",bg="white")
button3=Button(root,text="paper",padx=50,pady=20,fg="black",bg="white")
button1.grid(row =3,column=0)
button2.grid(row=4,column=0)
button3.grid(row=5,column=0)
root.mainloop()
