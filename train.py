from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np 
import traceback 
# import mysql.connector 
# from tkinter import ttk



class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x790+0+0")
        self.root.title("Automatic Attendance Management System")
        root.iconbitmap('clgicon.ico')

        #Tittle of MainFrame
        title_lbl=Label(self.root,text='''TRAIN DATA SET''',font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1410,height=50)
        
        #Top_Image 
        img_top=Image.open(r"Project_Image\trainedImg.jpg")
        img_top=img_top.resize((1410,240),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1410,height=240)
        #Button 
        b1=Button(self.root,text="TRAIN DATA \n Click ",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=300,width=1410,height=100)
        #Down Image
        img_bottom=Image.open(r"Project_Image\bg.jpg")
        img_bottom=img_bottom.resize((1510,375),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=410,width=1510,height=300)

    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]#list complihenson
        
        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Convert into Grayscale image
            imageNp = np.array(img,'uint8')
        try :   
            id = int(os.path.split(image)[1].split('.')[1]) 
        except :
            print(traceback.format_exc())
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Photos Sample",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) # use for 90% performane increase to covert RMA


        #Train the classifir and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        # clf=cv2.face.createLBPHFaceRecognizer()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training  Data Sets have beeen completed!")




        






if __name__ ==  "__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()        