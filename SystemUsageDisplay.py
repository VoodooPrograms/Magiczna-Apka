from SystemVolume import show_mixer
from SystemUsage import show_host_data

from tkinter import Label, font, Frame
import time


def init_system_usage_gui(frame):

    # testowe wywołanie
    # todo usunąć testowe wywołanie
    text = set_data_usage(show_host_data())
        

    title = Label(frame, text="System usage", font=font.Font(size=20))
    title.grid(column=0, row=0)

    usage_frame = Frame(frame)
    usage_frame.grid(column=0, row=1)
    screen = Label(usage_frame, text=text ,font=10, width=40, height=2, bg="#0b8615")
    screen.grid(column=1, row=0)
    usage_frame.grid_columnconfigure(1, minsize=40)

    

def set_data_usage(dic):
    text ="Cpu: "
    text += str(dic['cpu']) + "%"
    text += " Temperature: "
    text += str(dic['temperature']) + '\N{DEGREE SIGN}C'
    text += " Memory "
    text += str(dic['memory']) + "%"
    return text

