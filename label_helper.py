import PySimpleGUI as sg
import os

nextBtn = sg.Button("Next")
prevBtn = sg.Button("Previous")

def selectFilesLayout():
    layout =[
                [sg.Input(key=("_FILES_")), sg.FilesBrowse()],
                [nextBtn]
    ]
    return layout

def inputFilenameLayout(fileAbsDir, filename):
    layout = [
                [sg.Image(fileAbsDir + '/' + filename + '.png')],
                [sg.InputText(key="Answer", )],
                [prevBtn, nextBtn]
    ]
    return layout


browseWindow = sg.Window('Select Files', selectFilesLayout())
event, fileDict = browseWindow.Read()
if event != "Next" or len(fileDict["Browse"]) == 0:
    exit()
else:
    browseWindow.Close()

fileList = fileDict["_FILES_"].split(';')
fileAbsDir = '/'.join(fileList[0].split('/')[:-1])
fileList = [filename.split('/')[-1].split('.')[0] for filename in fileList]

index = 0
while index < len(fileList):
    newFilename = ""
    response = {}
    # try:
    inputWindow = sg.Window("[{}/{}] Please input - {}".format(index + 1, len(fileList), fileList[index]), inputFilenameLayout(fileAbsDir, fileList[index]))
    event, response = inputWindow.Read()
    newFilename = response["Answer"]

    if event == "Previous" and index > 0:
        if newFilename != "":
            os.rename(os.path.join(fileAbsDir, fileList[index] + ".png"), os.path.join(fileAbsDir, newFilename + ".png"))
            fileList[index] = newFilename
        index -= 1

    if event == "Next":
        if newFilename != "":
            os.rename(os.path.join(fileAbsDir, fileList[index] + ".png"), os.path.join(fileAbsDir, newFilename + ".png"))
            fileList[index] = newFilename
        # if index + 1 == len(fileList):
        #     print('Here')
        #     sg.Window("Finished!", [[sg.OK()]])
        # else:
        index += 1
    inputWindow.Close()

sg.Window("Finished!", [[sg.Text("Finished updating {} image labels.".format(len(fileList)))], [sg.OK()]]).Read()