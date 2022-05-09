from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import tkinter as tk

class multiple_chart:
    def __init__(self, master):
        self.root = master

        # [BOOK ISSUE] ===============================================================
        self.chart_button = Button(self.root,
                                       text="CHART",
                                       font=("tahoma", 15),
                                       borderwidth=0,
                                       fg="#C5C5C5",
                                       background="#262626",
                                       activeforeground="#C5C5C5",
                                       activebackground="#262626",
                                       command=self.openchart)
        self.chart_button.place(x=20,
                                    y=480)

    def openchart(self):
        Is = ChartWindow()





class ChartWindow:
    def __init__(self):
        self.root =Toplevel()
        self.root.title(" MULTIPLE CHARTS | LIBRARY MANAGEMENT SYSTEM")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.root.geometry("{w}x{h}+255+155".format(w=round(self.width * 0.83308),
                                                    h=round(self.height * 0.81771)))

        self.root.overrideredirect(1)
        self.root.resizable(False, False)

        data1 = {'Book Name': ['Python', 'Javascript', 'Flutter', 'MongDB', 'Angular'],
                 ' Quantity Borrow': [11, 12, 8, 9, 15]
                 }
        df1 = DataFrame(data1, columns=['Book Name', ' Quantity Borrow'])

        data2 = {'Month': ['May', 'January', 'March', 'December/2021'],
                 'Rate (%)': [17.0, 15.5, 13.2, 14.5]
                 }
        df2 = DataFrame(data2, columns=['Month', 'Rate (%)'])

        figure1 = plt.Figure(figsize=(9,10), dpi=70)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1,self.root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['Book Name', ' Quantity Borrow']].groupby('Book Name').sum()
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=10,color='green')
        ax1.set_title('Book Name &  The Most Borrowed Books in April, 2022',fontsize=19)

        figure2 = plt.Figure(figsize=(9, 10), dpi=70)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2,self.root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Month', 'Rate (%)']].groupby('Month').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=11)
        ax2.set_title('Percentage Of Monthly Borrowed in Library ,2022',fontsize=20)



# root.mainloop()