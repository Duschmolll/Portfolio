import tkinter as tk
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc
from typing import Any
from typing_extensions import Literal


class Score(tk.Frame):
    def __init__(self) -> None:
        pass


class MainGui(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
