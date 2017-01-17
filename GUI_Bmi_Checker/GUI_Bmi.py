#[+] ------------------Graphical BMI Checker---------------------[+]
#this app is only work in python 2.7
from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox

root=Tk()
root['background']="white"
root.title("BMI Checker")
root.iconbitmap('clienticon.ico')

imageFrame = Frame(root)
imageFrame.pack(side=TOP, pady = 2, padx=2)

frame = Frame(root)
frame.pack(side = TOP, pady = 2, padx=2)

frame1 = Frame(root)
frame1.pack(side = TOP, pady = 2, padx=2)

frame2 = Frame(root)
frame2.pack(side = TOP, pady = 2, padx=2)

frame3 = Frame(root)
frame3.pack(side = TOP, pady = 2, padx=2)

frame4 = Frame(root)
frame4.pack(side=TOP, pady = 2, padx=2)

def checkMe():
    weight = entry.get()
    w = int(weight)
    height = entry2.get()
    h = float(height)
    g = (h ** 2)
    a = (w / g)
    lab.configure(text="Your BMI is:")
    label3.configure(text=a)
    lab1.configure(text="the standard BMI is between 19 and 24")

def deleteData():
    lab.configure(text="")
    label3.configure(text="")
    lab1.configure(text="")

def aboutMe():
    return tkMessageBox.showinfo("About Us", "BMI Checker ,Version 0.1\nthis app is developed with Tkinter library in Python 2.7.12\nto use the app payattention to enter the height in meter like: 1.80\nand enter the weight in kg like: 65\n\nProgrammer: Fazel Ahmadi,\nEmail: fazelahmadi32@gmail.com,\n")

img = ImageTk.PhotoImage(Image.open("2000px-Bmi_wordmark.svg_Easy-Resize.com.png"))
imgShow = Label(imageFrame, image = img)
imgShow.pack(side=TOP, fill=BOTH, expand="yes")

lab1 = Label(frame4, text="", bg="white", fg="dark red")
lab1.pack(fill = BOTH)

lab = Label(frame3, bg="white")
lab.pack(side=LEFT, fill = BOTH)

label = Label(frame, text="Enter Your Weight: (only kg)", bg="white")
label.pack(side = LEFT, fill = BOTH)

label1 = Label(frame1, text="Enter Your Height:(only metr)", bg="white")
label1.pack(side = LEFT, fill = BOTH)

entry = Entry(frame)
entry.pack(side = RIGHT, fill = BOTH)

entry2 = Entry(frame1)
entry2.pack(side = RIGHT, fill = BOTH)

label3 =Label(frame3, text="BMI will apear here...", bg="white", fg="dark blue")
label3.pack(fill = BOTH, side = RIGHT)

button = Button(frame2, text="Check My BMI", command = checkMe, bg="#46a3ff", fg="white")
button.pack(side = RIGHT, fill = BOTH)

button1 = Button(frame2, text="Delete result", command = deleteData, bg="#46a3ff", fg="white")
button1.pack(side = LEFT, fill = BOTH)

button2 = Button(frame2, text="About us", command = aboutMe, bg="#46a3ff", fg="white")
button2.pack(side = LEFT, fill = BOTH)

root.mainloop()
