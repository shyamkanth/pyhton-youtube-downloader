from tkinter import *
from pytube import YouTube
import os
 
root = Tk()
root.title("D-Tube : YouTube Video Downloader")
root.minsize(500,500)
root.resizable(0,0)
msg= Label(root, text="Welcome To YouTube Video Downloader \n By Shyam Kanth"
             ,font=("Times New",12),bg="Yellow", fg="Black",padx=10, pady=10)
msg.place(x=90, y=20)
msg1= Label(root, text="Enter a valid Youtube URL :", font=("Arial", 10),
            fg="Black", pady=16)
msg1.place(x=40, y=100)
 
entry1=Entry(root,font=("Arial", 7), width=35)
entry1.place(x=270, y=120)
def veri():
    link = entry1.get()
    try:
        video = YouTube(link)
        def down():
            def fdown():
                path = entry2.get()
                isExist = os.path.exists(path)
                if isExist:
                    YouTube(link).streams.first().download(path)
                    msg6 = Label(root, text="Wooohoo...\nDownload Completed Successfully",fg="Green")
                    msg6.place(x=150, y=430)
                else:
                    msg7 = Label(root, text="OOPS!!!\nPath Not Found\nPlease Provide Correct Path For Download.", fg="Red")
                    msg7.place(x=122, y=430)
            msg2= Label(root, text="Enter Path (e.g. drive\..\ folder)", font=("Arial", 10),
                        fg="Black", pady=16)
            msg2.place(x=40, y=330)
            entry2 = Entry(root,font=("Arial", 7), width=35)
            entry2.place(y=350, x=270)
            fdownload= Button(root, text="Download", font=("Arial", 12),bg="Black",fg="White", width=10, command=fdown)
            fdownload.place(x=190, y=390)
        title= Label(root,fg="Green", text="Title : "+video.title)
        title.place(y=210, x=40)
        duration= Label(root,fg="Green", text="Duration : "+str(video.length)+" seconds")
        duration.place(y=230, x=40)
        views= Label(root,fg="Green", text="Views : "+str(video.views))
        views.place(y=250, x=40)
        rating= Label(root,fg="Green",text="Rating : "+str(video.rating))
        rating.place(y=270, x=40)
        download=Button(root, text="Want to Download", font=("Arial", 12),bg="Black",fg="White"
                                      , width=18, command=down)
        download.place(y=290, x=160)
    except KeyError:
        msg5= Label(root, text="OOPS!!! Video Not Downloadable.\n Please Enter A Valid URL",fg="Red")
        msg5.place(y=210, x=150)
     
     
verify=Button(root, text="Fetch Detail", font=("Arial", 12),bg="Black",fg="White"
                          , width=15, command=veri)
verify.place(y=170, x=170)
 
root.mainloop()
