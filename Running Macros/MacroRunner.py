# ------------------------ IMPORTS ---------------------------
import os
import datetime
import time
import pyautogui
import win32com.client as win32
import pandas

# ------------------------ FUNCTIONS ---------------------------
def run_macro(path, macro): # Creating the run_macro function to be used in future process
    xl = win32.DispatchEx("Excel.Application") # Create an instance of Excel
    xl.Visible = 1 # This makes excel visible to python
    book = xl.Workbooks.Open(Filename=path)
    xl.Run(macro) # This runs the macro requested in the second ""
    book.Save() # Save wb
    book.Close() # Close wb
    xl.Quit() # Quit excel instance


# mouse click
def click():
    pyautogui.click()


# move to specified x, y coordinate
def move(var1, var2, var3=0):
    pyautogui.moveTo(var1, var2, var3)


# pause for x amount of time (units: seconds)
def sleep(var1):
    time.sleep(var1)


# presses specified key(s) on keyboard
def key(var1, var2='', var3='', var4=''):
    pyautogui.hotkey(var1, var2, var3, var4)


# moves cursor to Tableau icon
def move_to_tableau():
    sleep(2)
    move(290, 750)
    sleep(2)
    click()
    sleep(20)

# ------------------------- PROCESS ----------------------------
# Enter file path in first "" and macro name in second "" below. Copy and repeat the "run_macro" function as needed.


run_macro(r"C:\Users\nicholas.jordan\Desktop\Python\Running Macros\test.xlsm", "test")
