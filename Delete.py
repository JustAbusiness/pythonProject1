from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



def deleteBook():


    # Over all window =========================================================================================
    deletebook_window = Tk()
    deletebook_window.title("Library Management System")
    deletebook_window.geometry("550x630")
    deletebook_window.config(background="white")
    deletebook_window.resizable(False, False)

    # Add book background ==========================================================================================

    image = Image.open("images/Background.png")
    deletebook_bg_pic = image.resize((600, 650))
    deletebook_bg_img = ImageTk.PhotoImage(deletebook_bg_pic)

    deletebook_bg = Label(deletebook_window,
                       image=deletebook_bg_img,
                       bd=0)
    deletebook_bg.place(x=-25,
                     y=0)

    # Add a leabel to heading Frame

    headingFrame1 = Frame(deletebook_window, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)


    headingLabel = Label(headingFrame1, text="Delete Book", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    # Add a label frame to canvas to give a lebel insite it to delete book
    LabelFrame = Frame(deletebook_window, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)


    # Take a book ID to delete
    book_id= Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    book_id.place(relx=0.05, rely=0.5)

    bookInfo = Entry(LabelFrame)
    bookInfo.place(relx=0.3, rely=0.5, relwidth=0.62)


    # submit button
    submitBtn = Button(deletebook_window, text="Submit", bg="lightblue", fg="black", command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(deletebook_window, text="Quit", bg="lightblue", fg="black", command=deletebook_window.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


    deletebook_window.mainloop()

