import math
import time
from tkinter import *
from tkinter import messagebox

import numpy as geek
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from phase_2 import precision


def g(x,exp):
    exp = exp.lower()

    exp = exp.replace('^', '**')
    exp = exp.replace('=x', '')
    exp = exp.replace('= x', '')
    exp = exp.replace('log', 'math.log10')

    exp = exp.replace('sin', 'math.sin')
    exp = exp.replace('cos', 'math.cos')
    exp = exp.replace('tan', 'math.tan')
    exp = exp.replace('sinh', 'math.sinh')
    exp = exp.replace('cosh', 'math.cosh')
    exp = exp.replace('tanh', 'math.tanh')

    exp = exp.replace('pi', 'math.pi')
    exp = exp.replace('e', 'math.e')
    return eval(exp)


def FixedPt(exp,x0, es, iter_max,top,pre):
    t1 = time.time()
    xp = []               #array to store estimated root in each step
    xr = x0                #Estimated root
    xp.append(xr)          #Keep xr from previous iteration
    iter = 0                #Keep track of # of iterations
    scrollbar = Scrollbar(top)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(top, yscrollcommand = scrollbar.set )
    mylist.insert(END,"Fixed Point :")
    while True:
        xr_old = xr
        xr = g(xr_old,exp)
        xr = precision.precision(xr,pre)
        xp.append(xr)
        ea = precision.precision(abs((xr - xr_old)),pre)
        iter += 1
        mylist.insert(END,"Iteration" + str(iter) +"\t,xi: " + str(xr))
        if (iter > 1):
            mylist.insert(END,"Approximation error: " + str(ea) + "")
            #res += "\nApproximation error: " + str(ea) + "\n"
            #print(" Approximation error: ", ea, "\n")
        if (ea <= es or iter >= iter_max or abs(xr) > (2 ** 31 - 1)):
            break
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"
    l9 = Label(top, text=element )
    l9.pack()
    ans = []
    for i in xp:
        z = g(i,exp)
        ans.append(z)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)
    x = geek.linspace(0, 5,100, endpoint=True)
    y = g(x,exp)
    plot1.plot(x, y, xp, ans, 'bo', x0, g(x0,exp), 'ro', xr, g(xr,exp), 'go', x, x, 'k')
    plot1.axhline(y=0, color = 'black')
    canvas = FigureCanvasTkAgg(fig,
                               master = top)

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   top)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    mylist.pack( side = BOTTOM,fill= BOTH)
    scrollbar.config( command = mylist.yview )
    if iter >= iter_max or abs(xr) > (2 ** 31 - 1):
        messagebox.showerror("No fixed point for given start value")
        top.destroy()









