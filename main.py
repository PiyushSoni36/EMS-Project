from cProfile import label
from py_compile import main
from re import search
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x800+0+0")
        self.root.title("Anjani and Company")



        lbl_title=Label(self.root,font=('times new roman',40,'bold'),text='Anjani and Company ',fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1300,height=50)


        #logo
        img_logo=Image.open('Images/top1.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=365,y=0,width=50,height=50)

        #Image_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='red')
        img_frame.place(x=0,y=50,width=1300,height=160)



        #Main_frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='red')
        main_frame.place(x=10,y=240,width=1300,height=500)


        #Upper_Frame

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Customer Details',font=('times new roman',16,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1300,height=250)



        #Labels and Entries

        lbl_dep=Label(upper_frame,text='Department',font=('arial',13,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)


        combo_dep=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select department','Village','City', 'metro city', 'town', 'outsider')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, sticky=W,padx=2,pady=10)

        #Name

        lbl_Name=Label(upper_frame,text='Customer Name',font=('arial',13,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        text_name=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_name.grid(row=1,column=1,padx=2,pady=7,sticky=W)


        #Phone_Number
        lbl_Phone=Label(upper_frame,text='Phone Number',font=('arial',13,'bold'),bg='white')
        lbl_Phone.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        text_name=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_name.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #Email

        lbl_Email=Label(upper_frame,text='Email',font=('arial',13,'bold'),bg='white')
        lbl_Email.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        text_name=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_name.grid(row=3,column=1,padx=2,pady=7,sticky=W)


        #Address

        lbl_Address=Label(upper_frame,text='Address',font=('arial',13,'bold'),bg='white')
        lbl_Address.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        text_address=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_address.grid(row=4,column=1,padx=2,pady=7,sticky=W)


        #ID_Proof


        #lbl_Id=Label(upper_frame,text='ID Proof',font=('arial',13,'bold'),bg='white')
        #lbl_Id.grid(row=0,column=2,padx=2,sticky=W)


        combo_dep=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select ID Proof','Aadhar','PAN', 'Driving License', 'Voter ID', 'NA')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=3, sticky=W,padx=20,pady=10)



        text_id=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_id.grid(row=0,column=4,padx=2,pady=7,sticky=W)


        #Gender

        #lbl_gen=Label(upper_frame,text='Gender',font=('arial',13,'bold'),bg='white')
        #lbl_gen.grid(row=1,column=3,padx=100,pady=7,sticky=W)


        gen_dep=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        gen_dep['value']=( 'Gender')
        gen_dep.current(0)
        gen_dep.grid(row=1, column=3, sticky=W,padx=20,pady=10)




        text_gen=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        text_gen.grid(row=1,column=4,padx=2,pady=7,sticky=W)


        #Cash Image

        imgCash=Image.open('Images/cash.png')
        imgCash=imgCash.resize((220,220),Image.ANTIALIAS)
        self.photoCash=ImageTk.PhotoImage(imgCash) 

        self.img_cash=Label(upper_frame,image=self.photoCash)
        self.img_cash.place(x=760,y=5,width=220,height=220)



        #Button Frame

        
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='darkblue')
        Button_frame.place(x=1000,y=5,width=250,height=210)

        #Buttons

        btn_add=Button(Button_frame,text="Add New",font=('arial',20,'bold'),width=18,fg='black',bg='black')
        btn_add.grid(row=0,column=0,padx=5,pady=5)

        btn_delete=Button(Button_frame,text="Delete",font=('arial',20,'bold'),width=18,fg='black',bg='black')
        btn_delete.grid(row=1,column=0,padx=5,pady=5)


        btn_update=Button(Button_frame,text="Update",font=('arial',20,'bold'),width=18,fg='black',bg='black')
        btn_update.grid(row=2,column=0,padx=5,pady=5)

        btn_clear=Button(Button_frame,text="Clear",font=('arial',20,'bold'),width=18,fg='black',bg='black')
        btn_clear.grid(row=3,column=0,padx=5,pady=5)

        btn_useless=Button(Button_frame,text="Clear",font=('arial',20,'bold'),width=18,fg='black',bg='black')
        btn_useless.grid(row=4,column=0,padx=5,pady=5)

        #Down_frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='pink',text='Customer Details History Table',font=('times new roman',11,'bold'),fg='black')
        down_frame.place(x=10,y=260,width=1300,height=250)


        #Search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='yellow',text='Search Employee information',font=('times new roman',11,'bold'),fg='black')
        search_frame.place(x=0,y=0,width=1200,height=60)

        search_by=Label(search_frame,font=('times new roman',15,'bold'),text='Search by', fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        com_txt_search=ttk.Combobox(search_frame,state='readonly',font=('times new roman',13,'bold'),width=18)
        com_txt_search['value']=("Select Option","Phone","id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        txt_search=ttk.Entry(search_frame,width=22,font=('times new roman',12,'bold'))
        txt_search.grid(row=0,column=2,padx=5,sticky=W)

        btn_search=Button(search_frame,text='Search',font=('times new roman',14,'bold'),width=15,bg='black',fg='blue' )
        btn_search.grid(row=0,column=3,padx=5,sticky=W)


        btn_showAll=Button(search_frame,text='Show All',font=('times new roman',14,'bold'),width=15,bg='black',fg='blue' )
        btn_showAll.grid(row=0,column=4,padx=5,sticky=W)


        









        #1st
        img1=Image.open('Images/Ajay1.jpeg')
        img1=img1.resize((400,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)


        #2nd
        img2=Image.open('Images/top1.png')
        img2=img2.resize((400,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=500,y=0,width=400,height=160)


        #3rd
        img3=Image.open('Images/Ajay3.png')
        img3=img3.resize((400,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=900,y=0,width=400,height=160)




if __name__ == '__main__':
    root=Tk()
    obj=Employee(root)
    root.mainloop()
