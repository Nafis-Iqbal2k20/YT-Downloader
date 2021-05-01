# all required module importing command
from tkinter import*
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter.filedialog import askdirectory
from pytube import YouTube
from threading import *
import time

# global variable declaring
file_size = 0
streams = " "

# function


def start_download():
    global file_size
    global streams
    global d_btn
    try:
        url = url_field_entry.get()
        d_btn.config(state=DISABLED)
        path = askdirectory()
        if path is None:
            showwarning("warning", message="Please, select your directory first where you want to save "
                                           "your Video.")
        # print(path)
        d_btn.config(text="Staring Download")
        yt = YouTube(url)
        streams = yt.streams.first()
        # print(streams)
        title = yt.title
        title_label2.config(text=title)
        showinfo("Info", message="To see your full video title, please increase the window width.")
        rating = round(yt.rating, 1)
        rating_label2.config(text=rating)
        views = yt.views
        views_label2.config(text=views)
        file_size = round(streams.filesize/1048576, 2)
        size_label2.config(text=str(file_size)+'MB')
        d_btn.config(text="Please wait..")
        streams.download(path)
        d_btn.config(text="Done")
        d_btn.config(state=NORMAL)
        time.sleep(2)
        url_field_entry.delete(0, END)
        d_btn.config(text="start Download")
    except Exception as e:
        exception = str(e)
        showerror("Error", message=exception + ". Please, try with another video url")


def start_download_thread():
    thread = Thread(target=start_download)
    thread.start()


# start crating window
root = Tk()
root.geometry("500x430")
root.minsize(width=500, height=430)
root.wm_iconbitmap()
root.title("YT-Downloader")
# url field
url_field_label = Label(root, text="Enter your url down bellow")
url_field_label.pack()
url_field_entry = Entry(root, font=("verdana", 20), bg="aqua")
url_field_entry.pack(side=TOP, fill=X, pady=5, padx=10)
# d_btn creating
d_btn = Button(root, text="Start Download", font=("verdana", 10), command=start_download_thread)
d_btn.pack(side=TOP)
# video details r
title_label = Label(root, text="Video Title", font=("verdana", 10))
title_label.pack(side=TOP, fill=X, pady=10)
title_label2 = Label(root, text="", font=("verdana", 15), bg="Brown")
title_label2.pack(side=TOP, fill=X, padx=40)
rating_label = Label(root, text="Video Rating", font=("verdana", 10))
rating_label.pack(side=TOP, fill=X, pady=10)
rating_label2 = Label(root, text="", font=("verdana", 15), bg="Brown")
rating_label2.pack(side=TOP, fill=X, padx=40)
views_label = Label(root, text="Video Views", font=("verdana", 10))
views_label.pack(side=TOP, fill=X, pady=10)
views_label2 = Label(root, text="", font=("verdana", 15), bg="Brown")
views_label2.pack(side=TOP, fill=X, padx=40)
size_label = Label(root, text="Video Size", font=("verdana", 10))
size_label.pack(side=TOP, fill=X, pady=10)
size_label2 = Label(root, text="", font=("verdana", 15), bg="Brown")
size_label2.pack(side=TOP, fill=X, padx=40)
root.mainloop()         
# tkinter window mainloop the code is end :)
