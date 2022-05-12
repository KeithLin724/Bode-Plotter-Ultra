'''
Title:Bode ploter ultra 
written By KYLiN
This is Bode ploter ultra , This is a code of build the bode plot , It is a upgrade version of "bode ploter".
Date: 05/09/22
'''
import GUI
from ttkbootstrap import Window


def main() -> None:

    global window
    window = Window(themename='superhero')

    window.title('Bode Ploter Ultra(design By KYLiN)')

    GUI.init(window=window)
    window.mainloop()
    GUI.clear_buffer()


if __name__ == '__main__':
    main()
