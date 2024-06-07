# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:39:21 2021

@author: Shubham Madane
"""
import tkinter as tk 
from tkinter import StringVar,PhotoImage
import time
from tkinter import ttk
import serial
import csv
from csv import DictWriter
from threading import Thread
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile,askopenfile
from PIL import ImageTk, Image
#CREATE TKINTER WINDOW
Config_Window=tk.Tk()
#photo = PhotoImage(file ="")
photo = tk.PhotoImage(file="E:\Python\Test1_BMS\image\picture.png") 
Config_Window.title("Serial Port Reader")
Config_Window.geometry("670x500")
Config_Window.config(bg="#424242")
LARGE_FONT= ("Verdana",11)
LARGER_FONT= ("Verdana", 12)
Config_Window.iconphoto(False,photo) 
#photo = ImageTk.PhotoImage(Image.open('blueface.png'))

#img = ImageTk.PhotoImage(Image.open("wingz_logo.png"))
#panel = tk.Label(Config_Window, image = img)
#panel.grid(row = 1, column = 1,padx=1, pady=1,sticky=tk.W)


# LABLE AND ENTRY WIDGETS
Com= tk.Label(Config_Window,bg="#424242",text = "Serial Port Reader",font=LARGER_FONT,fg="white").grid(row = 1, column = 2,padx=30, pady=30,sticky=tk.W)  

ComPort=StringVar()
Com= tk.Label(Config_Window,bg="#424242",text ="COM Port",font=LARGE_FONT,fg="white").grid(row = 4, column = 1,padx=20, pady=20,sticky=tk.W)  
Com_entry = tk.Entry(Config_Window,text=ComPort)
Com_entry.grid(row = 4, column = 2,padx=10, pady=10,ipadx=35,ipady=7,sticky=tk.W)

BaudRate=StringVar()
baudrate= tk.Label(Config_Window,bg="#424242",text ="Baud Rate",font=LARGE_FONT,fg="white").grid(row = 6, column = 1,padx=20, pady=20,sticky=tk.W)  

Com_types = ttk.Combobox(Config_Window, width = 18, textvariable = BaudRate)
Com_types.grid(row = 6, column = 2,padx=10, pady=15,ipadx=35,ipady=7,sticky=tk.W) 
Com_types['values'] = ('Select',  
                          '4800 ', 
                          '9600 ', 
                          '14400',
                          '19200','38400','57600','115200')
Get_stram=StringVar()
Receive= tk.Label(Config_Window,bg="#424242",text = "Receive",font=LARGER_FONT,fg="white").grid(row = 16, column = 1,padx=10, pady=15,sticky=tk.W)  
GET_data = tk.Entry(Config_Window,text=Get_stram)
GET_data .grid(row = 17, column = 0,padx=15, pady=0,ipadx=235,ipady=40,sticky=tk.W,columnspan=5)

# line
tk.ttk.Separator(Config_Window, orient=tk.HORIZONTAL).grid(column=0, row=9,columnspan=100,sticky="EW",padx=5, pady=10)
# BUTTON
connect = tk.Button(Config_Window,bg="#cccccc", text = 'Connect',font=LARGER_FONT,state =tk.NORMAL,command = lambda :start_connect())
connect .grid(column=3,row=6,padx=0, pady=0)

Stop = tk.Button(Config_Window,bg="#cccccc", text = 'Disconnect',font=LARGER_FONT,state = tk.NORMAL,command = lambda :stoped()) 
Stop.grid(column=4,row=6,padx=3, pady=5)

Get_Data = tk.Button(Config_Window,bg="#cccccc", text = 'Start',font=LARGER_FONT,state = tk.NORMAL,command = lambda :start_Get()) 
Get_Data.grid(column=4, row=19,padx=0, pady=5,columnspan=1)

save = tk.Button(Config_Window,bg="#cccccc", text = 'Save to File',font=LARGER_FONT,state = tk.NORMAL,command = lambda :start_Save()) 
save.grid(column=3,row=19,padx=0, pady=5,columnspan=1)


# VARIABLE DECLARATION
List=[]
threads1=[]
threads2=[]
threads3=[]
File=''
data=''
ser=''

#Function defination
def Connect():
   connect.config(state=tk.DISABLED) 
   global List
   global File
   global ser
   comport= ComPort.get()
   print(comport)
   baudrate=BaudRate.get()
   print(baudrate)
   try:
    ser=serial.Serial(comport, baudrate,timeout=2)
   except:
        print("error in connection")
        messagebox.showwarning("Warning","Check Serial Port Connection")
   connect.config(state=tk.NORMAL) 
   #print(ser)


def Get(): #start button  of receive data 
   global ser
   global data
   Get_Data.config(state=tk.DISABLED)
   while True: 
    try:
      Data=ser.readline()
      print("Data",Data)
      data=Replace(Data)  
      GET_data.insert("end",data)
    except:
        messagebox.showwarning("Warning","Check Serial Port Connection")
        #print("") 
   Get_Data.config(state=tk.NORMAL) 
   
def Save(): 
   global File
   timestr = time.strftime("%Y%m%d-%H%M%S")
   #filename = 'SEM_Test'+timestr+'.txt'
   #print(filename)
   #file = open(filename,"a+")
   #print(file)
   #File=file
   #print(type(File))
   save.config(state=tk.DISABLED) 
   files = [('All Files', '*.*'), 
             ('Text Document', '*.txt')]
   File = asksaveasfile(mode ='a+',filetypes = files, defaultextension = files)
   try:
    File.write("\n-------------------------------")
    #File.write("\n Data Log")
    #print(File)
    #print("Data",data)
    File.write("\n\nTime:"+timestr)
    File.write("\n\n"+data)
    File.close()
   except:
      pass
   save.config(state=tk.NORMAL) 

def stop():
   global ser
   ser.close()
   print("")   

def Replace(Response):
    Response=str(Response)
    Response=Response.replace("b'","")
    Response=Response.replace("'","") 
    Response=Response.replace(";","")
    Response=Response.replace("EM","")
    Response=Response.replace("\\t","") 
    Response=Response.replace("\\n","")
    Response=Response.replace("\\r","")
    return Response  

# thread functions
def start_connect():
          global threads1
          t = Thread(target=Connect(),args=[])
          threads1.append(t)
          t.start()


def start_Save():
          global threads3
          t = Thread(target=Save(),args=[])
          threads1.append(t)
          t.start()

def start_Get():
          global threads2
          t = Thread(target=Get(),args=[])
          threads1.append(t)
          t.start() 

def stoped():
          global threads2
          t = Thread(target=stop(),args=[])
          threads1.append(t)
          t.start() 
connect.config(state=tk.NORMAL)        
Config_Window.mainloop()




