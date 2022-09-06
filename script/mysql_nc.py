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

#connecting mysql database
#connection = connect(host="localhost",user="root",password="55+DAta#3")
#print(connection)

#for executing sql operations
#cursor = connection.cursor()

#setting the window
window = Tk()
window.title("MYSQL NO_CODE")
window.configure(width=600, height=700)
fontStyle = tkFont.Font(family="Candara", size=14)
fontStyle1 = tkFont.Font(family="Candara", size=17)

namelist = []

class mainwindow:
    def __init__(self, master):
        self.master = master

        self.master = master
        self.btn1 = tk.Button(self.master, text ="CREATE/DROP DATABSE", font = fontStyle1, command = self.clearpage1)
        self.btn1.place(relx = 0.5, rely = 0.40, anchor = CENTER)
        self.btn2 = tk.Button(self.master, text ="CREATE/DROP TABLE IN A DATABASE", font = fontStyle1, command = self.clearpage2)
        self.btn2.place(relx = 0.5, rely = 0.50, anchor = CENTER)
        self.btn3 = tk.Button(self.master, text ="INSERT/DELETE INPUTS IN A TABLE", font = fontStyle1, command = self.clearpage3)
        self.btn3.place(relx = 0.5, rely = 0.60, anchor = CENTER)

    #functions to clear the page to view the next page elements
    def clearpage1(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.another = cd_database(self.master)
    def clearpage2(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.another = cd_table(self.master)
    def clearpage3(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.another = inputs(self.master)

class cd_database:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle, command = self.load_back)
        self.btn1.place(relx = 0.90, rely = 0.84, anchor = CENTER)

        self.label1= Label(self.master, text="HOST ", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.08, anchor = CENTER)
        self.label2= Label(self.master, text="USER", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.12, anchor = CENTER)
        self.label3= Label(self.master, text="PASSWORD", font = fontStyle)
        self.label3.place(relx = 0.22, rely = 0.16, anchor = CENTER)

        self.label4= Label(self.master, text="CREATE DATABASE ", font = fontStyle)
        self.label4.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label5= Label(self.master, text="DROP DATABASE ", font = fontStyle)
        self.label5.place(relx = 0.22, rely = 0.60, anchor = CENTER)

        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.5, rely = 0.08, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.5, rely = 0.12, anchor = CENTER)
        self.entry3 = Entry(self.master)
        self.entry3.place(relx = 0.5, rely = 0.16, anchor = CENTER)
        self.entry4 = Entry(self.master)
        self.entry4.place(relx = 0.5, rely = 0.30, anchor = CENTER)
        self.entry5 = Entry(self.master)
        self.entry5.place(relx = 0.5, rely = 0.60, anchor = CENTER)

        def create():
            entry1 = self.entry1.get()
            entry2 = self.entry2.get()
            entry3 = self.entry3.get()
            entry4 = self.entry4.get()
            connection = connect(host="%s" %(entry1),user="%s" %(entry2),password="%s" %(entry3))
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE %s" %(entry4))
        def drop():
            entry1 = self.entry1.get()
            entry2 = self.entry2.get()
            entry3 = self.entry3.get()
            entry5 = self.entry5.get()
            connection = connect(host="%s" %(entry1),user="%s" %(entry2),password="%s" %(entry3))
            cursor = connection.cursor()
            cursor.execute("DROP DATABASE IF EXISTS `%s`" %(entry5))
        self.btn2 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create)
        self.btn2.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        self.btn3 = tk.Button(self.master, text ="DROP", font = fontStyle, command = drop)
        self.btn3.place(relx = 0.5, rely = 0.65, anchor = CENTER)

    #function to clear the current page to view the previous page elements
    def load_back(self):
        self.entry1.destroy()
        self.entry2.destroy()
        self.entry3.destroy()
        self.entry4.destroy()
        self.entry5.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.another = mainwindow(self.master)


class cd_table:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle, command = self.load_backk)
        self.btn1.place(relx = 0.90, rely = 0.90, anchor = CENTER)
        
        self.label1= Label(self.master, text="ENTER TABLE NAME", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.label2= Label(self.master, text="ENTER NUMBER OF COLUMNS", font = fontStyle)
        self.label2.place(relx = 0.22, rely = 0.40, anchor = CENTER)
        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.6, rely = 0.30, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.6, rely = 0.40, anchor = CENTER)

        def cols():
            self.label1.destroy()
            self.label2.destroy()
            self.btn1.destroy()
            entry1 = self.entry1.get()
            entry2 = int(self.entry2.get())
            self.btn2.destroy()
            namelist.append(entry1)
            self.entry1.destroy()
            self.entry2.destroy()
        
            if entry2 == 1:
                self.label11= Label(self.master, text="COLUMN_ONE NAME", font = fontStyle)
                self.label11.place(relx = 0.22, rely = 0.30, anchor = CENTER)
                self.label22= Label(self.master, text="COLUMN_ONE TYPE \n AND LENGTH", font = fontStyle)
                self.label22.place(relx = 0.22, rely = 0.40, anchor = CENTER)

                self.entry11 = Entry(self.master)
                self.entry11.place(relx = 0.6, rely = 0.30, anchor = CENTER)
                self.entry22 = Entry(self.master)
                self.entry22.place(relx = 0.6, rely = 0.40, anchor = CENTER)
        
                #cursor.execute("CREATE DATABASE %s" %(entry1))
                def create1():
                    connection = connect(host="localhost",user="root", database="new_database1",password="55+DAta#3")
                    cursor2 = connection.cursor()                    
                    entry111 = self.entry11.get()
                    entry222 = self.entry22.get()
                    com = entry111 + " " + entry222
                    for i in namelist:
                        cursor2.execute("CREATE TABLE %s (%s)" %(i, com))

                def load_back9():
                    self.label11.destroy()
                    self.label22.destroy()
                    self.entry11.destroy()
                    self.entry22.destroy()
                    self.btn3.destroy()
                    self.btn39.destroy()
                    self.another = mainwindow(self.master)

                self.btn3 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create1)
                self.btn3.place(relx = 0.6, rely = 0.50, anchor = CENTER)
                self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
                self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
            elif entry2 == 2:
                self.label11= Label(self.master, text="COLUMN_ONE NAME", font = fontStyle)
                self.label11.place(relx = 0.22, rely = 0.20, anchor = CENTER)
                self.label22= Label(self.master, text="COLUMN_ONE TYPE \n AND LENGTH", font = fontStyle)
                self.label22.place(relx = 0.22, rely = 0.30, anchor = CENTER)
                self.label33= Label(self.master, text="COLUMN_TWO NAME", font = fontStyle)
                self.label33.place(relx = 0.22, rely = 0.40, anchor = CENTER)
                self.label44= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
                self.label44.place(relx = 0.22, rely = 0.50, anchor = CENTER)


                self.entry11 = Entry(self.master)
                self.entry11.place(relx = 0.6, rely = 0.20, anchor = CENTER)
                self.entry22 = Entry(self.master)
                self.entry22.place(relx = 0.6, rely = 0.30, anchor = CENTER)
                self.entry33 = Entry(self.master)
                self.entry33.place(relx = 0.6, rely = 0.40, anchor = CENTER)
                self.entry44 = Entry(self.master)
                self.entry44.place(relx = 0.6, rely = 0.50, anchor = CENTER)
        
                #cursor.execute("CREATE DATABASE %s" %(entry1))
                def create2():
                    connection = connect(host="localhost",user="root", database="new_database1",password="55+DAta#3")
                    cursor3 = connection.cursor()
                    entry111 = self.entry11.get()
                    entry222 = self.entry22.get()
                    entry333 = self.entry33.get()
                    entry444 = self.entry44.get()
                    com1 = entry111 + " " + entry222
                    com2 = entry333 + " " + entry444
                    for i in namelist:
                        cursor3.execute("CREATE TABLE %s (%s, %s)" %(i, com1, com2))
                def load_back9():
                    self.label11.destroy()
                    self.label22.destroy()
                    self.label33.destroy()
                    self.label44.destroy()
                    self.entry11.destroy()
                    self.entry22.destroy()
                    self.entry33.destroy()
                    self.entry44.destroy()
                    self.btn4.destroy()
                    self.btn39.destroy()
                    self.another = mainwindow(self.master)
            
                self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
                self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
                self.btn4 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create2)
                self.btn4.place(relx = 0.6, rely = 0.60, anchor = CENTER)
            elif entry2 == 3:
                self.label11= Label(self.master, text="COLUMN_ONE NAME", font = fontStyle)
                self.label11.place(relx = 0.22, rely = 0.10, anchor = CENTER)
                self.label22= Label(self.master, text="COLUMN_ONE TYPE \n AND LENGTH", font = fontStyle)
                self.label22.place(relx = 0.22, rely = 0.20, anchor = CENTER)
                self.label33= Label(self.master, text="COLUMN_TWO NAME", font = fontStyle)
                self.label33.place(relx = 0.22, rely = 0.30, anchor = CENTER)
                self.label44= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
                self.label44.place(relx = 0.22, rely = 0.40, anchor = CENTER)
                self.label55= Label(self.master, text="COLUMN_THREE NAME", font = fontStyle)
                self.label55.place(relx = 0.22, rely = 0.50, anchor = CENTER)
                self.label66= Label(self.master, text="COLUMN_THREE TYPE \n AND LENGTH", font = fontStyle)
                self.label66.place(relx = 0.22, rely = 0.60, anchor = CENTER)


                self.entry11 = Entry(self.master)
                self.entry11.place(relx = 0.6, rely = 0.10, anchor = CENTER)
                self.entry22 = Entry(self.master)
                self.entry22.place(relx = 0.6, rely = 0.20, anchor = CENTER)
                self.entry33 = Entry(self.master)
                self.entry33.place(relx = 0.6, rely = 0.30, anchor = CENTER)
                self.entry44 = Entry(self.master)
                self.entry44.place(relx = 0.6, rely = 0.40, anchor = CENTER)
                self.entry55 = Entry(self.master)
                self.entry55.place(relx = 0.6, rely = 0.50, anchor = CENTER)
                self.entry66 = Entry(self.master)
                self.entry66.place(relx = 0.6, rely = 0.60, anchor = CENTER)
        
                #cursor.execute("CREATE DATABASE %s" %(entry1))
                def create3():
                    connection = connect(host="localhost",user="root", database="new_database1",password="55+DAta#3")
                    cursor4 = connection.cursor()
                    entry111 = self.entry11.get()
                    entry222 = self.entry22.get()
                    entry333 = self.entry33.get()
                    entry444 = self.entry44.get()
                    entry555 = self.entry55.get()
                    entry666 = self.entry66.get()
                    com1 = entry111 + " " + entry222
                    com2 = entry333 + " " + entry444
                    com3 = entry555 + " " + entry666
                    for i in namelist:
                        cursor4.execute("CREATE TABLE %s (%s, %s, %s)" %(i, com1, com2, com3))
                    
                def load_back9():
                    self.label11.destroy()
                    self.label22.destroy()
                    self.label33.destroy()
                    self.label44.destroy()
                    self.label55.destroy()
                    self.label66.destroy()
                    self.entry11.destroy()
                    self.entry22.destroy()
                    self.entry33.destroy()
                    self.entry44.destroy()
                    self.entry55.destroy()
                    self.entry66.destroy()                    
                    self.btn5.destroy()
                    self.btn39.destroy()
                    self.another = mainwindow(self.master)
            
                self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
                self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
                self.btn5 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create3)
                self.btn5.place(relx = 0.6, rely = 0.70, anchor = CENTER)
                
            elif entry2 == 4:
                self.label11= Label(self.master, text="COLUMN_ONE NAME", font = fontStyle)
                self.label11.place(relx = 0.22, rely = 0.10, anchor = CENTER)
                self.label22= Label(self.master, text="COLUMN_ONE TYPE \n AND LENGTH", font = fontStyle)
                self.label22.place(relx = 0.22, rely = 0.20, anchor = CENTER)
                self.label33= Label(self.master, text="COLUMN_TWO NAME", font = fontStyle)
                self.label33.place(relx = 0.22, rely = 0.30, anchor = CENTER)
                self.label44= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
                self.label44.place(relx = 0.22, rely = 0.40, anchor = CENTER)
                self.label55= Label(self.master, text="COLUMN_THREE NAME", font = fontStyle)
                self.label55.place(relx = 0.22, rely = 0.50, anchor = CENTER)
                self.label66= Label(self.master, text="COLUMN_THREE TYPE \n AND LENGTH", font = fontStyle)
                self.label66.place(relx = 0.22, rely = 0.60, anchor = CENTER)
                self.label77= Label(self.master, text="COLUMN_FOUR NAME", font = fontStyle)
                self.label77.place(relx = 0.22, rely = 0.70, anchor = CENTER)
                self.label88= Label(self.master, text="COLUMN_FOUR TYPE \n AND LENGTH", font = fontStyle)
                self.label88.place(relx = 0.22, rely = 0.80, anchor = CENTER)


                self.entry11 = Entry(self.master)
                self.entry11.place(relx = 0.6, rely = 0.10, anchor = CENTER)
                self.entry22 = Entry(self.master)
                self.entry22.place(relx = 0.6, rely = 0.20, anchor = CENTER)
                self.entry33 = Entry(self.master)
                self.entry33.place(relx = 0.6, rely = 0.30, anchor = CENTER)
                self.entry44 = Entry(self.master)
                self.entry44.place(relx = 0.6, rely = 0.40, anchor = CENTER)
                self.entry55 = Entry(self.master)
                self.entry55.place(relx = 0.6, rely = 0.50, anchor = CENTER)
                self.entry66 = Entry(self.master)
                self.entry66.place(relx = 0.6, rely = 0.60, anchor = CENTER)
                self.entry77 = Entry(self.master)
                self.entry77.place(relx = 0.6, rely = 0.70, anchor = CENTER)
                self.entry88 = Entry(self.master)
                self.entry88.place(relx = 0.6, rely = 0.80, anchor = CENTER)
        
                #cursor.execute("CREATE DATABASE %s" %(entry1))
                def create4():
                    connection = connect(host="localhost",user="root", database="new_database1",password="55+DAta#3")
                    cursor5 = connection.cursor()
                    entry111 = self.entry11.get()
                    entry222 = self.entry22.get()
                    entry333 = self.entry33.get()
                    entry444 = self.entry44.get()
                    entry555 = self.entry55.get()
                    entry666 = self.entry66.get()
                    entry777 = self.entry77.get()
                    entry888 = self.entry88.get()
                    com1 = entry111 + " " + entry222
                    com2 = entry333 + " " + entry444
                    com3 = entry555 + " " + entry666
                    com4 = entry777 + " " + entry888
                    for i in namelist:
                        cursor5.execute("CREATE TABLE %s (%s, %s, %s, %s)" %(i, com1, com2, com3, com4))
                    
                def load_back9():
                    self.label11.destroy()
                    self.label22.destroy()
                    self.label33.destroy()
                    self.label44.destroy()
                    self.label55.destroy()
                    self.label66.destroy()
                    self.label77.destroy()
                    self.label88.destroy()
                    self.entry11.destroy()
                    self.entry22.destroy()
                    self.entry33.destroy()
                    self.entry44.destroy()
                    self.entry55.destroy()
                    self.entry66.destroy()
                    self.entry77.destroy()
                    self.entry88.destroy()
                    self.btn6.destroy()
                    self.btn39.destroy()
                    self.another = mainwindow(self.master)
            
                self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
                self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
                self.btn6 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create4)
                self.btn6.place(relx = 0.6, rely = 0.90, anchor = CENTER)
                
            elif entry2 == 5:
                self.label11= Label(self.master, text="COLUMN_ONE NAME", font = fontStyle)
                self.label11.place(relx = 0.22, rely = 0.08 , anchor = CENTER)
                self.label22= Label(self.master, text="COLUMN_ONE TYPE \n AND LENGTH", font = fontStyle)
                self.label22.place(relx = 0.22, rely = 0.16, anchor = CENTER)
                self.label33= Label(self.master, text="COLUMN_TWO NAME", font = fontStyle)
                self.label33.place(relx = 0.22, rely = 0.24, anchor = CENTER)
                self.label44= Label(self.master, text="COLUMN_TWO TYPE \n AND LENGTH", font = fontStyle)
                self.label44.place(relx = 0.22, rely = 0.32, anchor = CENTER)
                self.label55= Label(self.master, text="COLUMN_THREE NAME", font = fontStyle)
                self.label55.place(relx = 0.22, rely = 0.40, anchor = CENTER)
                self.label66= Label(self.master, text="COLUMN_THREE TYPE \n AND LENGTH", font = fontStyle)
                self.label66.place(relx = 0.22, rely = 0.48, anchor = CENTER)
                self.label77= Label(self.master, text="COLUMN_FOUR NAME", font = fontStyle)
                self.label77.place(relx = 0.22, rely = 0.56, anchor = CENTER)
                self.label88= Label(self.master, text="COLUMN_FOUR TYPE \n AND LENGTH", font = fontStyle)
                self.label88.place(relx = 0.22, rely = 0.64, anchor = CENTER)
                self.label99= Label(self.master, text="COLUMN_FIVE NAME", font = fontStyle)
                self.label99.place(relx = 0.22, rely = 0.72, anchor = CENTER)
                self.label10= Label(self.master, text="COLUMN_FIVE TYPE \n AND LENGTH", font = fontStyle)
                self.label10.place(relx = 0.22, rely = 0.80, anchor = CENTER)


                self.entry11 = Entry(self.master)
                self.entry11.place(relx = 0.6, rely = 0.08, anchor = CENTER)
                self.entry22 = Entry(self.master)
                self.entry22.place(relx = 0.6, rely = 0.16, anchor = CENTER)
                self.entry33 = Entry(self.master)
                self.entry33.place(relx = 0.6, rely = 0.24, anchor = CENTER)
                self.entry44 = Entry(self.master)
                self.entry44.place(relx = 0.6, rely = 0.32, anchor = CENTER)
                self.entry55 = Entry(self.master)
                self.entry55.place(relx = 0.6, rely = 0.40, anchor = CENTER)
                self.entry66 = Entry(self.master)
                self.entry66.place(relx = 0.6, rely = 0.48, anchor = CENTER)
                self.entry77 = Entry(self.master)
                self.entry77.place(relx = 0.6, rely = 0.56, anchor = CENTER)
                self.entry88 = Entry(self.master)
                self.entry88.place(relx = 0.6, rely = 0.64, anchor = CENTER)
                self.entry99 = Entry(self.master)
                self.entry99.place(relx = 0.6, rely = 0.72, anchor = CENTER)
                self.entry10 = Entry(self.master)
                self.entry10.place(relx = 0.6, rely = 0.80, anchor = CENTER)
        
                #cursor.execute("CREATE DATABASE %s" %(entry1))
                def create5():
                    connection = connect(host="localhost",user="root", database="new_database1",password="55+DAta#3")
                    cursor6 = connection.cursor()
                    entry111 = self.entry11.get()
                    entry222 = self.entry22.get()
                    entry333 = self.entry33.get()
                    entry444 = self.entry44.get()
                    entry555 = self.entry55.get()
                    entry666 = self.entry66.get()
                    entry777 = self.entry77.get()
                    entry888 = self.entry88.get()
                    entry999 = self.entry99.get()
                    entry100 = self.entry10.get()
                    com1 = entry111 + " " + entry222
                    com2 = entry333 + " " + entry444
                    com3 = entry555 + " " + entry666
                    com4 = entry777 + " " + entry888
                    com5 = entry999 + " " + entry100
                    for i in namelist:
                        cursor6.execute("CREATE TABLE %s (%s, %s, %s, %s, %s)" %(i, com1, com2, com3, com4, com5))

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
                    self.btn7.destroy()
                    self.btn39.destroy()
                    self.another = mainwindow(self.master)
            
                self.btn39 = tk.Button(self.master, text ="BACK", font = fontStyle, command = load_back9)
                self.btn39.place(relx = 0.9, rely = 0.90, anchor = CENTER)
                self.btn7 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = create5)
                self.btn7.place(relx = 0.6, rely = 0.90, anchor = CENTER)
        self.btn2 = tk.Button(self.master, text ="NEXT", font = fontStyle, command = cols)
        self.btn2.place(relx = 0.6, rely = 0.50, anchor = CENTER)
    
    def load_backk(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.another = mainwindow(self.master)

class inputs:
    def __init__(self, master):
        self.master = master

        self.btn1 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn1.place(relx = 0.90, rely = 0.84, anchor = CENTER)

        self.label1= Label(self.master, text="ENTER HOST", font = fontStyle)
        self.label1.place(relx = 0.22, rely = 0.20, anchor = CENTER)
        self.labe22= Label(self.master, text="ENTER USER", font = fontStyle)
        self.labe22.place(relx = 0.22, rely = 0.30, anchor = CENTER)
        self.labe33= Label(self.master, text="ENTER DATABASE", font = fontStyle)
        self.labe33.place(relx = 0.22, rely = 0.40, anchor = CENTER)
        self.labe44= Label(self.master, text="ENTER PASSWORD", font = fontStyle)
        self.labe44.place(relx = 0.22, rely = 0.50, anchor = CENTER)
        self.label55= Label(self.master, text="ENTER TABLE_NAME", font = fontStyle)
        self.label55.place(relx = 0.22, rely = 0.60, anchor = CENTER)

        self.entry1 = Entry(self.master)
        self.entry1.place(relx = 0.6, rely = 0.20, anchor = CENTER)
        self.entry2 = Entry(self.master)
        self.entry2.place(relx = 0.6, rely = 0.30, anchor = CENTER)
        self.entry3 = Entry(self.master)
        self.entry3.place(relx = 0.6, rely = 0.40, anchor = CENTER)
        self.entry4 = Entry(self.master)
        self.entry4.place(relx = 0.6, rely = 0.50, anchor = CENTER)
        self.entry5 = Entry(self.master)
        self.entry5.place(relx = 0.6, rely = 0.60, anchor = CENTER)

        
        def col():
            ent1 = self.entry1.get()
            ent2 = self.entry2.get()
            ent3 = self.entry3.get()
            ent4 = self.entry4.get()
            ent5 = self.entry5.get()
            connection = connect(host="%s" %(ent1),user="%s" %(ent2), database="%s" %(ent3),password="%s" %(ent4))
            #for executing sql operations
            cursor9 = connection.cursor()

            cursor9.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name= '%s';" %(ent5))
            coli=cursor9.fetchall()
            
            for x in coli:
                for i in x:
                    if i == 1:
                        self.label1.destroy()
                        self.labe22.destroy()
                        self.labe33.destroy()
                        self.labe44.destroy()
                        self.labe55.destroy()
                        self.entry1.destroy()
                        self.entry2.destroy()
                        self.entry3.destroy()
                        self.entry4.destroy()
                        self.entry5.destroy()

                        def coll():   
                            self.label1= Label(self.master, text="INPUT", font = fontStyle)
                            self.label1.place(relx = 0.22, rely = 0.20, anchor = CENTER)
                            self.entry1 = Entry(self.master)
                            self.entry1.place(relx = 0.6, rely = 0.20, anchor = CENTER)

                            ent = self.entry1.get()
                            cursor9.execute("INSERT INTO %s (%s);" %(ent5, ent))

                        self.btn77 = tk.Button(self.master, text ="INSERT", font = fontStyle, command = coll)
                        self.btn77.place(relx = 0.6, rely = 0.90, anchor = CENTER)
        self.btn7 = tk.Button(self.master, text ="CREATE", font = fontStyle, command = col)
        self.btn7.place(relx = 0.6, rely = 0.90, anchor = CENTER)



    #function to clear the current page to view the previous page elements
    def load_back(self):
        self.entry_1.destroy()
        self.btn1.destroy()
     

        self.another = mainwindow(self.master)


#make window unexpandable(fixed)
window.resizable(False,False)
#set default window as mainwindow and run
mainwindow(window)
window.mainloop()
