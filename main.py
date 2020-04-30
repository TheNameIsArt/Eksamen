import re
import wx
import GUI


class DiffFrame(GUI.DiffFrame):
    def __init__(self, parent):
        GUI.DiffFrame.__init__(self,parent)
        self.fejlframe = FejlFrame(self)

    def afslut(self, event):
        self.Hide()

    def udregn( self, event ):
        self.differentier()

    def vis_forside( self, event ):
        self.Hide()

    def vis_tre_trin( self, event ):
        self.tretrinsframe.Show()

    def Analyse(self):
        try:
            val = self.indsæt_mono.GetValue()
            #val = "23x^4-e^x+x+5/x+sqrt(32)+lg(60)"
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

    def differentier(self):
        try:
            val = self.Analyse()
            result = ""
            for i in range(0, len(val[0])):
                forskrift = val[1][i]
                x = val[2][i]

                if val[0][i][:-1].isdigit() and val[0][i][-1:] == "x": # Førstegrads-led
                    result += forskrift + x
                    if MainFrame.debug: print("Debug | Konstant    : i = " + str(i) + ", x = " + str(x) + ", n = " + ", Forskrift " + forskrift + ", Val[2]: " + str(val[2]))

                elif val[0][i][:1] == "e" and val[0][i][-1:] == "x": # Euler-led
                    val[2].insert(0, "0")
                    if MainFrame.debug: print("Debug | Euler     : i = " + str(i) + ", x = " + x + ", n = 0, Forskrift: " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + val[0][i]

                elif val[0][i] == "x": # X-led
                    val[2].insert(0, "0")
                    result += forskrift + "1"
                    if MainFrame.debug: print("Debug | X-led     : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift: " + forskrift + ", Val[2]: " + str(val[2]))

                elif "^" in val[0][i] and val[0][i][:1] != "e": # Eksponential-led
                    if val[0][i][0] == "x":
                        val[2].insert(0, "1")
                    x = int(val[2][i])
                    n = int(val[2][i+1])
                    val[2].remove(str(n))
                    if n != 2:
                        result += forskrift + str(n * x) + "x^" + str(n - 1)
                    else:
                        result += forskrift + str(n * x) + "x"
                    if MainFrame.debug: print("Debug | Eksponent : i = " + str(i) + ", x = " + str(x) + ", n = " + str(n) + ", Forskrift: " + forskrift + ", Val[2]: " + str(val[2]))

                elif "/" in val[0][i]: # Divisions-led
                    result += "-1/"+ x+"^2"
                    if MainFrame.debug: print("Debug | Division  : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift: " + forskrift + ", Val[2]: " + str(val[2]))

                elif "sqrt" in val[0][i]: #K vadratrodsled
                    result += forskrift + "1/√" + x
                    if MainFrame.debug: print("Debug | Kvadratrod: i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))

                elif "lg" in val[0][i] or "log" in val[0][i]: # Logoritmeled
                    result += forskrift + "1/" + x
                    if MainFrame.debug: print("Debug | Logoritme : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))

            if result[:1] == "+":
                result = result[1:]

            result = "y=" + result
            print("Resultat: " + result)
            self.result_indsæt.Append(result)

        except:
            self.fejlframe.Show()

class IntFrame(GUI.IntFrame):
    def __init__(self, parent):
        GUI.IntFrame.__init__(self, parent)
        self.fejlframe = FejlFrame(self)

    def udregn( self, event ):
        self.integrer()

    def afslut( self, event ):
        self.Hide()

    def Analyse(self):
        try:
            val = self.indsætInt.GetValue()
            #val = "2+x^8+4x^6-sin(7)+cos(9)-tan(2)+e^8+ln(5)-log(22)"
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

    def integrer(self):
        try:
            val = self.Analyse()
            result = ""
            for i in range(0, len(val[0])):
                forskrift = val[1][i]
                x = val[2][i]

                if val[0][i].isdigit(): # Konstant-led
                    x = val[0][i]
                    if MainFrame.debug: print("Debug | Konstant : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + x + "x"

                elif "^" in val[0][i] and val[0][i][:1] != "e" and val[0][i][:1] != "x": # Potens-led 1
                    n = int(val[2][i + 1])
                    val[2].remove(str(n))
                    if MainFrame.debug: print("Debug | Potens 1 : i = " + str(i) + ", x = " + str(x) + ", n = " + str(n) + ", Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + "(" + str(x) + "x^" + str(n+1) + ")/" + str(n+1)

                elif val[0][i][-1:] == "x": # Potens-led 2
                    if MainFrame.debug: print("Debug | Potens 2 : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + "(" + x + "x)/2"

                elif "^" in val[0][i] and val[0][i][1:] != "e" and val[0][i][:1] == "x": # Eksponent-led
                    n = int(val[2][i + 1])
                    if MainFrame.debug: print("Debug | Eksponent: i = " + str(i) + ", x = " + str(x) + ", n = " + str(n) + ", Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + "(x^" + str(n + 1) + ")/" + str(n + 1)

                elif "sin" in val[0][i]: # Sinus
                    if MainFrame.debug: print("Debug | Sinus    : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += "-cos(" + x + ")"

                elif "cos" in val[0][i]: # Cosinus
                    if MainFrame.debug: print("Debug | Cosinus  : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + "sin(" + x + ")"

                elif "tan" in val[0][i]: # Tangent
                    if MainFrame.debug: print("Debug | Tangent  : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += "-ln(cos(" + x + "))"

                elif val[0][i][:1] == "e": # Euler
                    if MainFrame.debug: print("Debug | Euler    : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + val[0][i]

                elif "ln" in val[0][i]: # Ln
                    if MainFrame.debug: print("Debug | Ln       : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + str(x) + "(ln(" + str(x) + "))-" + str(x)

                elif "log" in val[0][i]: # Log
                    if MainFrame.debug: print("Debug | Log      : i = " + str(i) + ", x = " + str(x) + ", n = 0, Forskrift " + forskrift + ", Val[2]: " + str(val[2]))
                    result += forskrift + str(x) + "(log(" + str(x) + "))-" + str(x) + "/ln(" + str(x) + ")"

            if result[:1] == "+":
                result = result[1:]

            result = "y=" + result + "+k"
            print("Resultat: " + result)
            self.resultatInt.Append(result)

        except:
            self.fejlframe.Show()


class FejlFrame(GUI.FejlFrame):
    def __init__(self, parent):
        GUI.FejlFrame.__init__(self, parent)

    def afslut( self, event ):
        self.Hide()


class MainFrame(GUI.MainFrame):
    def __init__(self, parent):
        GUI.MainFrame.__init__(self, parent)
        self.diffFrame = DiffFrame(self)
        self.intframe = IntFrame(self)

    debug = True

    def vis_diffFrame( self, event ):
        self.diffFrame.Show()

    def vis_intFrame( self, event ):
        self.intframe.Show()


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()