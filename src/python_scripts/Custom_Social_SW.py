import os
import time
import tkinter as tk
from tkinter import messagebox
from robodk.robolink import *
from robodk.robomath import *

# Define relative path to the .rdk file
relative_path = "src/roboDK/Custom_Social_Task.rdk"
absolute_path = os.path.abspath(relative_path)

# Start RoboDK with the project file
RDK = Robolink()
RDK.AddFile(absolute_path)

# ----
# Crear al robodk les posicions i moviments
# crear en python els items creats a robodk (com està a baix)

# Retrieve items from the RoboDK station
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item("Hand")
Init_target = RDK.Item("Init")
Hello_start_target = RDK.Item("Hello start")
Hello_left_target = RDK.Item("Hello left")
Hello_right_target = RDK.Item("Hello right")
Bye_start_target = RDK.Item("Bye start")
Bye_left_target = RDK.Item("Bye left")
Bye_right_target = RDK.Item("Bye right")

# Set robot frame, tool and speed
robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(20)

# ----
# Aquesta funció mou el robot a la posició inicial i hauria de ser la mateixa pel nostre cas
# Move to initial position
def move_to_init():
    print("Init")
    robot.MoveL(Init_target, True)
    print("Init_target REACHED")

# ----
# Modificar les funcions per a que facin el que volem
# Perform house sequence
def hello():
    print("Hello!")
    robot.MoveL(Hello_start_target, True)
    for i in range(2):
        robot.MoveL(Hello_left_target, True)
        robot.MoveL(Hello_right_target, True)
    print("Hello FINISHED")

def bye():
    print("Bye!")
    robot.MoveL(Bye_start_target, True)
    for i in range(2):
        robot.MoveL(Bye_left_target, True)
        robot.MoveL(Bye_right_target, True)
    print("Bye FINISHED")

# ----
# Mencionar les diferents funcions que volem que faci el robot
# Main sequence
def main():
    move_to_init()
    hello()
    move_to_init()
    print("Program completed.")
    bye()
    move_to_init()
    print("Program completed.")
    

# Confirmation dialog to close RoboDK
def confirm_close():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askquestion(
        "Close RoboDK",
        "Do you want to save changes before closing RoboDK?",
        icon='question'
    )
    if response == 'yes':
        RDK.Save()
        RDK.CloseRoboDK()
        print("RoboDK saved and closed.")
    else:
        RDK.CloseRoboDK()
        print("RoboDK closed without saving.")

# Run main and handle closing
if __name__ == "__main__":
    main()
    #confirm_close()
