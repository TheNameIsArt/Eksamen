import re
import math
import wx
import GUI

class mainFrame(GUI.MainFrame):
    def __init__(self, parent):
        GUI.MainFrame.__init__(self, parent)
        self.monoframe = monoframe
        monoframe.Show(self)

def format(val):
    polynomsplitter = "[=+-]"
    forskriftsplitter = "[^=+-]"
    koefficienter = "[^0-9]"

    x = re.split(polynomsplitter, val)
    y = re.split(forskriftsplitter, val)
    z = re.split(koefficienter, val)

    x = list(filter(None, x))
    y = list(filter(None, y))
    z = list(filter(None, z))
    #print(x, y, z)
    return x, y, z


def roots(x):
    val = format(x)
    a = val[2][0]
    b = val[1][1] + val[2][1]
    c = val[1][2] + val[2][2]


    D = int(b)**2-4*int(a)*int(c)
    x1 = (-int(b)+math.sqrt(D))/(2*int(a))
    x2 = (-int(b)-math.sqrt(D))/(2*int(a))
    return x1, x2

def differentier(val):
    val = format(val)
    result = []
    for i in range(1, len(val[2])):
        #print("før " + val[0][i])

        if val[0][i].isdigit():
            result.append(0)

        if val[0][i] == "x":
            result.append(1)

        if len(val[0][i]) == 2:
            if val[0][i][0].isdigit() and val[0][i][1] == x:
                result.append(val[0][i][0])

        print(val[0][i])
        print(result)
        #if val[0][i]

        #print("efter" + str(result))
        #print(val[0][i][0])




#print(roots("y=3x^2+3x-3"))

differentier("y=3x^3+2x^2-x-3")

class monoframe(GUI.MonoFrame):
    def __init__(self, parent):
        GUI.MonoFrame.__init__(self, parent)

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()