from typing import Callable
from tkinter import *


class kyDebugTk:

    def __init__(self, frame: Frame, valFunc: Callable) -> None:

        self.__targetValue = valFunc
        self.__deBugButton = Button(frame,
                                    text='debug',
                                    command=self.__func,
                                    bg='black', fg='red').pack(side=BOTTOM)

    def __outputFormatStr(self) -> str:
        tmpVal = self.__targetValue()
        return f'Type: {type(tmpVal)} debug Value : {tmpVal}'

    def __func(self) -> None:
        print(self.__outputFormatStr())

    def __str__(self) -> str:
        return f'type : kyDebugTk value:{self.__targetValue()}'

    def markValueFunc(self, changeValueFunc) -> None:
        self.__targetValue = changeValueFunc

    def outputDebug(self) -> None:
        print(self.__outputFormatStr())

    def outMsg(msg) -> None:
        print(f'---\ndebug msg: {msg}\n---')
