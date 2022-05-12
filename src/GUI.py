from ttkbootstrap import *
from KY_Entry import kyEntry
from button_function import *


def init(window: Window) -> None:
    # User Frame
    userFrame = Frame(window)

    global styleMain
    styleMain = Style()
    styleMain.configure('TLabel', font=('Arial', 13))
    styleMain.configure('TButton', font=('Arial', 13))

    global upperPloyEntry
    upperPloyEntry = kyEntry(frame=userFrame, entryName='輸入分子多項式 : ')

    global lowerPloyEntry
    lowerPloyEntry = kyEntry(frame=userFrame, entryName='輸入分母多項式 : ')

    global runBodePloterButton
    runBodePloterButton = Button(userFrame,
                                 text='run',
                                 command=run_bode_ploter,
                                 width=8).pack()

    funcLabel = Label(userFrame,
                      text='Transfor Function',
                      width=20).pack()

    global answerFuncOutputImageLabel
    answerFuncOutputImageLabel = Label(userFrame)
    answerFuncOutputImageLabel.pack()

    userFrame.pack(side=LEFT)

    # output bodeplot
    outputFrame = Frame(window)

    bodeLabel = LabelFrame(outputFrame,
                           text='Bode & Phase Plot',
                           width=20).pack()

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
                                width=8).pack()

    global saveFileButton
    saveFileButton = Button(buttonFrame,
                            text='save',
                            command=save_file,
                            width=8).pack()

    global clearButton
    clearButton = Button(buttonFrame,
                         text='clear',
                         command=clear,
                         width=8).pack()

    buttonFrame.pack()
