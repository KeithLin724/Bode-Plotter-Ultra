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
    styleMain.configure('TLabelFrame', font=('Arial', 24))

    inputLabelFrame = LabelFrame(userFrame,
                                 text='Input',
                                 bootstyle='warning')

    global upperPloyEntry
    upperPloyEntry = kyEntry(frame=inputLabelFrame, entryName='輸入分子多項式 : ')

    global lowerPloyEntry
    lowerPloyEntry = kyEntry(frame=inputLabelFrame, entryName='輸入分母多項式 : ')

    global runBodePloterButton
    runBodePloterButton = Button(inputLabelFrame,
                                 text='run',
                                 bootstyle="success",
                                 command=run_bode_plotter,
                                 width=8).pack()
    inputLabelFrame.pack()

    funcLabel = LabelFrame(userFrame,
                           text='Transfor Function',
                           bootstyle='info',
                           width=20)

    global answerFuncOutputImageLabel
    answerFuncOutputImageLabel = Label(funcLabel)
    answerFuncOutputImageLabel.pack()
    funcLabel.pack()

    userFrame.pack(side=LEFT)

    # output bodeplot
    outputFrame = Frame(window)

    bodeLabel = LabelFrame(outputFrame,
                           text='Bode & Phase Plot',
                           bootstyle='info',
                           width=20)

    global bodePlotFuncOutputImageLabel
    bodePlotFuncOutputImageLabel = Label(bodeLabel)
    bodePlotFuncOutputImageLabel.pack()
    bodeLabel.pack()

    outputFrame.pack(side=RIGHT)

    # button frame (base on output Frame)
    buttonFrame = LabelFrame(outputFrame,
                             text='Function',
                             bootstyle='warning')

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
