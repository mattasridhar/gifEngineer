import os
import tkinter as tkt
from tkinter import filedialog
import imageio
import shutil
import cv2
from datetime import datetime


class GifEngineer:
    def __init__(self):
        # For Images
        self.images = []
        self.imagesList = []
        self.imageEntns = ['.JPG', '.PNG', '.JPEG', '.TIFF']
        self.imageSrcDir = ''
        self.imageTrgtDir = ''
        self.tempDirName = '_temp'
        self.postFix = datetime.now()
        self.imageSrcDirTitle = 'Select Images Directory'

        # For GIF
        self.gifTrgtDir = ''
        self.gifTrgtDirBtnText = 'Save GIF @'
        self.gifTrgtDirTitle = 'Save GIF @ Directory'

    # select the directory path
    def loadImgSrcDir(self, frame):
        self.imageSrcDir = filedialog.askdirectory(title=self.imageSrcDirTitle)

        if self.imageSrcDir:
            # Create button and show on frame based on the selected type
            trgtDirBtn = tkt.Button(frame, text=self.gifTrgtDirBtnText, bg='#454545',
                                    borderwidth=0, command=lambda: self.loadGifTrgtDir())
            trgtDirBtn.pack()
            trgtDirBtn.place(bordermode='outside', x=0.1, y=0.1)

    # select the target directory path
    def loadGifTrgtDir(self):
        self.gifTrgtDir = filedialog.askdirectory(
            initialdir=self.imageSrcDir, title=self.gifTrgtDirTitle)

        if self.gifTrgtDir:
            self.gifFromImages(self.imageSrcDir, self.gifTrgtDir)

    # form a Gif using images
    def gifFromImages(self, srcDirPath, gifDirPath):
        self.imageTrgtDir = os.path.join(self.imageSrcDir, self.tempDirName)
        if not os.path.isdir(self.imageTrgtDir):
            print('Creating a temporary directory..')
            os.mkdir(self.imageTrgtDir)
        gifFilename = 'gifFromImages' + \
            self.postFix.strftime('%m%d%Y_%H%M%S') + '.gif'

        # copy the images to a temp file for safety
        for filename in os.listdir(srcDirPath):
            source = srcDirPath + '/' + filename
            target = self.imageTrgtDir + '/' + filename
            if filename is not None and os.path.isfile(source):
                fName, fExt = os.path.splitext(filename)
                if fExt.upper() in self.imageEntns:
                    shutil.copyfile(source, target)
                    self.images.append(source)

        # create the gif and save to the destination
        try:
            with imageio.get_writer(gifDirPath + '/' + gifFilename, mode='I') as writer:
                for filePath in self.images:
                    image = imageio.imread(filePath)
                    writer.append_data(image)
            print('Creation of Gif completed.')
            shutil.rmtree(self.imageTrgtDir)
        except:
            print('Error while creating the GIF.')
