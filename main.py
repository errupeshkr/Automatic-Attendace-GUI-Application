from tkinter import*
import tkinter
from PIL import Image,ImageTk
import os
# from student import Student
# from train import Train_Data
# from face_recogniton import Face_Recoginition
# from student_attendance import Student_Attendance
# from developer import Developer
from time import strftime
import datetime as dt 


# import tkinter as tk
# from tkinter import ttk
# from std_try import Student
# from pyclbr import Function
# from datetime import datetime
# from logging import root



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x700+0+0")
        self.root.title("Automatic Attendance Management System")
        root.iconbitmap('clgicon.ico')
        # root.resizable(1,1)

    #First Image Upload
        img=Image.open(r"Project_Image\sisrb.jpeg")
        img=img.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150) 

    #Second1 Image Upload
        img1=Image.open(r"Project_Image\trainedImg.jpg")
        img1=img1.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=490,y=0,width=500,height=150) 


     #Third Image Upload
        img2=Image.open(r"Project_Image\rgpv.jpg")
        img2=img2.resize((500,170),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=950,y=0,width=500,height=150)


     #background Image Upload
        img3=Image.open(r"Project_Image\bg.webp")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1530,height=710)

    #Automatic Attendance Management System Using Face Detecton 
        title_lbl=Label(bg_img,text="Automatic Attendance Management System Using Face Recognition ",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=50)

        date = dt.datetime.now()
        label = Label(root, text=f"{date:%A}", font=('times new roman',18,'bold'), bg='white',fg='darkblue')
        label.place(x=1230,y=172,width=115,height=50)
# Real world time %d for 24H %I for 12H
        def time():
                string = strftime('%I:%M:%S %p  %d/%m/%Y')
                lbl.config(text = string)
                lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman',18,'bold'), bg='white',fg='darkblue')
        lbl.place(x=5,y=0,width=250,height=50)
        time()


        

#Student button1
        img4=Image.open(r"Project_Image\studet.jpeg")
        img4=img4.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=180,y=120,width=180,height=120)
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=180,y=240,width=180,height=40)
#gsdfgh
#Face Recognition button2 
        img5=Image.open(r"Project_Image\face.jpeg")
        img5=img5.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command = self.Face_Data)
        b1.place(x=480,y=120,width=180,height=120)
        b1=Button(bg_img,text="Face Recognition",cursor="hand2",command = self.Face_Data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=480,y=240,width=180,height=40)

    #Attendance button3 
        img6=Image.open(r"Project_Image\attendance.jpeg")
        img6=img6.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendace)
        b1.place(x=780,y=120,width=180,height=120)
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendace,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=780,y=240,width=180,height=40)

    #Help Desk button4 
        img7=Image.open(r"Project_Image\helpdesk.jpeg")
        img7=img7.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Developer)
        b1.place(x=1080,y=120,width=180,height=120)
        b1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1080,y=240,width=180,height=40)



    #Train Data/Face button5
        img8=Image.open(r"Project_Image\train.jpeg")
        img8=img8.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.Train_Student_Data)
        b1.place(x=180,y=320,width=180,height=120)
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.Train_Student_Data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=180,y=440,width=180,height=40)

#Photos button6 
        img9=Image.open(r"Project_Image\photo.jpeg")
        img9=img9.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=480,y=320,width=180,height=120)
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=480,y=440,width=180,height=40)

#Developer button7 
        img10=Image.open(r"Project_Image\developer.jpeg")
        img10=img10.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer)
        b1.place(x=780,y=320,width=180,height=120)
        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=780,y=440,width=180,height=40)

# Exit button8
        img11=Image.open(r"Project_Image\exit.jpg")
        img11=img11.resize((180,120),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Win_Exit)
        b1.place(x=1080,y=320,width=180,height=120)
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.Win_Exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1080,y=440,width=180,height=40)



    def open_img(sslef):
        os.startfile("Data")


        # FunctionBUTTONS for student imagge and tittle
    # def student_details(self):
    #     self.new_window=Toplevel(self.root)
    #     self.rupesh=Student(self.new_window)

    # def Train_Student_Data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.rupesh=Train_Data(self.new_window)       

    # def Face_Data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.rupesh=Face_Recoginition(self.new_window)

    # def Attendace(self):
    #     self.new_window=Toplevel(self.root)
    #     self.rupesh=Student_Attendance(self.new_window)

    # def Developer(self):
    #     self.new_window=Toplevel(self.root)
    #     self.rupesh=Developer(self.new_window)


    def Win_Exit(self):
        self.Win_Exit=tkinter.messagebox.askyesno("Face Recognition", "Do you want to exit window page",parent=self.root)
        if self.Win_Exit > 0:
                self.root.destroy()
        else:
                return

if __name__ ==  "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()