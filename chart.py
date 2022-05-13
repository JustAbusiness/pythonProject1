import mysql.connector
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
FigureCanvasTkAgg,
NavigationToolbar2Tk
)


class chart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CHART")

        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="admin")
        mycursor = mydb.cursor()

        # Fecthing Data From mysql to my python progame
        mycursor.execute("select name, marks from student")
        result = mycursor.fetchall

        Names = []
        Marks = []

        for i in mycursor:
            Names.append(i[0])
            Marks.append(int(i[1]))

        data = dict(zip(Names, Marks))
        print(data)
        print("Name of Students = ", Names)
        print("Marks of Students = ", Marks)


        # prepare data
        languages = data.keys()
        popularity = data.values()



        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)



        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)



        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)



        # create axes
        axes = figure.add_subplot()



        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')



        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




if __name__ == '__main__':
    app = chart()
    app.mainloop()
# window = Tk()
# window.title("WHORE")
# window.geometry("600x500")
#
# # Visulizing Data using Matplotlib
# plt.bar(Names, Marks)
# plt.ylim(0, 5)
# plt.xlabel("Name of Students")
# plt.ylabel("Marks of Students")
# plt.title("Student's Information")
# plt.show()
#
#
# window.mainloop()
