# Deckert, Timothy
# 1000-637-406
# 2017-09-01
# Assignment_00_01

import tkinter as tk
import Deckert_01_02 as k02  # This module includes all the widgets
import Deckert_01_03 as k03  # This module includes graphic components


def close_window_callback(root):
    if tk.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

ob_root_window = tk.Tk()
ob_root_window.protocol("WM_DELETE_WINDOW", lambda root_window=ob_root_window: close_window_callback(root_window))
ob_world = k03.cl_world()
k02.cl_widgets(ob_root_window, ob_world)
ob_root_window.mainloop()
