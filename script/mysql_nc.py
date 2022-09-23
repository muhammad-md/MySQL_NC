from multiprocessing import connection
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from getpass import getpass
from mysql.connector import connect, Error
from pymysql import *

#setting the window
window = Tk()
window.title("MYSQL NO_CODE")
window.state("zoomed")
window.configure(width=600, height=700)
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
fontStyle = tkFont.Font(family="Candara", size=14)
fontStyle1 = tkFont.Font(family="Candara", size=17)

#list to save connection details
connection_list = []

entries = []
countlist = []
columnslis = []

class save_connection:
    def __init__(self, master):
        self.master = master
        
        self.label1= Label(self.master, text="HOST", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="USER", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.35, anchor = CENTER)
        self.label3= Label(self.master, text="PASSWORD", font = fontStyle)
        self.label3.place(relx = 0.22, rely = 0.40, anchor = CENTER)

        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.5, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        self.entry3 = Entry(self.master)
        self.entry3.place(relx = 0.5, rely = 0.40, anchor = CENTER)
        

        self.btn1 = tk.Button(self.master, text ="NEXT", font = fontStyle, command = self.clearpage1)
        self.btn1.place(relx = 0.5, rely = 0.50, anchor = CENTER)

    #functions to clear the page to view the next page elements
    def clearpage1(self):
        host = self.entry1.get()
        user = self.entry2.get()
        password = self.entry3.get()
        connection_list.append(host)
        connection_list.append(user)
        connection_list.append(password)
        print(connection_list)
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.entry3.destroy()
        self.btn1.destroy()
        self.another = mainwindow(self.master)

class mainwindow:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="CREATE/DROP DATABSE", font = fontStyle1, command = self.clearpage1)
        self.btn1.place(relx = 0.5, rely = 0.30, anchor = CENTER)
        self.btn2 = tk.Button(self.master, text ="CREATE/DROP TABLE IN A DATABASE", font = fontStyle1, command = self.clearpage2)
        self.btn2.place(relx = 0.5, rely = 0.40, anchor = CENTER)
        self.btn3 = tk.Button(self.master, text ="ADD/DROP COLUMN IN A TABLE", font = fontStyle1, command = self.clearpage3)
        self.btn3.place(relx = 0.5, rely = 0.50, anchor = CENTER)
        self.btn4 = tk.Button(self.master, text ="INSERT/DELETE INPUTS IN A TABLE", font = fontStyle1, command = self.clearpage4)
        self.btn4.place(relx = 0.5, rely = 0.60, anchor = CENTER)


    #functions to clear the page to view the next page elements
    def clearpage1(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = cd_database(self.master)
    def clearpage2(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = cd_table(self.master)
    def clearpage3(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = alter(self.master)
    def clearpage4(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = inputs(self.master)

class cd_database:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle, command = self.load_back)
        self.btn1.place(relx = 0.90, rely = 0.84, anchor = CENTER)

        self.label1= Label(self.master, text="CREATE DATABASE ", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="DROP DATABASE ", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.60, anchor = CENTER)

        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.5, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.5, rely = 0.60, anchor = CENTER)

        def create():
            entry1 = self.entry1.get()
            connection = connect(host="%s" %(connection_list[0]),user="%s" %(connection_list[1]),password="%s" %(connection_list[2]))
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE %s" %(entry1))
        def drop():
            entry2 = self.entry2.get()
            connection = connect(host="%s" %(connection_list[0]),user="%s" %(connection_list[1]),password="%s" %(connection_list[2]))
            cursor = connection.cursor()
            cursor.execute("DROP DATABASE IF EXISTS `%s`" %(entry2))
        self.btn2 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create)
        self.btn2.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        self.btn3 = tk.Button(self.master, text ="DROP", font = fontStyle, command = drop)
        self.btn3.place(relx = 0.5, rely = 0.65, anchor = CENTER)

    #function to clear the current page to view the previous page elements
    def load_back(self):
        self.entry1.destroy()
        self.entry2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.another = mainwindow(self.master)


class cd_table:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle, command = self.load_backk)
        self.btn1.place(relx = 0.90, rely = 0.90, anchor = CENTER)

        self.btn2 = tk.Button(self.master, text ="CREATE TABLE", font = fontStyle, command = self.cols)
        self.btn2.place(relx = 0.6, rely = 0.40, anchor = CENTER)
        self.btn3 = tk.Button(self.master, text ="DROP TABLE", font = fontStyle, command = self.droptab)
        self.btn3.place(relx = 0.6, rely = 0.47, anchor = CENTER)
       
        
        self.label1= Label(self.master, text="ENTER DATABASE NAME", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="ENTER TABLE NAME", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.35, anchor = CENTER)
        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.6, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.6, rely = 0.35, anchor = CENTER)

    def droptab(self):
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        connection = connect(host="%s" %(connection_list[0]), database="%s" %(entry1), user="%s" %(connection_list[1]), password="%s" %(connection_list[2]))
        cursor0 = connection.cursor()

        cursor0.execute("DROP TABLE %s" %(entry2))
    
    
    def cols(self):
        self.label1.destroy()
        self.label2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        self.btn2.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        connection = connect(host="%s" %(connection_list[0]), database="%s" %(entry1), user="%s" %(connection_list[1]), password="%s" %(connection_list[2]))
        cursor0 = connection.cursor()
        
        self.label11= Label(self.master, text="COLUMN_ONE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label11.place(relx = 0.10, rely = 0.05, anchor = CENTER)
        self.label22= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
        self.label22.place(relx = 0.10, rely = 0.15, anchor = CENTER)
        self.label33= Label(self.master, text="COLUMN_THREE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label33.place(relx = 0.10, rely = 0.25, anchor = CENTER)
        self.label44= Label(self.master, text="COLUMN_FOUR NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label44.place(relx = 0.10, rely = 0.35, anchor = CENTER)
        self.label55= Label(self.master, text="COLUMN_FIVE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label55.place(relx = 0.10, rely = 0.45, anchor = CENTER)
        self.label66= Label(self.master, text="COLUMN_SIX NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label66.place(relx = 0.10, rely = 0.55, anchor = CENTER)
        self.label77= Label(self.master, text="COLUMN_SEVEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label77.place(relx = 0.10, rely = 0.65, anchor = CENTER)
        self.label88= Label(self.master, text="COLUMN_EIGHT NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label88.place(relx = 0.10, rely = 0.75, anchor = CENTER)
        self.label99= Label(self.master, text="COLUMN_NINE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label99.place(relx = 0.10, rely = 0.85, anchor = CENTER)
        self.label10= Label(self.master, text="COLUMN_TEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label10.place(relx = 0.10, rely = 0.95, anchor = CENTER)
        self.label111= Label(self.master, text="COLUMN_ELEVEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label111.place(relx = 0.60, rely = 0.05, anchor = CENTER)
        self.label222= Label(self.master, text="COLUMN_TWELVE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label222.place(relx = 0.60, rely = 0.15, anchor = CENTER)
        self.label333= Label(self.master, text="COLUMN_THIRTHEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label333.place(relx = 0.60, rely = 0.25, anchor = CENTER)
        self.label444= Label(self.master, text="COLUMN_FOURTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label444.place(relx = 0.60, rely = 0.35, anchor = CENTER)
        self.label555= Label(self.master, text="COLUMN_FIFTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label555.place(relx = 0.60, rely = 0.45, anchor = CENTER)
        self.label666= Label(self.master, text="COLUMN_SIXTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label666.place(relx = 0.60, rely = 0.55, anchor = CENTER)
        self.label777= Label(self.master, text="COLUMN_SEVENTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label777.place(relx = 0.60, rely = 0.65, anchor = CENTER)
        self.label888= Label(self.master, text="COLUMN_EIGHTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label888.place(relx = 0.60, rely = 0.75, anchor = CENTER)
        self.label999= Label(self.master, text="COLUMN_NINETEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label999.place(relx = 0.60, rely = 0.85, anchor = CENTER)
        self.label2000= Label(self.master, text="COLUMN_TWENTY NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label2000.place(relx = 0.60, rely = 0.95, anchor = CENTER)

        self.entry11 = Entry(self.master)
        self.entry11.place(relx = 0.25, rely = 0.05, anchor = CENTER)
        self.entry22 = Entry(self.master)
        self.entry22.place(relx = 0.25, rely = 0.15, anchor = CENTER)
        self.entry33 = Entry(self.master)
        self.entry33.place(relx = 0.25, rely = 0.25, anchor = CENTER)
        self.entry44 = Entry(self.master)
        self.entry44.place(relx = 0.25, rely = 0.35, anchor = CENTER)
        self.entry55 = Entry(self.master)
        self.entry55.place(relx = 0.25, rely = 0.45, anchor = CENTER)
        self.entry66 = Entry(self.master)
        self.entry66.place(relx = 0.25, rely = 0.55, anchor = CENTER)
        self.entry77 = Entry(self.master)
        self.entry77.place(relx = 0.25, rely = 0.65, anchor = CENTER)
        self.entry88 = Entry(self.master)
        self.entry88.place(relx = 0.25, rely = 0.75, anchor = CENTER)
        self.entry99 = Entry(self.master)
        self.entry99.place(relx = 0.25, rely = 0.85, anchor = CENTER)
        self.entry10 = Entry(self.master)
        self.entry10.place(relx = 0.25, rely = 0.95, anchor = CENTER)

        self.entry111 = Entry(self.master)
        self.entry111.place(relx = 0.75, rely = 0.05, anchor = CENTER)
        self.entry222 = Entry(self.master)
        self.entry222.place(relx = 0.75, rely = 0.15, anchor = CENTER)
        self.entry333 = Entry(self.master)
        self.entry333.place(relx = 0.75, rely = 0.25, anchor = CENTER)
        self.entry444 = Entry(self.master)
        self.entry444.place(relx = 0.75, rely = 0.35, anchor = CENTER)
        self.entry555 = Entry(self.master)
        self.entry555.place(relx = 0.75, rely = 0.45, anchor = CENTER)
        self.entry666 = Entry(self.master)
        self.entry666.place(relx = 0.75, rely = 0.55, anchor = CENTER)
        self.entry777 = Entry(self.master)
        self.entry777.place(relx = 0.75, rely = 0.65, anchor = CENTER)
        self.entry888 = Entry(self.master)
        self.entry888.place(relx = 0.75, rely = 0.75, anchor = CENTER)
        self.entry999 = Entry(self.master)
        self.entry999.place(relx = 0.75, rely = 0.85, anchor = CENTER)
        self.entry2000 = Entry(self.master)
        self.entry2000.place(relx = 0.75, rely = 0.95, anchor = CENTER)
            
        def createtables():
            entries.append(self.entry11.get())
            entries.append(self.entry22.get())
            entries.append(self.entry33.get())
            entries.append(self.entry44.get())
            entries.append(self.entry55.get())
            entries.append(self.entry66.get())
            entries.append(self.entry77.get())
            entries.append(self.entry88.get())
            entries.append(self.entry99.get())
            entries.append(self.entry10.get())
            entries.append(self.entry111.get())
            entries.append(self.entry222.get())
            entries.append(self.entry333.get())
            entries.append(self.entry444.get())
            entries.append(self.entry555.get())
            entries.append(self.entry666.get())
            entries.append(self.entry777.get())
            entries.append(self.entry888.get())
            entries.append(self.entry999.get())
            entries.append(self.entry2000.get())

            print(entries)

            count = 0
            for i in entries:
                if len(i)>0:
                    count = count + 1
                    countlist.append(count)
            print(countlist)
            count = max(countlist)
            
            if count == 1:
                cursor0.execute("CREATE TABLE %s (%s)" %(entry2, entries[0]))
            elif count == 2:
                cursor0.execute("CREATE TABLE %s (%s, %s)" %(entry2, entries[0], entries[1]))
            elif count == 3:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s)" %(entry2, entries[0], entries[1], entries[2]))
            elif count == 4:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3]))
            elif count == 5:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4]))
            elif count == 6:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5]))
            elif count == 7:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6]))
            elif count == 8:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7]))
            elif count == 9:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8]))
            elif count == 10:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9]))
            elif count == 11:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10]))
            elif count == 12:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11]))
            elif count == 13:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12]))
            elif count == 14:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13]))
            elif count == 15:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14]))
            elif count == 16:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15]))
            elif count == 17:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16]))
            elif count == 18:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17]))
            elif count == 19:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18]))
            elif count == 20:
                cursor0.execute("CREATE TABLE %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18], entries[19]))

        def load_back9():
            self.label11.destroy()
            self.label22.destroy()
            self.label33.destroy()
            self.label44.destroy()
            self.label55.destroy()
            self.label66.destroy()
            self.label77.destroy()
            self.label88.destroy()
            self.label99.destroy()
            self.label10.destroy()
            self.label111.destroy()
            self.label222.destroy()
            self.label333.destroy()
            self.label444.destroy()
            self.label555.destroy()
            self.label666.destroy()
            self.label777.destroy()
            self.label888.destroy()
            self.label999.destroy()
            self.label2000.destroy()
            self.entry11.destroy()
            self.entry22.destroy()
            self.entry33.destroy()
            self.entry44.destroy()
            self.entry55.destroy()
            self.entry66.destroy()
            self.entry77.destroy()
            self.entry88.destroy()
            self.entry99.destroy()
            self.entry10.destroy()
            self.entry111.destroy()
            self.entry222.destroy()
            self.entry333.destroy()
            self.entry444.destroy()
            self.entry555.destroy()
            self.entry666.destroy()
            self.entry777.destroy()
            self.entry888.destroy()
            self.entry999.destroy()
            self.entry2000.destroy()
            self.btn7.destroy()
            self.btn39.destroy()

            entries.clear()
            countlist.clear()
            self.another = mainwindow(self.master)
            
        self.btn7 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = createtables)
        self.btn7.place(relx = 0.9, rely = 0.80, anchor = CENTER)
        self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
        self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
            
        
    
    def load_backk(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.another = mainwindow(self.master)

class alter:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn1.place(relx = 0.90, rely = 0.84, anchor = CENTER)

        self.btn2 = tk.Button(self.master, text ="NEXT", font = fontStyle, command = self.cols)
        self.btn2.place(relx = 0.6, rely = 0.40, anchor = CENTER)

        self.label1= Label(self.master, text="ENTER DATABASE NAME", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="ENTER TABLE NAME", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.35, anchor = CENTER)
        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.6, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.6, rely = 0.35, anchor = CENTER)

    def cols(self):
        self.label1.destroy()
        self.label2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        self.entry1.destroy()
        self.entry2.destroy()
        connection = connect(host="%s" %(connection_list[0]), database="%s" %(entry1), user="%s" %(connection_list[1]), password="%s" %(connection_list[2]))
        cursor0 = connection.cursor()
        
        self.label11= Label(self.master, text="COLUMN_ONE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label11.place(relx = 0.10, rely = 0.05, anchor = CENTER)
        self.label22= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
        self.label22.place(relx = 0.10, rely = 0.15, anchor = CENTER)
        self.label33= Label(self.master, text="COLUMN_THREE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label33.place(relx = 0.10, rely = 0.25, anchor = CENTER)
        self.label44= Label(self.master, text="COLUMN_FOUR NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label44.place(relx = 0.10, rely = 0.35, anchor = CENTER)
        self.label55= Label(self.master, text="COLUMN_FIVE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label55.place(relx = 0.10, rely = 0.45, anchor = CENTER)
        self.label66= Label(self.master, text="COLUMN_SIX NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label66.place(relx = 0.10, rely = 0.55, anchor = CENTER)
        self.label77= Label(self.master, text="COLUMN_SEVEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label77.place(relx = 0.10, rely = 0.65, anchor = CENTER)
        self.label88= Label(self.master, text="COLUMN_EIGHT NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label88.place(relx = 0.10, rely = 0.75, anchor = CENTER)
        self.label99= Label(self.master, text="COLUMN_NINE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label99.place(relx = 0.10, rely = 0.85, anchor = CENTER)
        self.label10= Label(self.master, text="COLUMN_TEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label10.place(relx = 0.10, rely = 0.95, anchor = CENTER)
        self.label111= Label(self.master, text="COLUMN_ELEVEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label111.place(relx = 0.60, rely = 0.05, anchor = CENTER)
        self.label222= Label(self.master, text="COLUMN_TWELVE NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label222.place(relx = 0.60, rely = 0.15, anchor = CENTER)
        self.label333= Label(self.master, text="COLUMN_THIRTHEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label333.place(relx = 0.60, rely = 0.25, anchor = CENTER)
        self.label444= Label(self.master, text="COLUMN_FOURTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label444.place(relx = 0.60, rely = 0.35, anchor = CENTER)
        self.label555= Label(self.master, text="COLUMN_FIFTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label555.place(relx = 0.60, rely = 0.45, anchor = CENTER)
        self.label666= Label(self.master, text="COLUMN_SIXTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label666.place(relx = 0.60, rely = 0.55, anchor = CENTER)
        self.label777= Label(self.master, text="COLUMN_SEVENTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label777.place(relx = 0.60, rely = 0.65, anchor = CENTER)
        self.label888= Label(self.master, text="COLUMN_EIGHTEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label888.place(relx = 0.60, rely = 0.75, anchor = CENTER)
        self.label999= Label(self.master, text="COLUMN_NINETEEN NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label999.place(relx = 0.60, rely = 0.85, anchor = CENTER)
        self.label2000= Label(self.master, text="COLUMN_TWENTY NAME \n TYPE AND LENGTH", font = fontStyle)
        self.label2000.place(relx = 0.60, rely = 0.95, anchor = CENTER)

        self.entry11 = Entry(self.master)
        self.entry11.place(relx = 0.25, rely = 0.05, anchor = CENTER)
        self.entry22 = Entry(self.master)
        self.entry22.place(relx = 0.25, rely = 0.15, anchor = CENTER)
        self.entry33 = Entry(self.master)
        self.entry33.place(relx = 0.25, rely = 0.25, anchor = CENTER)
        self.entry44 = Entry(self.master)
        self.entry44.place(relx = 0.25, rely = 0.35, anchor = CENTER)
        self.entry55 = Entry(self.master)
        self.entry55.place(relx = 0.25, rely = 0.45, anchor = CENTER)
        self.entry66 = Entry(self.master)
        self.entry66.place(relx = 0.25, rely = 0.55, anchor = CENTER)
        self.entry77 = Entry(self.master)
        self.entry77.place(relx = 0.25, rely = 0.65, anchor = CENTER)
        self.entry88 = Entry(self.master)
        self.entry88.place(relx = 0.25, rely = 0.75, anchor = CENTER)
        self.entry99 = Entry(self.master)
        self.entry99.place(relx = 0.25, rely = 0.85, anchor = CENTER)
        self.entry10 = Entry(self.master)
        self.entry10.place(relx = 0.25, rely = 0.95, anchor = CENTER)

        self.entry111 = Entry(self.master)
        self.entry111.place(relx = 0.75, rely = 0.05, anchor = CENTER)
        self.entry222 = Entry(self.master)
        self.entry222.place(relx = 0.75, rely = 0.15, anchor = CENTER)
        self.entry333 = Entry(self.master)
        self.entry333.place(relx = 0.75, rely = 0.25, anchor = CENTER)
        self.entry444 = Entry(self.master)
        self.entry444.place(relx = 0.75, rely = 0.35, anchor = CENTER)
        self.entry555 = Entry(self.master)
        self.entry555.place(relx = 0.75, rely = 0.45, anchor = CENTER)
        self.entry666 = Entry(self.master)
        self.entry666.place(relx = 0.75, rely = 0.55, anchor = CENTER)
        self.entry777 = Entry(self.master)
        self.entry777.place(relx = 0.75, rely = 0.65, anchor = CENTER)
        self.entry888 = Entry(self.master)
        self.entry888.place(relx = 0.75, rely = 0.75, anchor = CENTER)
        self.entry999 = Entry(self.master)
        self.entry999.place(relx = 0.75, rely = 0.85, anchor = CENTER)
        self.entry2000 = Entry(self.master)
        self.entry2000.place(relx = 0.75, rely = 0.95, anchor = CENTER)

        def createcols():
            entries.append(self.entry11.get())
            entries.append(self.entry22.get())
            entries.append(self.entry33.get())
            entries.append(self.entry44.get())
            entries.append(self.entry55.get())
            entries.append(self.entry66.get())
            entries.append(self.entry77.get())
            entries.append(self.entry88.get())
            entries.append(self.entry99.get())
            entries.append(self.entry10.get())
            entries.append(self.entry111.get())
            entries.append(self.entry222.get())
            entries.append(self.entry333.get())
            entries.append(self.entry444.get())
            entries.append(self.entry555.get())
            entries.append(self.entry666.get())
            entries.append(self.entry777.get())
            entries.append(self.entry888.get())
            entries.append(self.entry999.get())
            entries.append(self.entry2000.get())

            print(entries)

            count = 0
            for i in entries:
                if len(i)>0:
                    count = count + 1
                    countlist.append(count)
            print(countlist)
            count = max(countlist)
            
            if count == 1:
                cursor0.execute("ALTER TABLE %s ADD (%s)" %(entry2, entries[0]))
            elif count == 2:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s)" %(entry2, entries[0], entries[1]))
            elif count == 3:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s)" %(entry2, entries[0], entries[1], entries[2]))
            elif count == 4:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3]))
            elif count == 5:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4]))
            elif count == 6:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5]))
            elif count == 7:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6]))
            elif count == 8:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7]))
            elif count == 9:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8]))
            elif count == 10:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9]))
            elif count == 11:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10]))
            elif count == 12:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11]))
            elif count == 13:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12]))
            elif count == 14:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13]))
            elif count == 15:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14]))
            elif count == 16:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15]))
            elif count == 17:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16]))
            elif count == 18:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17]))
            elif count == 19:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18]))
            elif count == 20:
                cursor0.execute("ALTER TABLE %s ADD (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18], entries[19]))

        def dropcols():
            entries.append(self.entry11.get())
            entries.append(self.entry22.get())
            entries.append(self.entry33.get())
            entries.append(self.entry44.get())
            entries.append(self.entry55.get())
            entries.append(self.entry66.get())
            entries.append(self.entry77.get())
            entries.append(self.entry88.get())
            entries.append(self.entry99.get())
            entries.append(self.entry10.get())
            entries.append(self.entry111.get())
            entries.append(self.entry222.get())
            entries.append(self.entry333.get())
            entries.append(self.entry444.get())
            entries.append(self.entry555.get())
            entries.append(self.entry666.get())
            entries.append(self.entry777.get())
            entries.append(self.entry888.get())
            entries.append(self.entry999.get())
            entries.append(self.entry2000.get())

            print(entries)

            count = 0
            for i in entries:
                if len(i)>0:
                    count = count + 1
                    countlist.append(count)
            print(countlist)
            count = max(countlist)
            
            if count == 1:
                cursor0.execute("ALTER TABLE %s DROP %s" %(entry2, entries[0]))
            elif count == 2:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s" %(entry2, entries[0], entries[1]))
            elif count == 3:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2]))
            elif count == 4:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3]))
            elif count == 5:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4]))
            elif count == 6:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5]))
            elif count == 7:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6]))
            elif count == 8:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7]))
            elif count == 9:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8]))
            elif count == 10:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9]))
            elif count == 11:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10]))
            elif count == 12:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11]))
            elif count == 13:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12]))
            elif count == 14:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13]))
            elif count == 15:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14]))
            elif count == 16:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15]))
            elif count == 17:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16]))
            elif count == 18:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17]))
            elif count == 19:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18]))
            elif count == 20:
                cursor0.execute("ALTER TABLE %s DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s, DROP %s" %(entry2, entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18], entries[19]))

        def load_back9():
            self.label11.destroy()
            self.label22.destroy()
            self.label33.destroy()
            self.label44.destroy()
            self.label55.destroy()
            self.label66.destroy()
            self.label77.destroy()
            self.label88.destroy()
            self.label99.destroy()
            self.label10.destroy()
            self.label111.destroy()
            self.label222.destroy()
            self.label333.destroy()
            self.label444.destroy()
            self.label555.destroy()
            self.label666.destroy()
            self.label777.destroy()
            self.label888.destroy()
            self.label999.destroy()
            self.label2000.destroy()
            self.entry11.destroy()
            self.entry22.destroy()
            self.entry33.destroy()
            self.entry44.destroy()
            self.entry55.destroy()
            self.entry66.destroy()
            self.entry77.destroy()
            self.entry88.destroy()
            self.entry99.destroy()
            self.entry10.destroy()
            self.entry111.destroy()
            self.entry222.destroy()
            self.entry333.destroy()
            self.entry444.destroy()
            self.entry555.destroy()
            self.entry666.destroy()
            self.entry777.destroy()
            self.entry888.destroy()
            self.entry999.destroy()
            self.entry2000.destroy()
            self.btn7.destroy()
            self.btn8.destroy()
            self.btn39.destroy()

            entries.clear()
            countlist.clear()
            self.another = mainwindow(self.master)
            
        self.btn7 = tk.Button(self.master, text ="CREATE COLUMN", font = fontStyle, command = createcols)
        self.btn7.place(relx = 0.9, rely = 0.70, anchor = CENTER)
        self.btn8 = tk.Button(self.master, text ="DROP COLUMN", font = fontStyle, command = dropcols)
        self.btn8.place(relx = 0.9, rely = 0.80, anchor = CENTER)
        self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
        self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)

    
    def load_back(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        #self.btn3.destroy()
        self.another = mainwindow(self.master)

class inputs:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn1.place(relx = 0.90, rely = 0.84, anchor = CENTER)
        self.btn2 = tk.Button(self.master, text ="NEXT", font = fontStyle1, command = self.cols)
        self.btn2.place(relx = 0.6, rely = 0.50, anchor = CENTER)

        self.label1= Label(self.master, text="ENTER DATABASE", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="ENTER TABLE_NAME", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.40, anchor = CENTER)

        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.6, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.6, rely = 0.40, anchor = CENTER)
        
#################################################################################################################################################################################
    def cols(self):
        self.label1.destroy()
        self.label2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        self.entry1.destroy()
        self.entry2.destroy()
        connection = connect(host="%s" %(connection_list[0]), database="%s" %(entry1), user="%s" %(connection_list[1]), password="%s" %(connection_list[2]))
        cursor0 = connection.cursor()
        
        self.label11= Label(self.master, text="COLUMN_ONE NAME \n VALUE", font = fontStyle)
        self.label11.place(relx = 0.10, rely = 0.05, anchor = CENTER)
        self.label22= Label(self.master, text="COLUMN_TWO TYPE \n VALUE", font = fontStyle)
        self.label22.place(relx = 0.10, rely = 0.15, anchor = CENTER)
        self.label33= Label(self.master, text="COLUMN_THREE NAME \n VALUE", font = fontStyle)
        self.label33.place(relx = 0.10, rely = 0.25, anchor = CENTER)
        self.label44= Label(self.master, text="COLUMN_FOUR NAME \n VALUE", font = fontStyle)
        self.label44.place(relx = 0.10, rely = 0.35, anchor = CENTER)
        self.label55= Label(self.master, text="COLUMN_FIVE NAME \n VALUE", font = fontStyle)
        self.label55.place(relx = 0.10, rely = 0.45, anchor = CENTER)
        self.label66= Label(self.master, text="COLUMN_SIX NAME \n VALUE", font = fontStyle)
        self.label66.place(relx = 0.10, rely = 0.55, anchor = CENTER)
        self.label77= Label(self.master, text="COLUMN_SEVEN NAME \n VALUE", font = fontStyle)
        self.label77.place(relx = 0.10, rely = 0.65, anchor = CENTER)
        self.label88= Label(self.master, text="COLUMN_EIGHT NAME \n VALUE", font = fontStyle)
        self.label88.place(relx = 0.10, rely = 0.75, anchor = CENTER)
        self.label99= Label(self.master, text="COLUMN_NINE NAME \n VALUE", font = fontStyle)
        self.label99.place(relx = 0.10, rely = 0.85, anchor = CENTER)
        self.label10= Label(self.master, text="COLUMN_TEN NAME \n VALUE", font = fontStyle)
        self.label10.place(relx = 0.10, rely = 0.95, anchor = CENTER)
        self.label111= Label(self.master, text="COLUMN_ELEVEN NAME \n VALUE", font = fontStyle)
        self.label111.place(relx = 0.60, rely = 0.05, anchor = CENTER)
        self.label222= Label(self.master, text="COLUMN_TWELVE NAME \n VALUE", font = fontStyle)
        self.label222.place(relx = 0.60, rely = 0.15, anchor = CENTER)
        self.label333= Label(self.master, text="COLUMN_THIRTHEEN NAME \n VALUE", font = fontStyle)
        self.label333.place(relx = 0.60, rely = 0.25, anchor = CENTER)
        self.label444= Label(self.master, text="COLUMN_FOURTEEN NAME \n VALUE", font = fontStyle)
        self.label444.place(relx = 0.60, rely = 0.35, anchor = CENTER)
        self.label555= Label(self.master, text="COLUMN_FIFTEEN NAME \n VALUE", font = fontStyle)
        self.label555.place(relx = 0.60, rely = 0.45, anchor = CENTER)
        self.label666= Label(self.master, text="COLUMN_SIXTEEN NAME \n VALUE", font = fontStyle)
        self.label666.place(relx = 0.60, rely = 0.55, anchor = CENTER)
        self.label777= Label(self.master, text="COLUMN_SEVENTEEN NAME \n VALUE", font = fontStyle)
        self.label777.place(relx = 0.60, rely = 0.65, anchor = CENTER)
        self.label888= Label(self.master, text="COLUMN_EIGHTEEN NAME \n VALUE", font = fontStyle)
        self.label888.place(relx = 0.60, rely = 0.75, anchor = CENTER)
        self.label999= Label(self.master, text="COLUMN_NINETEEN NAME \n VALUE", font = fontStyle)
        self.label999.place(relx = 0.60, rely = 0.85, anchor = CENTER)
        self.label2000= Label(self.master, text="COLUMN_TWENTY NAME \n VALUE", font = fontStyle)
        self.label2000.place(relx = 0.60, rely = 0.95, anchor = CENTER)

        self.entry11 = Entry(self.master)
        self.entry11.place(relx = 0.25, rely = 0.05, anchor = CENTER)
        self.entry22 = Entry(self.master)
        self.entry22.place(relx = 0.25, rely = 0.15, anchor = CENTER)
        self.entry33 = Entry(self.master)
        self.entry33.place(relx = 0.25, rely = 0.25, anchor = CENTER)
        self.entry44 = Entry(self.master)
        self.entry44.place(relx = 0.25, rely = 0.35, anchor = CENTER)
        self.entry55 = Entry(self.master)
        self.entry55.place(relx = 0.25, rely = 0.45, anchor = CENTER)
        self.entry66 = Entry(self.master)
        self.entry66.place(relx = 0.25, rely = 0.55, anchor = CENTER)
        self.entry77 = Entry(self.master)
        self.entry77.place(relx = 0.25, rely = 0.65, anchor = CENTER)
        self.entry88 = Entry(self.master)
        self.entry88.place(relx = 0.25, rely = 0.75, anchor = CENTER)
        self.entry99 = Entry(self.master)
        self.entry99.place(relx = 0.25, rely = 0.85, anchor = CENTER)
        self.entry10 = Entry(self.master)
        self.entry10.place(relx = 0.25, rely = 0.95, anchor = CENTER)

        self.entry111 = Entry(self.master)
        self.entry111.place(relx = 0.75, rely = 0.05, anchor = CENTER)
        self.entry222 = Entry(self.master)
        self.entry222.place(relx = 0.75, rely = 0.15, anchor = CENTER)
        self.entry333 = Entry(self.master)
        self.entry333.place(relx = 0.75, rely = 0.25, anchor = CENTER)
        self.entry444 = Entry(self.master)
        self.entry444.place(relx = 0.75, rely = 0.35, anchor = CENTER)
        self.entry555 = Entry(self.master)
        self.entry555.place(relx = 0.75, rely = 0.45, anchor = CENTER)
        self.entry666 = Entry(self.master)
        self.entry666.place(relx = 0.75, rely = 0.55, anchor = CENTER)
        self.entry777 = Entry(self.master)
        self.entry777.place(relx = 0.75, rely = 0.65, anchor = CENTER)
        self.entry888 = Entry(self.master)
        self.entry888.place(relx = 0.75, rely = 0.75, anchor = CENTER)
        self.entry999 = Entry(self.master)
        self.entry999.place(relx = 0.75, rely = 0.85, anchor = CENTER)
        self.entry2000 = Entry(self.master)
        self.entry2000.place(relx = 0.75, rely = 0.95, anchor = CENTER)

        def createcols():
            entries.append(self.entry11.get())
            entries.append(self.entry22.get())
            entries.append(self.entry33.get())
            entries.append(self.entry44.get())
            entries.append(self.entry55.get())
            entries.append(self.entry66.get())
            entries.append(self.entry77.get())
            entries.append(self.entry88.get())
            entries.append(self.entry99.get())
            entries.append(self.entry10.get())
            entries.append(self.entry111.get())
            entries.append(self.entry222.get())
            entries.append(self.entry333.get())
            entries.append(self.entry444.get())
            entries.append(self.entry555.get())
            entries.append(self.entry666.get())
            entries.append(self.entry777.get())
            entries.append(self.entry888.get())
            entries.append(self.entry999.get())
            entries.append(self.entry2000.get())

            print(entries)

            count = 0
            for i in entries:
                if len(i)>0:
                    count = count + 1
                    countlist.append(count)
            print(countlist)
            count = max(countlist)
            print("count =", count)
            print(entry2)
            
            cursor0.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='%s' AND `TABLE_NAME`='%s' order by ordinal_position;" %(entry1, entry2))
            coloutput = cursor0.fetchall()
            print(coloutput)
            for col in coloutput:
                col = " ".join(col)
                columnslis.append(col)
            print(columnslis)

            if count == 1:
                cursor0.execute("INSERT INTO %s (%s) VALUES ('%s')" %(entry2, columnslis[0], entries[0]))
                connection.commit()
            elif count == 2:
                cursor0.execute("INSERT INTO %s (%s, %s) VALUES ('%s', '%s')" %(entry2, columnslis[0], columnslis[1], entries[0], entries[1]))
                connection.commit()
            elif count == 3:
                cursor0.execute("INSERT INTO %s (%s, %s, %s) VALUES ('%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], entries[0], entries[1], entries[2]))
                connection.commit()
            elif count == 4:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], entries[0], entries[1], entries[2], entries[3]))
                connection.commit()
            elif count == 5:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], entries[0], entries[1], entries[2], entries[3], entries[4]))
                connection.commit()
            elif count == 6:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5]))
                connection.commit()
            elif count == 7:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6]))
                connection.commit()
            elif count == 8:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7]))
                connection.commit()
            elif count == 9:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8]))
                connection.commit()
            elif count == 10:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9]))
                connection.commit()
            elif count == 11:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10]))
                connection.commit()
            elif count == 12:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11]))
                connection.commit()
            elif count == 13:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12]))
                connection.commit()
            elif count == 14:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13]))
                connection.commit()
            elif count == 15:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14]))
                connection.commit()
            elif count == 16:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], columnslis[15], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15]))
                connection.commit()
            elif count == 17:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], columnslis[15], columnslis[16], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16]))
                connection.commit()
            elif count == 18:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], columnslis[15], columnslis[16], columnslis[17], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17]))
                connection.commit()
            elif count == 19:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], columnslis[15], columnslis[16], columnslis[17], columnslis[18], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18]))
                connection.commit()
            elif count == 20:
                cursor0.execute("INSERT INTO %s (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(entry2, columnslis[0], columnslis[1], columnslis[2], columnslis[3], columnslis[4], columnslis[5], columnslis[6], columnslis[7], columnslis[8], columnslis[9], columnslis[10], columnslis[11], columnslis[12], columnslis[13], columnslis[14], columnslis[15], columnslis[16], columnslis[17], columnslis[18], columnslis[19], entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], entries[15], entries[16], entries[17], entries[18], entries[19]))
                connection.commit()

        
        def load_back9():
            self.label11.destroy()
            self.label22.destroy()
            self.label33.destroy()
            self.label44.destroy()
            self.label55.destroy()
            self.label66.destroy()
            self.label77.destroy()
            self.label88.destroy()
            self.label99.destroy()
            self.label10.destroy()
            self.label111.destroy()
            self.label222.destroy()
            self.label333.destroy()
            self.label444.destroy()
            self.label555.destroy()
            self.label666.destroy()
            self.label777.destroy()
            self.label888.destroy()
            self.label999.destroy()
            self.label2000.destroy()
            self.entry11.destroy()
            self.entry22.destroy()
            self.entry33.destroy()
            self.entry44.destroy()
            self.entry55.destroy()
            self.entry66.destroy()
            self.entry77.destroy()
            self.entry88.destroy()
            self.entry99.destroy()
            self.entry10.destroy()
            self.entry111.destroy()
            self.entry222.destroy()
            self.entry333.destroy()
            self.entry444.destroy()
            self.entry555.destroy()
            self.entry666.destroy()
            self.entry777.destroy()
            self.entry888.destroy()
            self.entry999.destroy()
            self.entry2000.destroy()
            self.btn7.destroy()
            self.btn39.destroy()

            entries.clear()
            countlist.clear()
            columnslis.clear()
            
            self.another = mainwindow(self.master)
            
        self.btn7 = tk.Button(self.master, text ="INSERT", font = fontStyle, command = createcols)
        self.btn7.place(relx = 0.9, rely = 0.80, anchor = CENTER)
        self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
        self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)

    
    def load_back(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        #self.btn3.destroy()
        self.another = mainwindow(self.master)
    
#set default window as mainwindow and run
save_connection(window)
window.mainloop()
