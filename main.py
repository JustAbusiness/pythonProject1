from tkinter import *
from tkinter import messagebox as mb,ttk
from PIL import ImageTk, Image
import mysql.connector as mc
import Delete



class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("   LIBRARY MANAGEMENT SYSTEM")
        self.window.geometry("1300x600+100+50")
        self.window.resizable(False,False)              #Size window cannot change


    # BACK GROUND OF LOGIN FROM
        self.bg=PhotoImage(file='images/Background.png')
        self.bg_image=Label(self.window, image=self.bg).place(x=1, y=1,relwidth=1, relheight=1)



    # LOGIN FRAME OF LOGIN
        Frame_Login = Frame(self.window, bg="white")
        Frame_Login.place(x=500, y=80, width=500, height=430)

    # ICON USER ADMIN
        self.sign_in_image = Image.open('images/profile.png')
        photo= ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_label = Label(Frame_Login,image=photo, bg='white')
        self.sign_in_label.image = photo
        self.sign_in_label.place(x= 370, y= 30, width= 100, height=100)



    # TITLE OF LOGN FORM
        title = Label(Frame_Login, text='Login Here', font=('Calibri', 35, 'bold'), fg='#48e84b', bg='white').place(x=90,y=18)
        title2 = Label(Frame_Login, text='Members Login Area', font=('Goudy old style', 20, 'bold'), fg='#1d1d1d', bg='white').place(
            x=90, y=100)

    # USERNAME
        user_name=Label(Frame_Login, text='Username', font=('Goudy old style', 15, 'bold'), fg='grey', bg='white').place(x=90,y=145)
        self.username = Entry(Frame_Login, font=('Goudy old style', 15), bg='#E7E6E6')
        self.username.place(x=90, y=180, width=340, height=40)

    # PASSWORD
        password = Label(Frame_Login, text='Password', font=('Goudy old style', 15, 'bold'), fg='grey',
                          bg='white').place(x=90, y=230)
        self.password = Entry(Frame_Login, font=('Goudy old style', 15), bg='#E7E6E6',show="*")
        self.password.place(x=90, y=265, width=340, height=40)


    #BUTTON
        # forget = Button(Frame_Login, text=' Forget password ?',command=self.forgot_password_window,cursor='hand2', font=('Goudy old style', 12), fg='#6162FF',
        #                   bg='white', bd=0).place(x=90, y=310)
        submit =Button(Frame_Login,command=self.check_function,cursor="hand2", text=' Login', font=('Goudy old style', 15), bg='#48e84b',
                          fg='white', bd=0, activebackground='#0b610c', activeforeground='white').place(x=90, y=330, width=180, height=40)

    # LOGIN FUNCTION
    def check_function(self):
        try:
            mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='admin'
            )

            mycursor = mydb.cursor()
            sql = "select from admin_member where Username='"+self.username.get()+"' and Password='"+self.password.get()+"'"
            mycursor.execute(sql)
            res=mycursor.fetchone()
            print(res)
            if(res==None):
                mb.showerror('Error Login','Invalid Username and Password ! Please Try Again')
            else:
                win=Toplevel()
                window=Login(win)
        except:
            mb.showerror('Failed connection', 'please open your xampp sever')

        # if self.username.get()==""  or self.password.get()=="":
        #
        #     mb.showerror("Error", "All field are required", parent=self.window)
        # else:
        #     try:
        #         con = pymysql.connect(host="localhost", user="root", password="phamngochuy2703", database="admin")
        #         cur = con.cursor()
        #         cur.execute("select * from admin_member where Username=%s and Password=%s",(self.username.get(),self.password.get()))
        #         row = cur.fecthone()
        #         if row == None:
        #              mb.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.window)
        #
        #         else:
        #             mb.showinfo("Success", "Welcome",parent=self.window)
        #             self.window.destroy()
        #             import Delete
        #         con.close()
        #     except Exception as es:
        #         mb.showerror("Error", f"Error Due to: {str(es)}", parent=self.window)

    #
    # # FORGOT PASSWORD FUNCTION
    # def reset(self):
    #     self.question.current(0)
    #     self.type_newpassword.delete(0,END)
    #     self.text_answer.delete(0,END)
    #     self.password.delete(0,END)
    #     self.username.delete(0,END)
    #
    #
    # def forgot_password(self):
    #     if self.question.get()=="Select"or self.text_answer.get()=="" or self.type_newpassword.get()=="":
    #         mb.showerror("Error","All field are required",parent=self.window2)
    #     else:
    #         try:
    #             con = pymysql.connect(host="localhost", user="root", password="phamngochuy2703", database="admin")
    #             cur = con.cursor()
    #             cur.execute("select *  from admin_member where Username=%s and question=%s and answer=%s", (self.username.get(),self.question.get(),self.text_answer.get()))
    #             row = cur.fecthone()
    #             if row == None:
    #                 mb.showerror("Error", "Please Select the Correct Security Question / Enter Answer",parent=self.window)
    #             else:
    #                 cur.execute("update admin_member set Password=%s where Username=%s",(self.type_newpassword.get(),self.username.get()))
    #                 con.commit()
    #                 con.close()
    #                 mb.showinfo("Success","your password has been reset, Please login with new password", parent=self.window2)
    #                 self.reset()
    #                 self.window2.destroy()
    #         except Exception as es:
    #             mb.showerror("Error", f"Error Due to: {str(es)}", parent=self.window)
    #
    # def forgot_password_window(self):                      # NOTICE: Request valid username to reset password
    #     if self.username.get()== "":
    #         mb.showerror("Error",'Please enter your valid username to reset your password',parent=self.window)
    #     else:
    #         try:
    #             con=pymysql.connect(host="localhost",user="root",password="phamngochuy2703",database="admin")
    #             cur=con.cursor()
    #             cur.execute("SELECT * FROM admin_member WHERE Username=%s",self.username.get())
    #             row=cur.fecthone()
    #             if row==None:
    #                 mb.showerror("Error","Please enter the valid username to reset your password")
    #             else:
    #                 con.close()
    #                 self.window2=Toplevel()
    #                 self.window2.title("Library Management System")
    #                 self.window2.geometry("500x400+600+160")
    #                 self.window2.resizable(False, False)
    #                 self.window2.focus_force()             # Cannot change the size table
    #                 self.window2.config(bg='white')
    #
    #
    #                 t=Label(self.window2,text='FORGET PASSWORD', font=('times new roman',20,'bold'),bg='white',fg='#48e84b').place(x=0,y=10,relwidth=1)
    #
    #     # -------------FORGOT PASSWORD LIST------------------------
    #                 question=Label(self.window2,text='Security Questions',font=('Goudy old style',15,'bold'),bg="white",fg='red').place(x=100,y=80)
    #
    #                 self.question=ttk.Combobox(self.window2,font=('times new roman',13),state='readonly',justify=CENTER)
    #                 self.question['values']=('Select','Your First Pet Name','Your Career Future','Your Best Food')
    #                 self.question.place(x=100,y=110,width=300)
    #                 self.question.current(0)
    #
    #                 answer=Label(self.window2,text='Answer', font=('Goudy old style',15,'bold'),bg='white',fg='gray').place(x=100,y=170)
    #                 self.text_answer=Entry(self.window2,font=('times new roman',15),bg='#E7E6E6')
    #                 self.text_answer.place(x=100,y=200,width=300)
    #
    #                 new_password = Label(self.window2, text='Create New Password', font=('Goudy old style', 15, 'bold'), bg='white', fg='gray').place(x=100, y=260)
    #                 self.type_newpassword = Entry(self.window2, font=('times new roman', 15), bg='#E7E6E6',show="*")
    #                 self.type_newpassword.place(x=100, y=290, width=300)
    #
    #
    #                 btn_change_newpassword=Button(self.window2,text='Resest Password',command=self.forgot_password, font=('Goudy old style', 15),bg='#48e84b',fg='white', bd=0, activebackground='#0b610c', activeforeground='white',cursor='hand2').place(x=155,y=350,width=180,height=40)
    #                 photo = PhotoImage(file='images/library (1).png')  # Set Icon
    #                 self.window2.iconphoto(False, photo)
    #
    #         except Exception as es:
    #             mb.showerror("Error",f"Error Due to: {str(es)}",parent=self.window)


window = Tk()
obj = Login(window)
photo = PhotoImage(file='images/library (1).png')       # Set Icon
window.iconphoto(False, photo)
window.mainloop()

