from tkinter import *
import smtplib
from PIL import ImageTk, Image


class emai_sending:
    def __init__(self, master):
        self.root = master

        # [BOOK ISSUE] ===============================================================
        self.email_button = Button(self.root,
                                       text="EMAIL",
                                       font=("tahoma", 15),
                                       borderwidth=0,
                                       fg="#C5C5C5",
                                       background="#262626",
                                       activeforeground="#C5C5C5",
                                       activebackground="#262626",
                                       command=self.openemail)
        self.email_button.place(x=20,
                                    y=400)

    def openemail(self):
        Is = EmailWindow()

class EmailWindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('EMAIL SENDING')
        # self.root.geometry('1138x580+220+165')
        self.root.config(bg='black')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.root.geometry("{w}x{h}+255+155".format(w=round(self.width * 0.83308),
                                                      h=round(self.height * 0.81771)))

        self.root.overrideredirect(1)
        self.root.resizable(False, False)


        self.Frame_Login = Frame(self.root, bg="#48e84b")
        self.Frame_Login.place(x=79, y=50, width=1130, height=550)



        self.label = Label(self.Frame_Login, text='Email Sending',width=20,font=('Goudy old style',40,'bold'))
        self.label.place(x=240, y=1)


        radio = IntVar()

        self.label_to =Label(self.Frame_Login,text='Send To:',bg='#48e84b',fg='black',font=('Helvetica',15,'bold'))
        self.label_to.place(x=70,y=105)

        self.entry_to = Entry(self.Frame_Login,width=25,font=('calibri',14,'bold'),bd=2)
        self.entry_to.place(x=170,y=105)

        self.label_subject =Label(self.Frame_Login,text='Subject:',bg='#48e84b',font=('Helvetica',15,'bold'))
        self.label_subject.place(x=570,y=105)

        self.entry_subject = Entry(self.Frame_Login,font=('calibri',14,'bold italic'),bd=2,width=25)
        self.entry_subject.place(x=665,y=105)

        self.label_message =Label(self.Frame_Login,text='Message:',bg='#48e84b',font=('Helvetica',15,'bold'))
        self.label_message.place(x=70,y=175)

        self.entry_message = Text(self.Frame_Login,height=10,width=68,font=('Helvetica',15,'bold'))
        self.entry_message.place(x=170,y=210)

        self.btn = Button(self.Frame_Login, command=self.MailSending, text='Send Email', bg='white', width='20', cursor='hand2',
                     font=('Goudy old style', 20, 'italic'))
        self.btn.place(x=390, y=470)


    def MailSending(self):

        to= StringVar()
        sub=StringVar()
        msg= StringVar()

        to= self.entry_to.get()
        sub=self.entry_subject.get()
        msg=self.entry_message.get(1.0,'end-1c')
        message= 'Subject:{}\n\n{}'.format(sub,msg,to)


        sender='huysanti654321@gmail.com'
        password= 'hoang9a8'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,password)

        server.sendmail(sender,to,message)
        print("Mail Sent")

        # btn = Button(self.Frame_Login,command=self.,text='Send Email',bg='white',width='20',cursor='hand2',font=('Goudy old style',20,'italic'))
        # btn.place(x=390, y=470)

# photo = PhotoImage(file='images/library (1).png')       # Set Icon
# root.iconphoto(False, photo)
# root.mainloop()
# root = Tk()
# obj = emai_sending(root)
# root.mainloop()