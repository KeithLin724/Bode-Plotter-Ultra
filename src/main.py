'''
Title:Bode ploter ultra 
written By KYLiN
This is Bode ploter ultra , This is a code of build the bode plot , It is a upgrade version of "bode ploter".
Date: 05/09/22
'''
from tkinter import Tk

import GUI
from ttkbootstrap import Style as sl
from tkinter.ttk import *

from window_upgrade import window_scaler


def main() -> None:

    global window
    window = Tk()
    ScaleFactor = window_scaler()
    window.tk.call('tk', 'scaling', ScaleFactor/75)

    styleTheme = sl(theme='superhero')
    # styleTheme.theme('cosmo')
    #styleTheme = Style(theme='cosmo')
    #window = styleTheme.master

    window.title('Bode Ploter Ultra(design By KYLiN)')

    GUI.init(window=window)
    window.mainloop()
    GUI.clear_buffer()


if __name__ == '__main__':
    main()
