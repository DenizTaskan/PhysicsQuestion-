import datetime
import math
import tkinter as tk
import random
import math

root = tk.Tk()
answer = ""

canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(250, 270, window=entry1)

correct_answer = 0

def generate_question():
    global correct_answer
    
    x = int(random.random()*100)
    t = "An apple is falling " +str(x) + " meters from the sky. \n How many seconds before it hits the ground? (g =10) \n Round to 2 decimal places"
    correct_answer = round(math.pow((x/5),0.5),2)
    
    label1 = tk.Label(root, text = t)
    canvas1.create_window(250, 200, window=label1)
    
    label2 = tk.Label(root, text =  answer)
    canvas1.create_window(250, 360, window=label2)
    
def check_answer():
    global answer
    
    Flag = len(entry1.get()) == 0
    if not Flag and float(correct_answer) == float(entry1.get()):
       answer = "Correct"
       entry1.delete(0, 'end')
       generate_question()
    elif not Flag:
        answer = "Wrong"          
        label2 = tk.Label(root, text =  answer)
        canvas1.create_window(250, 360, window=label2)
        
button1 = tk.Button(root, text = "Check", command = check_answer)
canvas1.create_window(250, 320, window=button1)

generate_question()    
    
root.mainloop()        