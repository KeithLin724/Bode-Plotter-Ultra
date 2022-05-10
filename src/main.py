'''
Title:Bode ploter ultra 
written By KYLiN
This is Bode ploter ultra , This is a code of build the bode plot , It is a upgrade version of "bode ploter".
Date: 05/09/22
'''
from tkinter import Tk
import GUI


def main() -> None:
    global window
    window = Tk()
    window.title('Bode Ploter Ultra(design By KYLiN)')

    GUI.init(window=window)
    window.mainloop()


if __name__ == '__main__':
    main()
