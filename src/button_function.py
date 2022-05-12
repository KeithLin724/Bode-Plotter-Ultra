# button function
#NOTE: GUI
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from ttkbootstrap import *
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import os
import shutil
from attr import define
# NOTE: math and graph library
from sympy import polys
from numpy import array
from control.matlab import tf, pole, zero, bode
from matplotlib.pyplot import close, savefig, show
# NOTE: write by my self
from DeBug import kyDebugTk
from KY_Entry import kyEntry
import latex_div as ld
import GUI
from window_upgrade import get_ppi

global haveRunBodePloter
haveRunBodePloter = False

global window_dpi
window_dpi = get_ppi()


def set_haveRunBodePloter(TF: bool) -> None:
    global haveRunBodePloter
    haveRunBodePloter = TF


def open_bode_plot_detail() -> None:  # open bode ploter more pro
    kyDebugTk.outMsg(msg='open bode ploter')  # DEBUG:
    if haveRunBodePloter == True:
        mag, phase, omega = bode(transFuncG)
        show()
    else:
        messagebox.showerror(title='error',
                             message='Didn\'t Run the build Bode plot button')
        return


def topLevel_com() -> None:
    kyDebugTk.outMsg('ToLevel : save it')
    folderName = inputFolderNameEntry.get_enter_input()

    if folderName == '':  # folder name error
        messagebox.showerror(title='error',
                             message='invalid name')
        fileWindow.destroy()
        return

    kyDebugTk.outMsg(folderName)

    userChooseDir = askdirectory()  # choose directory path
    if userChooseDir is None:
        messagebox.showerror(title='error',
                             message='Didn\'t choose the folder')
        fileWindow.destroy()
        return

    # new save file path
    saveFilePath = os.path.join(userChooseDir, folderName)
    if os.path.exists(saveFilePath) == True:
        kyDebugTk.outMsg('same path')
        coverChoose = messagebox.askquestion(title='cover file',
                                             message=f'''
                                             There have same folder.
                                             Do you want to cover it ?
                                             Path: {saveFilePath}
                                             ''')
        if coverChoose == 'no':
            inputFolderNameEntry.clear_entry()
            return

    else:
        os.mkdir(saveFilePath)

    kyDebugTk.outMsg(saveFilePath + ' exists:' +  # DEBUG:
                     str(os.path.exists(saveFilePath)))

    # copy file
    try:
        shutil.copy2(src=funcFilePath,
                     dst=os.path.join(saveFilePath, 'func.png'))
    except Exception as e:
        kyDebugTk.outMsg(e)  # DEBUG:
        messagebox.showerror(title='error',
                             message=e)

    try:
        shutil.copy2(src=bodePolterFilePath,
                     dst=os.path.join(saveFilePath, 'bode.png'))
    except Exception as e:
        kyDebugTk.outMsg(e)  # DEBUG:
        messagebox.showerror(title='error',
                             message=e)

    with open(os.path.join(saveFilePath, 'bodeText.txt'), mode='w') as f:
        f.write(str(transFuncG))

    messagebox.showinfo(title='save file path',
                        message='Success\nSave in ' + saveFilePath)

    fileWindow.destroy()


def save_file() -> None:  # ask the file name  # save file
    kyDebugTk.outMsg('Save file')
    if haveRunBodePloter == True:
        global fileWindow
        fileWindow = Toplevel()
        global inputFolderNameEntry
        inputFolderNameEntry = kyEntry(frame=fileWindow,
                                       entryName='Input folder name:')

        enterSaveButton = Button(fileWindow,
                                 text='save',
                                 command=topLevel_com,
                                 width=8).pack()
        return

    else:
        messagebox.showerror(title='error',
                             message='Didn\'t Run the build Bode plot button')
        return


def clear() -> None:  # clear
    kyDebugTk.outMsg('clear all')  # DEBUG:

    GUI.bodePlotFuncOutputImageLabel.config(image='')
    GUI.answerFuncOutputImageLabel.config(image='')

    GUI.upperPloyEntry.clear_entry()
    GUI.lowerPloyEntry.clear_entry()

    set_haveRunBodePloter(False)


def display_png(FuncPath: str, BodePath: str) -> None:
    # function display
    funcPhoto = Image.open(FuncPath)
    funcPhotoConverted = ImageTk.PhotoImage(funcPhoto)
    GUI.answerFuncOutputImageLabel.configure(image=funcPhotoConverted)
    GUI.answerFuncOutputImageLabel.image = funcPhotoConverted

    # bodeplot display
    bodePhoto = Image.open(BodePath)
    bodePhotoConverted = ImageTk.PhotoImage(bodePhoto)
    GUI.bodePlotFuncOutputImageLabel.configure(image=bodePhotoConverted)
    GUI.bodePlotFuncOutputImageLabel.image = bodePhotoConverted

    kyDebugTk.outMsg('display photo')  # DEBUG:  # success


def run_bode_ploter() -> None:
    set_haveRunBodePloter(False)
    if GUI.upperPloyEntry.get_enter_input() == "" or GUI.lowerPloyEntry.get_enter_input() == "":
        outputString = 'No '

        if GUI.upperPloyEntry.get_enter_input() == '':
            outputString += 'Upper Poly '

        if GUI.lowerPloyEntry.get_enter_input() == '':
            outputString += 'Lower Poly '

        messagebox.showwarning(title='Warning',
                               message=outputString + 'input')

        kyDebugTk.outMsg(msg='No input')  # DEBUG:
        return

    else:
        upperPolyStr, lowerPolyStr = GUI.upperPloyEntry.get_enter_input(
        ), GUI.lowerPloyEntry.get_enter_input()

        upperPolyCoffsList, lowerPolyCoffsList = [], []

        # prase string to poly
        try:
            if upperPolyStr.isdigit():
                upperPolyCoffsList = [upperPolyStr]
            else:
                upperPoly = polys.polytools.\
                    poly_from_expr(upperPolyStr)[0]
                upperPolyCoffsList = upperPoly.all_coeffs()

        except Exception as e:
            kyDebugTk.outMsg(e)  # DEBUG:
            messagebox.showerror(title='error',
                                 message=e)

            return  # out of function

        try:
            if lowerPolyStr.isdigit():
                lowerPolyCoffsList = [lowerPolyStr]
            else:
                lowerPoly = polys.polytools.\
                    poly_from_expr(lowerPolyStr)[0]
                lowerPolyCoffsList = lowerPoly.all_coeffs()

        except Exception as e:
            kyDebugTk.outMsg(e)  # DEBUG:
            messagebox.showerror(title='error',
                                 message=e)

            return  # out of function

        # change to list

        # prase to list using float type
        upperPolyCoffsList = [float(i) for i in upperPolyCoffsList]
        lowerPolyCoffsList = [float(i) for i in lowerPolyCoffsList]

        kyDebugTk.outMsg(upperPolyCoffsList)  # DEBUG:
        kyDebugTk.outMsg(lowerPolyCoffsList)  # DEBUG:

        # make path
        absPath = os.path.abspath(os.path.curdir)
        global folderPath
        folderPath = os.path.join(absPath, 'tmp')

        # make folder
        if os.path.exists(folderPath) == False:
            os.mkdir(folderPath)

        global funcFilePath
        funcFilePath = os.path.join(folderPath, 'Func.png')

        kyDebugTk.outMsg(funcFilePath)  # DEBUG:

        # save function photo
        ld.to_latex_div_png(upperPolyList=upperPolyCoffsList,
                            lowerPolyList=lowerPolyCoffsList,
                            path=funcFilePath,
                            dpi=window_dpi)

        num, den = array(upperPolyCoffsList), array(lowerPolyCoffsList)

        global transFuncG  # for display

        try:
            transFuncG = tf(num, den)
        except Exception as e:
            kyDebugTk.outMsg(e)  # DEBUG:
            messagebox.showerror(title='error',
                                 message=e)
            return

        pole(transFuncG)
        zero(transFuncG)

        global mag, phase, omega
        mag, phase, omega = bode(transFuncG)

        global bodePolterFilePath
        bodePolterFilePath = os.path.join(folderPath, 'bode.png')
        savefig(bodePolterFilePath, dpi=window_dpi)
        close()

        set_haveRunBodePloter(True)
        # display function
        display_png(FuncPath=funcFilePath,
                    BodePath=bodePolterFilePath)


def clear_buffer() -> None:  # clear tmp
    kyDebugTk.outMsg('clear tmp')

    try:
        os.remove(funcFilePath)
        kyDebugTk.outMsg('remove func')

    except NameError:
        kyDebugTk.outMsg('not build func')

    try:
        os.remove(bodePolterFilePath)
        kyDebugTk.outMsg('remove bode')

    except NameError:
        kyDebugTk.outMsg('not build bode')

    try:
        os.rmdir(folderPath)
        kyDebugTk.outMsg('remove bode')

    except NameError:
        kyDebugTk.outMsg('not build folder')
