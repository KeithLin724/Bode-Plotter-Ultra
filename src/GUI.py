from tkinter import *
from KY_Entry import kyEntry
from button_function import *


def init(window: Tk) -> None:
    # User Frame
    userFrame = Frame(window)

    global upperPloyEntry
    upperPloyEntry = kyEntry(frame=userFrame, entryName='輸入分子多項式 : ')

    global lowerPloyEntry
    lowerPloyEntry = kyEntry(frame=userFrame, entryName='輸入分母多項式 : ')

    global runBodePloterButton
    runBodePloterButton = Button(userFrame,
                                 text='run',
                                 command=run_bode_ploter,
                                 width=8, height=1).pack()

    funcLabel = Label(userFrame, text='Transfor Function',
                      width=20,
                      font=('Arial', 16)).pack()

    global answerFuncOutputImageLabel
    answerFuncOutputImageLabel = Label(userFrame)
    answerFuncOutputImageLabel.pack()

    userFrame.pack(side=LEFT)

    # output bodeplot
    outputFrame = Frame(window)

    bodeLabel = Label(outputFrame, text='Bode & Phase Plot',
                      width=20,
                      font=('Arial', 16)).pack()

    global bodePlotFuncOutputImageLabel
    bodePlotFuncOutputImageLabel = Label(outputFrame)
    bodePlotFuncOutputImageLabel.pack()

    outputFrame.pack(side=RIGHT)

    # button frame (base on output Frame)
    buttonFrame = Frame(outputFrame)

    global openBodePlotButton
    openBodePlotButton = Button(buttonFrame,
                                text='open',
                                command=open_bode_plot_detail,
                                width=8, height=1).pack()

    global saveFileButton
    saveFileButton = Button(buttonFrame,
                            text='save',
                            command=save_file,
                            width=8, height=1).pack()

    global clearButton
    clearButton = Button(buttonFrame,
                         text='clear',
                         command=clear,
                         width=8, height=1).pack()

    buttonFrame.pack()
