'''
Title:Bode plotter ultra 
written By KYLiN
This is Bode plotter ultra , This is a code of build the bode plot , It is a upgrade version of "bode plotter".
Date: 05/09/22
'''
import GUI
from ttkbootstrap import Window


def main() -> None:

    global window
    window = Window(themename='superhero')

    window.iconbitmap(default='icon\icon_92E_icon.ico')
    window.iconbitmap('icon\icon_92E_icon.ico')

    window.title('Bode Ploter Ultra(design By KYLiN)')

    GUI.init(window=window)
    window.mainloop()
    GUI.clear_buffer()


if __name__ == '__main__':
    main()
