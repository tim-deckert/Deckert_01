import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

class cl_widgets:
    def __init__(self, ob_root_window, ob_world=[]):
        self.ob_root_window = ob_root_window
        self.ob_world = ob_world
        self.menu = cl_menu(self)
        self.toolbar = cl_toolbar(self)
        self.buttons_panel_01 = cl_buttons_panel_01(self)
        self.ob_canvas_frame = cl_canvas_frame(self)
        self.ob_world.add_canvas(self.ob_canvas_frame.canvas)


class cl_canvas_frame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master.ob_root_window, width=640, height=480, bg="yellow")
