#Imports
from guisetup import WindowMain, WindowDisplay

#Thanks to rdbende for Tkinter Theme
#https://github.com/rdbende/Sun-Valley-ttk-theme
import sv_ttk






#Initialization
Window = WindowMain()
sv_ttk.set_theme("dark")

WindowDisplay(Window)
Window.mainloop()