from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog
# from unicodedata import name
# import mysql.connector 
# import numpy as np 
# import cv2


myData=[]
class Student_Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x790+0+0")
        self.root.title("Automatic Attendance Management System")
        root.iconbitmap('clgicon.ico')

    #Variables
        # self.var_attendace_studentSNo=StringVar()
        self.var_attendace_studentName=StringVar()
        self.var_attendace_enrollNo=StringVar()
        self.var_attendace_dep=StringVar()
        self.var_attendace_date=StringVar()
        self.var_attendace_time=StringVar()
        self.var_attendace_attendance=StringVar()
        


    #First Image Upload
        img=Image.open(r"Project_Image\AuLeft.jpg")
        img=img.resize((500,190),Image.Resampling.LANCZOS)
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
        img2=Image.open(r"Project_Image\AuRight.jpg")
        img2=img2.resize((500,170),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=950,y=0,width=500,height=150)

    #background Image Upload
        img3=Image.open(r"Project_Image\bg.webp")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT STSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1430,height=50)

        # Real world time
        def time():
                string = strftime('%I:%M:%S %p  %d/%m/%Y')
                lbl.config(text = string)
                lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman',20,'bold'), bg='white',fg='darkblue')
        lbl.place(x=5,y=0,width=350,height=50)
        time()

    #main frame in student 
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=45,width=1320,height=520)

    #left label frame
        Left_lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",18,"bold"))
        Left_lframe.place(x=10,y=10,width=650,height=550)

        img_left=Image.open(r"Project_Image\rightpic.jpg")
        img_left=img_left.resize((640,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_lframe,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=650,height=100)

    #current attendace information
        current_attendace_frame=LabelFrame(Left_lframe ,bd=2,relief=RIDGE,text="Current Course information :",font=("times new roman",15,"bold"))
        current_attendace_frame.place(x=10,y=100 ,width=620,height=350)
    #Label & Entry 
    #student serial no
        # studentSNo_label=Label(current_attendace_frame,text="Student S.No. :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        # studentSNo_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
    # student s.no. entry
        # studentSNo_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_studentSNo,font=("times new roman",14,"bold"),width=13)
        # studentSNo_entry.grid(row=0,column=1,padx=2,pady=0,sticky=W)

#   # student Name label uncomment from here
    #     studentName_label=Label(current_attendace_frame,text="Student Name :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     studentName_label.grid(row=0,column=2,padx=2,pady=2,sticky=W)
    # #student name entry
    #     studentName_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_studentName,font=("times new roman",14,"bold"),width=13)
    #     studentName_entry.grid(row=0,column=3,padx=2,pady=2,sticky=W)


    # #student Enrollment numbber label
    #     enrollNo_label=Label(current_attendace_frame,text="Enrollment No. :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     enrollNo_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)
    # #student Enrollment numbber entry
    #     enrollNo_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_enrollNo,font=("times new roman",14,"bold"),width=13)
    #     enrollNo_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W) 


    # #Department
    #     dep_label=Label(current_attendace_frame,text="Department :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     dep_label.grid(row=1,column=2,padx=2,sticky=W)
    # #student department name entry
    #     dep_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_dep,font=("times new roman",14,"bold"),width=13)
    #     dep_label_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)


    # #Attendace Date label
    #     date_label=Label(current_attendace_frame,text="Date :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     date_label.grid(row=2,column=0,padx=2,sticky=W)
    # #Attendance date entry
    #     date_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_date,font=("times new roman",14,"bold"),width=13)
    #     date_label_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

    # #Attendace Time label
    #     date_label=Label(current_attendace_frame,text="Time :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     date_label.grid(row=2,column=2,padx=2,sticky=W)
    # #Attendance time entry
    #     date_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_time,font=("times new roman",14,"bold"),width=13)
    #     date_label_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)


    # #Attendace status 
    #     attendace_label=Label(current_attendace_frame,text="Attendance Status",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
    #     attendace_label.grid(row=3,column=0,padx=2,pady=5,sticky=W)
    # #attendace status combobox
    #     self.attendance_status=ttk.Combobox(current_attendace_frame,textvariable=self.var_attendace_attendance,font=("times new roman",14,"bold"),state="readonly",width=11)
    #     self.attendance_status["values"]=("Select Status ","Present", "Absent")
    #     self.attendance_status.current(0)
    #     self.attendance_status.grid(row=3,column=1,padx=2, pady=5,sticky=W)


















        #student Name label
        studentName_label=Label(current_attendace_frame,text="Student Name :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        studentName_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
    #student name entry
        studentName_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_studentName,font=("times new roman",14,"bold"),width=13)
        studentName_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)


    #student Enrollment numbber label
        enrollNo_label=Label(current_attendace_frame,text="Enrollment No. :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        enrollNo_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)
    #student Enrollment numbber entry
        enrollNo_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_enrollNo,font=("times new roman",14,"bold"),width=13)
        enrollNo_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W) 


    #Department
        dep_label=Label(current_attendace_frame,text="Department :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        dep_label.grid(row=1,column=0,padx=2,sticky=W)
    #student department name entry
        dep_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_dep,font=("times new roman",14,"bold"),width=13)
        dep_label_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)


    #Attendace Date label
        time_label=Label(current_attendace_frame,text="Time :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        time_label.grid(row=1,column=2,padx=2,sticky=W)
    #Attendance date entry
        time_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_date,font=("times new roman",14,"bold"),width=13)
        time_label_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

    #Attendace Time label
        date_label=Label(current_attendace_frame,text="Date :",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        date_label.grid(row=2,column=0,padx=2,sticky=W)
    #Attendance time entry
        date_label_entry=ttk.Entry(current_attendace_frame,textvariable=self.var_attendace_time,font=("times new roman",14,"bold"),width=13)
        date_label_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)


    #Attendace status 
        attendace_label=Label(current_attendace_frame,text="Attendance Status",font=("times new roman",14,"bold"),bg="white",fg="darkgreen")
        attendace_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)
    #attendace status combobox
        self.attendance_status=ttk.Combobox(current_attendace_frame,textvariable=self.var_attendace_attendance,font=("times new roman",14,"bold"),state="readonly",width=11)
        self.attendance_status["values"]=("Select Status ","Present", "Absent")
        self.attendance_status.current(0)
        self.attendance_status.grid(row=2,column=3,padx=2, pady=5,sticky=W)


#   #Button frame
        btn_frame=Frame(current_attendace_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=620,height=80)

        import_csv_btn=Button(btn_frame,text="IMPORT CSV",command=self.importCsv,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        import_csv_btn.grid(row=0,column=0)

        export_csv_btn=Button(btn_frame,text="EXPORT CVS",command=self.exportCsv,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        export_csv_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="UPDATE",width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_date,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



    #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=670,y=10,width=640,height=500)
    #table frame ==========
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=630,height=470)
    #Scroll bar =======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # self.AttendanceReportTable=ttk.Treeview(table_frame,column=("studentSNo","studentName","enrollNo","dep","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("studentName","enrollNo","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("studentSNo",text="Student S.No.")
        self.AttendanceReportTable.heading("studentName",text="Student Name")
        self.AttendanceReportTable.heading("enrollNo",text="Enrollment No.")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"


        # self.AttendanceReportTable.column("studentSNo",width=100)
        self.AttendanceReportTable.column("studentName",width=100)
        self.AttendanceReportTable.column("enrollNo",width=100)
        self.AttendanceReportTable.column("dep",width=150)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ===========Fatch Data================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #Import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("NO DATA","No data has been found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_csv_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_csv_write.writerow(i)
                messagebox.showinfo("DATA EXPORT","Your data has been exported to" +os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        # self.var_attendace_studentSNo.set(rows[0])
        # self.var_attendace_studentName.set(rows[1])
        # self.var_attendace_enrollNo.set(rows[2])
        # self.var_attendace_dep.set(rows[3])
        # self.var_attendace_date.set(rows[4])
        # self.var_attendace_time.set(rows[5])
        # self.var_attendace_attendance.set(rows[6])

        self.var_attendace_studentName.set(rows[0])
        self.var_attendace_enrollNo.set(rows[1])
        self.var_attendace_dep.set(rows[2])
        self.var_attendace_date.set(rows[3])
        self.var_attendace_time.set(rows[4])
        self.var_attendace_attendance.set(rows[5])


    def reset_date(self):
        # self.var_attendace_studentSNo.set("")
        self.var_attendace_studentName.set("")
        self.var_attendace_enrollNo.set("")
        self.var_attendace_dep.set("")
        self.var_attendace_date.set("")
        self.var_attendace_time.set("")
        self.var_attendace_attendance.set("")




if __name__ ==  "__main__":
    root=Tk()
    obj=Student_Attendance(root)
    root.mainloop()          