import re
import math
import wx
import GUI


class MonoFrame(GUI.MonoFrame):
    def __init__(self, parent):
        GUI.MonoFrame.__init__(self,parent)
        self.fejlframe = FejlFrame(self)

    def Udregn( self, event ):
        self.integration()

    def Afslut( self, event ):
        pass



    def Analyse(self):
        try:
            #val = self.indsæt_mono.GetValue()
            val = "23x^4-e^x+365x-32+x"
            if val[0] == "y" and val[1] == "=":
                val = val[2:]

            polynomsplitter = "[=+-]"
            forskriftsplitter = "[^=+-]"
            koefficienter = "[^0-9]"

            x = re.split(polynomsplitter, val)
            y = re.split(forskriftsplitter, val)
            z = re.split(koefficienter, val)

            if val[2] != "-":
                y.insert(0, "+")

            x = list(filter(None, x))
            y = list(filter(None, y))
            z = list(filter(None, z))

            print("Analyseret: " + str(x) + " " + str(y) + " " + str(z))
            return x, y, z

        except:
            self.fejlframe.Show()

    def integration(self):
        val = self.Analyse()
        result = ""

        for i in range(0, len(val[1])):


        #print(result)

    def roots(self):
        val = self.Analyse()
        if val[1][0] == "=":
            a = "+" + val[2][0]
        else:
            a = "-" + val[2][0]
        print("a: " + str(a))
        b = val[1][1] + val[2][1]
        print("b: " + str(b))
        c = val[1][2] + val[2][2]
        print("c: " + str(c))

        D = int(b) ** 2 - 4 * int(a) * int(c)
        print("Diskriminanten: " + str(D))

        x1 = (-int(b) + math.sqrt(D)) / (2 * int(a))
        print("x1: " + str(x1))
        x2 = (-int(b) - math.sqrt(D)) / (2 * int(a))
        print("x2: " + str(x2))

        #return x1, x2

    def differentier(self):
        val = self.Analyse()
        result = ""
        for i in range(0, len(val[1])):
            forskrift = val[1][i]


            if "^" in val[0][i] and val[0][i][:1] != "e": #Eksponential-led
                x = int(val[2][i+i])
                n = int(val[2][i+i+1])
                if n != 2:
                    result += forskrift + str(n * x) + "x^" + str(n - 1)
                else:
                    result += forskrift + str(n * x) + "x"
                if MainFrame.debug: print("Debug | Eksponent: i = " + str(i) + ", x = " + str(x) + ", n = " + str(n) + ", Forskrift: " + forskrift)

            elif val[0][i][:-1].isdigit() and val[0][i][-1:] == "x": #Førstegrads-led
                k = val[0][i][:-1]
                result += forskrift + k
                if MainFrame.debug: print("Debug | Førstegrad: i = " + str(i) + ", k = " + str(k) + ", Forskrift: " + forskrift)

            elif val[0][i][:1] == "e" and val[0][i][-1:] == "x": #Euler-led
                x = "e^x"
                result += forskrift + x
                if MainFrame.debug: print("Debug | Euler: i = " + str(i), ", x = " + x)

            elif val[0][i] == "x": #X-led
                x = "1"
                result += forskrift + x
                if MainFrame.debug: print("Debug | X: i =" + str(i) + ", x = " + str(x) + "Forskrift: " + forskrift)

        print("Resultat: " + result)


    def afslut(self, event):
        self.Hide()

class FejlFrame(GUI.FejlFrame):
    def __init__(self, parent):
        GUI.FejlFrame.__init__(self, parent)


class DiffFrame(GUI.DiffFrame):
    def __init__(self, parent):
        GUI.DiffFrame.__init__(self, parent)
        self.tretrinsframe = TreTrinsFrame(self)

    def afslut( self, event ):
        self.Hide()

    def tretrinsregl( self, event ):
        self.tretrinsframe.Show()
        self.Hide()

    def afled_funktion( self, event ):
        self.Hide()


class TreTrinsFrame(GUI.TretrinFrame):
    def __init__(self, parent):
        GUI.TretrinFrame.__init__(self, parent)
        self.trin1frame = Trin1Frame(self)
        self.trin2frame = Trin2Frame(self)
        self.trin3frame = Trin3Frame(self)

    def afslut(self, event):
        self.Hide()

    def trin1(self, event):
        self.trin1frame.Show()

    def trin2(self, event):
        self.trin2frame.Show()

    def trin3(self, event):
        self.trin3frame.Show()


class Trin1Frame(GUI.Trin1Frame):
    def __init(self, parent):
        GUI.Trin1Frame.__init__(self, parent)


class Trin2Frame(GUI.Trin2Frame):
    def __init(self, parent):
        GUI.Trin2Frame.__init__(self, parent)


class Trin3Frame(GUI.Trin3Frame):
    def __init(self, parent):
        GUI.Trin3Frame.__init__(self, parent)


class IntFrame(GUI.IntFrame):
    def __init__(self, parent):
        GUI.IntFrame.__init__(self, parent)

    def afslut( self, event ):
        self.Hide()


class MainFrame(GUI.MainFrame):
    def __init__(self, parent):
        GUI.MainFrame.__init__(self, parent)
        self.monoframe = MonoFrame(self)
        self.diffFrame = DiffFrame(self)
        self.intframe = IntFrame(self)

    debug = True


    def vis_monoFrame( self, event ):
        self.monoframe.Show()

    def vis_diffFrame( self, event ):
        self.diffFrame.Show()

    def vis_intFrame( self, event ):
        self.intframe.Show()


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()