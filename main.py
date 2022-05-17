from tkinter import *
from tkinter import ttk
import random

from colors import *
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort

window = Tk()
window.title('Sorting algorithms visualization')
window.maxsize(1000, 700)
window.config(bg=WHITE)

algorithm_name = StringVar()
algorithm_list = ['Bubble Sort', 'Merge Sort']

speed_name = StringVar()
#This is for selecting algorithm speed
speed_list = ['Ultra Fast','Fast','Medium','Slow']

#Data array, every time it will be randomly generated.
data = []

#Will draw the data array on the canvas as vertical bars.
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width=800
    canvas_height=400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i/max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i*x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    window.update_idletasks()
#Will generate the data array with random values.
def generateData():
    global data
    data = []
    for i in range(0, 200):
        random_value = random.randint(1, 250)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))] )
#Sets the sorting speed.
def setSpeed():
    if speed_menu.get() == "Slow":
        return 0.3
    elif speed_menu.get() == "Medium":
        return 0.1
    elif speed_menu.get() == "Fast":
        return 0.001
    else:
        return 0.00001


#Triggers the selected algorithm.
#Starts the data sorting.
def sort():
    global data
    timeTick = setSpeed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data)-1, drawData, timeTick)

UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Dropdwon to select the sorting algorithm
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algorithm_list)
algo_menu.grid(row=0, column=0, padx=5, pady=5)
algo_menu.current(0)

#Dropdown to select sorting speed.
l2 = Label(UI_frame, text="Sorting speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#Sort button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

#Generate array button
b2 = Button(UI_frame, text="Generate array", command=generateData, bg=LIGHT_GRAY)
b2.grid(row=2, column=0, padx=5, pady=5)

#Canvas to draw the array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
