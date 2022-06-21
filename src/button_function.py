# button function
#NOTE: GUI
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from ttkbootstrap import *
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
#NOTE: file
import os
import shutil
# NOTE: math and graph library
from sympy import polys
from numpy import array
from control.matlab import tf, pole, zero, bode
from matplotlib.pyplot import close, savefig, show
# NOTE: write by my self
import logging
from KY_Entry import kyEntry
import latex_div as ld
import GUI
from window_upgrade import get_ppi

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s',
                    level=logging.INFO)

global haveRunBodePlotter
haveRunBodePlotter = False

global window_dpi
window_dpi = get_ppi()

global saveClick
saveClick = False


def set_saveClick(TF: bool) -> None:
    global saveClick
    saveClick = TF


def set_haveRunBodePlotter(TF: bool) -> None:
    """_summary_
        setting some the var of RunBodePlotter
    Args:
        TF (bool): about the the true false value
    """

    global haveRunBodePlotter
    haveRunBodePlotter = TF


def open_bode_plot_detail() -> None:  # open bode plotter more pro
    logging.info('open bode plotter')
    # kyDebugTk.outMsg(msg='open bode plotter')  # DEBUG:
    if haveRunBodePlotter == True:
        mag, phase, omega = bode(transFuncG)
        show()
    else:
        messagebox.showerror(title='error',
                             message='Didn\'t Run the build Bode plot button')
        return


def topLevel_com() -> None:
    logging.info('ToLevel : save it')
    folderName = inputFolderNameEntry.get_enter_input()

    if folderName == '':  # folder name error
        messagebox.showerror(title='error', message='invalid name')

        fileWindow.destroy()
        set_saveClick(TF=False)
        return

    logging.info(folderName)

    userChooseDir = askdirectory()  # choose directory path
    if userChooseDir == '':
        messagebox.showerror(title='error',
                             message='Didn\'t choose the folder')

        fileWindow.destroy()
        set_saveClick(TF=False)
        return

    # new save file path
    saveFilePath = os.path.join(userChooseDir, folderName)

    okCancelChoose = messagebox.askokcancel(title='save path',
                                            message=f'''
                                    Is it correct 
                                    Path: {saveFilePath}
                                    ''')
    if okCancelChoose == False:
        logging.info('cancel save file')

        fileWindow.destroy()
        set_saveClick(TF=False)
        return

    if os.path.exists(saveFilePath) == True:
        logging.info('same path')
        coverChoose = messagebox.askquestion(title='cover file',
                                             message=f'''
                                                    There have same folder.
                                                    Do you want to cover it ?
                                                    Path: {saveFilePath}
                                                    ''')
        if coverChoose == 'no':
            inputFolderNameEntry.clear_entry()
            fileWindow.focus_force()
            return

    else:
        os.mkdir(saveFilePath)

    logging.info(saveFilePath + ' exists:' +  # DEBUG:
                 str(os.path.exists(saveFilePath)))

    # copy file
    try:
        shutil.copy2(src=funcFilePath,
                     dst=os.path.join(saveFilePath, 'func.png'))
    except Exception as e:
        logging.error(e)  # DEBUG:
        messagebox.showerror(title='error', message=e)

    try:
        shutil.copy2(src=bodePlotterFilePath,
                     dst=os.path.join(saveFilePath, 'bode.png'))
    except Exception as e:
        logging.error(e)  # DEBUG:
        messagebox.showerror(title='error', message=e)

    with open(os.path.join(saveFilePath, 'bodeText.txt'), mode='w') as f:
        f.write(str(transFuncG))

    messagebox.showinfo(title='save file path',
                        message='Success\nSave in ' + saveFilePath)

    fileWindow.destroy()
    set_saveClick(TF=False)


def save_file() -> None:
    """_summary_
        ask the file name 
        save file
    """

    logging.info('go to Save file')  # DEBUG:
    if haveRunBodePlotter == True:

        if saveClick == False:  # is not build it
            logging.info('Save file')  # DEBUG:
            set_saveClick(TF=True)

            global fileWindow
            fileWindow = Toplevel(title='save file')

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
    logging.info('clear all')  # DEBUG:

    GUI.bodePlotFuncOutputImageLabel.config(image='')
    GUI.answerFuncOutputImageLabel.config(image='')

    GUI.upperPloyEntry.clear_entry()
    GUI.lowerPloyEntry.clear_entry()

    set_haveRunBodePlotter(False)


def display_png(FuncPath: str, BodePath: str) -> None:
    # function display
    funcPhoto = Image.open(FuncPath)
    funcPhotoConverted = ImageTk.PhotoImage(funcPhoto)
    GUI.answerFuncOutputImageLabel.configure(image=funcPhotoConverted)
    GUI.answerFuncOutputImageLabel.image = funcPhotoConverted

    # bode plot display
    bodePhoto = Image.open(BodePath)
    bodePhotoConverted = ImageTk.PhotoImage(bodePhoto)
    GUI.bodePlotFuncOutputImageLabel.configure(image=bodePhotoConverted)
    GUI.bodePlotFuncOutputImageLabel.image = bodePhotoConverted

    logging.info('display photo')  # DEBUG:  # success


def run_bode_plotter() -> None:
    set_haveRunBodePlotter(False)
    if GUI.upperPloyEntry.get_enter_input() == ""\
        or GUI.lowerPloyEntry.get_enter_input() == "":

        outputString = 'No '

        if GUI.upperPloyEntry.get_enter_input() == '':
            outputString += 'Upper Poly '

        if GUI.lowerPloyEntry.get_enter_input() == '':
            outputString += 'Lower Poly '

        messagebox.showwarning(title='Warning', message=outputString + 'input')

        logging.warning('No input')  # DEBUG:
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
            logging.error(e)  # DEBUG:
            messagebox.showerror(title='error', message=e)

            return  # out of function

        try:
            if lowerPolyStr.isdigit():
                lowerPolyCoffsList = [lowerPolyStr]
            else:
                lowerPoly = polys.polytools.\
                    poly_from_expr(lowerPolyStr)[0]
                lowerPolyCoffsList = lowerPoly.all_coeffs()

        except Exception as e:
            logging.error(e)
            messagebox.showerror(title='error', message=e)

            return  # out of function

        # change to list

        # prase to list using float type
        upperPolyCoffsList = [float(i) for i in upperPolyCoffsList]
        lowerPolyCoffsList = [float(i) for i in lowerPolyCoffsList]

        logging.info(upperPolyCoffsList)  # DEBUG:
        logging.info(lowerPolyCoffsList)  # DEBUG:

        # make path
        absPath = os.path.abspath(os.path.curdir)
        global folderPath
        folderPath = os.path.join(absPath, 'tmp')

        # make folder
        if os.path.exists(folderPath) == False:
            os.mkdir(folderPath)

        global funcFilePath
        funcFilePath = os.path.join(folderPath, 'Func.png')

        logging.info(funcFilePath)  # DEBUG:

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
            logging.error(e)
            messagebox.showerror(title='error', message=e)
            return

        pole(transFuncG)
        zero(transFuncG)

        global mag, phase, omega
        mag, phase, omega = bode(transFuncG)

        global bodePlotterFilePath
        bodePlotterFilePath = os.path.join(folderPath, 'bode.png')
        savefig(bodePlotterFilePath, dpi=window_dpi)
        close()

        set_haveRunBodePlotter(True)
        # display function
        display_png(FuncPath=funcFilePath, BodePath=bodePlotterFilePath)


def clear_buffer() -> None:
    """_summary_
        clear tmp
    """
    logging.info('clear tmp')

    # check folder
    try:
        if os.path.exists(folderPath) == False:
            logging.warning('not build folder')
            return
    except NameError:
        logging.warning('not build folder')
        return

    # check the picture
    try:
        if os.path.exists(funcFilePath):
            os.remove(funcFilePath)
            logging.info('remove func')

    except NameError:
        logging.error('not build func')

    try:
        if os.path.exists(bodePlotterFilePath):
            os.remove(bodePlotterFilePath)
            logging.info('remove bode')

    except NameError:
        logging.error('not build bode')

    # remove folder
    os.rmdir(folderPath)
    logging.info('remove bode')
