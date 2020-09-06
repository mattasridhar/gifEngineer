import os
import tkinter as tkt
from tkinter import filedialog, Text
from GifEngineer import GifEngineer

titleText = 'Gif Engineer'
imageDirBtnText = 'Select Images directory'
videoDirBtnText = 'Select Video directory'
gifFrmImgBtnText = 'Create GIF using Images'
gifFrmVidBtnText = 'Create GIF using Video'
choiceMade = 'fromImages'

gifEngineer = GifEngineer()

# Creating the main Window
window = tkt.Tk()  # instance creation
canvas = tkt.Canvas(window, width=700, height=350,
                    bg='#454545')  # canvas creation
canvas.pack()
window.resizable(False, False)  # to prevent user from resizing the window
window.title(titleText)  # window title

gifFrmImgBtn = tkt.Button(window, text=gifFrmImgBtnText, padx=0.5,
                          pady=0.5, bg='#454545', borderwidth=0, command=lambda: gifEngineer.loadImgSrcDir(window)).place(x=0, y=0)  # creating button and adding to frame
# gifFrmImgBtn.pack(side='left')

gifFrmVidBtn = tkt.Button(window, text=gifFrmVidBtnText, padx=0.5,
                          pady=0.5, bg='#454545', borderwidth=0, command=lambda: gifEngineer.loadImgSrcDir(window)).place(x=532, y=0)  # creating button and adding to frame
# gifFrmVidBtn.pack(side='right')

# dirBtn = tkt.Button(frame, text=imageDirBtnText, padx=0.5,
#                     pady=0.5, bg='#b5b5b5', borderwidth=0, command=lambda: gifEngineer.loadImgSrcDir(frame))  # creating button and adding to frame
# dirBtn.pack()
# dirBtn.place(bordermode='outside', relwidth=0.5, relheight=0.5, relx=0.1, rely=0.1)

# handle window close
window.protocol("WM_DELETE_WINDOW", gifEngineer.windowClose(window))

# show the created window
window.mainloop()
