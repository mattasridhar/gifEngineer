import os
import tkinter as tkt
from tkinter import filedialog, Text
from GifEngineerHandler import GifEngineerHandler

titleText = 'Gif Engineer'

gifFrmImgBtnText = 'Create GIF using Images'
gifFrmGifsBtnText = 'Create GIF using GIFs'
gifFrmVidBtnText = 'Create GIF using Video'
labelText = 'Please select the desired option and then the source directory/file. \nThe Gif will be created and rendered here. \nPlease be patient while it is processed!'

gifEngineerHandler = GifEngineerHandler()

# Creating the main Window
window = tkt.Tk()  # instance creation
canvas = tkt.Canvas(window, width=700, height=350,
                    bg='#454545')  # canvas creation
canvas.pack()
window.resizable(False, False)  # to prevent user from resizing the window
window.title(titleText)  # window title

label = tkt.Label(window, text=labelText).place(x=150, y=150)

# creating buttons and adding to frame
gifFrmImgBtn = tkt.Button(window, text=gifFrmImgBtnText, padx=0.5,
                          pady=0.5, bg='#454545', borderwidth=0, command=lambda: gifEngineerHandler.loadImgSrcDir(window)).place(x=0, y=0)

gifFrmGifsBtn = tkt.Button(window, text=gifFrmGifsBtnText, padx=0.5,
                           pady=0.5, bg='#454545', borderwidth=0, command=lambda: gifEngineerHandler.loadGIFSrcDir(window)).place(x=275, y=0)

gifFrmVidBtn = tkt.Button(window, text=gifFrmVidBtnText, padx=0.5,
                          pady=0.5, bg='#454545', borderwidth=0, command=lambda: gifEngineerHandler.loadVideoSrcDir(window)).place(x=532, y=0)

# handle window close
window.protocol("WM_DELETE_WINDOW",
                lambda: gifEngineerHandler.windowClose(window))

# show the created window
window.mainloop()
