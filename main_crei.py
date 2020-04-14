import re
import math
import wx
import GUI

class monoFrame(GUI.MonoFrame):
    def __init__(self, parent):
        GUI.MonoFrame.__init__(self,parent)

    def afslut_monoFrame( self, event ):
        self.Hide()

class diffFrame(GUI.DiffFrame):
    def __init__(self, parent):
        GUI.DiffFrame.__init__(self, parent)

    def afslut_diffFrame( self, event ):
        self.Hide()

class mainFrame(GUI.MainFrame):
    def __init__(self, parent):
        GUI.MainFrame.__init__(self, parent)
        self.monoframe = monoFrame(self)
        self.diffFrame = diffFrame(self)

    def vis_monoFrame( self, event ):
        self.monoframe.Show()

    def vis_diffFrame( self, event ):
        self.diffFrame.Show()

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()