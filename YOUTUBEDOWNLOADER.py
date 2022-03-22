from cgitb import text
from importlib.resources import path
import shutil
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

def slp():
    
    p2 = filedialog.askdirectory()
    p1.config(text=path)

def downloadfile():
    getlink = LINK.get()
    usr_path = p1.cget ('text')
    DNA.title('downloading<<<...>>>')
    vid = YouTube(getlink).streams.get_highest_resolution().download()
    vid1 = VideoFileClip(vid)
    vid1.close()
    shutil.move(vid, usr_path)
    DNA.title('downloading completed!!')
    
DNA =Tk()
title = DNA.title('youtube downloader')
can = Canvas(DNA,width=500, height=500)
can.pack()

LINK = Entry(DNA, width=50)
L1 = Label(DNA, text=' Enter the link down her!! ' , font=('Arial', 15))

p1 = Label(DNA, text= 'select path down her !!!' ,font=('Arial', 20))
b1 = Button(DNA, text= 'select', command=p1)

can.create_window(250, 280, window=p1)
can.create_window(250, 330, window=b1)

can.create_window(250, 170, window=L1)
can.create_window(250, 220, window=LINK)

b2 = Button(DNA, text='Download file', command=downloadfile)
can.create_window(250, 365, window=b2)
DNA.mainloop()