# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.Main_Title = wx.StaticText( self, wx.ID_ANY, u"FUNKTIONSREGNEREN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Main_Title.Wrap( -1 )

		self.Main_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Main_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Main_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical.Add( self.Main_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 0), 0, wx.EXPAND|wx.TOP, 5 )

		self.Discription_txt = wx.StaticText( self, wx.ID_ANY, u"Dette er et program som kan hjælpe dig med at udregne ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Discription_txt.Wrap( -1 )

		vertical.Add( self.Discription_txt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Discription_txt1 = wx.StaticText( self, wx.ID_ANY, u"forskellige matematiske funktioner. Den kan lave en monotoni ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Discription_txt1.Wrap( -1 )

		vertical.Add( self.Discription_txt1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Discription_txt2 = wx.StaticText( self, wx.ID_ANY, u"undersøgelse, lave differentialregning og integrationsregning.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Discription_txt2.Wrap( -1 )

		vertical.Add( self.Discription_txt2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Discription_txt3 = wx.StaticText( self, wx.ID_ANY, u"Den kan desuden laver en graf over din funktion.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Discription_txt3.Wrap( -1 )

		vertical.Add( self.Discription_txt3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 50), 0, wx.EXPAND|wx.TOP, 5 )

		horizontal = wx.BoxSizer( wx.HORIZONTAL )

		self.mono_butt = wx.Button( self, wx.ID_ANY, u"Monotoni", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.mono_butt, 0, wx.ALL, 5 )

		self.diff_butt = wx.Button( self, wx.ID_ANY, u"Differential", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.diff_butt, 0, wx.ALL, 5 )

		self.inte_butt = wx.Button( self, wx.ID_ANY, u"Integration", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.inte_butt, 0, wx.ALL, 5 )


		vertical.Add( horizontal, 0, wx.ALIGN_CENTER, 5 )


		self.SetSizer( vertical )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.mono_butt.Bind( wx.EVT_BUTTON, self.mono )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mono( self, event ):
		event.Skip()


###########################################################################
## Class MonoFrame
###########################################################################

class MonoFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,563 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.Mono_Title = wx.StaticText( self, wx.ID_ANY, u"MONOTONI UNDERSØGELSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Mono_Title.Wrap( -1 )

		self.Mono_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Mono_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Mono_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical.Add( self.Mono_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		grid = wx.GridSizer( 0, 2, 0, 0 )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.indsæt_mono = wx.TextCtrl( self, wx.ID_ANY, u"Indsæt din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		vertical.Add( self.indsæt_mono, 0, wx.ALL, 5 )

		self.afledte_mono = wx.StaticText( self, wx.ID_ANY, u"Afledte funktion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.afledte_mono.Wrap( -1 )

		vertical.Add( self.afledte_mono, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT, 5 )

		result_indsætChoices = []
		self.result_indsæt = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,50 ), result_indsætChoices, 0 )
		vertical.Add( self.result_indsæt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		grid.Add( vertical, 0, 0, 5 )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.rødder_txt = wx.StaticText( self, wx.ID_ANY, u"Rødderne:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rødder_txt.Wrap( -1 )

		vertical.Add( self.rødder_txt, 0, wx.ALL, 5 )

		rødderChoices = []
		self.rødder = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 255,100 ), rødderChoices, 0 )
		vertical.Add( self.rødder, 0, wx.ALL, 5 )


		grid.Add( vertical, 0, 0, 5 )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.vælg_txt = wx.StaticText( self, wx.ID_ANY, u"Vælg tal: f'(x)>0 og f'(x)<0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vælg_txt.Wrap( -1 )

		vertical.Add( self.vælg_txt, 0, wx.ALL, 5 )

		self.tal1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.tal1, 0, wx.ALL, 5 )

		self.tal2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.tal2, 0, wx.ALL, 5 )

		self.tal3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.tal3, 0, wx.ALL, 5 )


		grid.Add( vertical, 1, wx.EXPAND, 5 )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.result_tal = wx.StaticText( self, wx.ID_ANY, u"Resultat:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.result_tal.Wrap( -1 )

		vertical.Add( self.result_tal, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.m_textCtrl13, 0, wx.ALL, 5 )


		grid.Add( vertical, 1, wx.EXPAND, 5 )


		vertical.Add( grid, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.forside_butt, 0, wx.ALL, 5 )


		vertical.Add( bSizer43, 0, wx.EXPAND, 5 )


		self.SetSizer( vertical )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class DiffFrame
###########################################################################

class DiffFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.Diff_Title = wx.StaticText( self, wx.ID_ANY, u"DIFFERENTIALREGNING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Diff_Title.Wrap( -1 )

		self.Diff_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Diff_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Diff_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical.Add( self.Diff_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Her kan du få afledt din funktion, se beviset for tre-trin reglen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer21.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"og få udregnet differention af sum af 2 funktioner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		bSizer21.Add( self.m_staticText35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer21.Add( ( 0, 10), 0, wx.EXPAND, 5 )


		vertical.Add( bSizer21, 0, wx.ALIGN_CENTER, 5 )

		horizontal = wx.BoxSizer( wx.HORIZONTAL )

		self.afled_butt = wx.Button( self, wx.ID_ANY, u"Afled din funktion", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.afled_butt, 0, wx.ALL, 5 )

		self.tretrin_butt = wx.Button( self, wx.ID_ANY, u"Tre-trins reglen", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.tretrin_butt, 0, wx.ALL, 5 )


		vertical.Add( horizontal, 0, wx.ALIGN_CENTER, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )


		bSizer44.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( bSizer44, 0, wx.EXPAND, 5 )


		self.SetSizer( vertical )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class AfledDiffFrame
###########################################################################

class AfledDiffFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical1 = wx.BoxSizer( wx.VERTICAL )

		self.AdledDiff_Title = wx.StaticText( self, wx.ID_ANY, u"AFLED DIN FUNKTION ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AdledDiff_Title.Wrap( -1 )

		self.AdledDiff_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.AdledDiff_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.AdledDiff_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical1.Add( self.AdledDiff_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.AdledDiff_Title1 = wx.StaticText( self, wx.ID_ANY, u"(DIFFERENTION)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AdledDiff_Title1.Wrap( -1 )

		self.AdledDiff_Title1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.AdledDiff_Title1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.AdledDiff_Title1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical1.Add( self.AdledDiff_Title1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical1.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		vertical2 = wx.BoxSizer( wx.VERTICAL )

		self.indsætDiff = wx.TextCtrl( self, wx.ID_ANY, u"Indsæt din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		vertical2.Add( self.indsætDiff, 0, wx.ALL, 5 )


		vertical1.Add( vertical2, 0, wx.ALIGN_CENTER, 5 )

		vertical = wx.BoxSizer( wx.VERTICAL )


		vertical.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.ijuhbygh7u = wx.StaticText( self, wx.ID_ANY, u"Din afledte funktion er:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ijuhbygh7u.Wrap( -1 )

		vertical.Add( self.ijuhbygh7u, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		resultatDiffChoices = []
		self.resultatDiff = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,50 ), resultatDiffChoices, 0 )
		vertical.Add( self.resultatDiff, 0, wx.ALL, 5 )


		vertical1.Add( vertical, 0, wx.ALIGN_CENTER, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )


		bSizer74.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer74.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical1.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( vertical1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TretrinFrame
###########################################################################

class TretrinFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.Tretrin_Title = wx.StaticText( self, wx.ID_ANY, u"TRE-TRINS REGLEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tretrin_Title.Wrap( -1 )

		self.Tretrin_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Tretrin_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Tretrin_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer18.Add( self.Tretrin_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer18.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"Tre-trins reglen er en metode for hvordan man differentierer ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		bSizer59.Add( self.m_staticText80, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"funktioner. Her kan du se beviset for det opdelt i de enkelte trin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer59.Add( self.m_staticText81, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer59.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		bSizer18.Add( bSizer59, 0, wx.EXPAND, 5 )

		horizontal = wx.BoxSizer( wx.HORIZONTAL )

		self.t1_butt = wx.Button( self, wx.ID_ANY, u"TRIN 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.t1_butt, 0, wx.ALL, 5 )

		self.t2_butt = wx.Button( self, wx.ID_ANY, u"TRIN 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.t2_butt, 0, wx.ALL, 5 )

		self.t3_butt = wx.Button( self, wx.ID_ANY, u"TRIN 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		horizontal.Add( self.t3_butt, 0, wx.ALL, 5 )


		bSizer18.Add( horizontal, 0, wx.ALIGN_CENTER, 5 )

		bSizer76 = wx.BoxSizer( wx.VERTICAL )


		bSizer76.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76.Add( self.forside_butt, 0, wx.ALL, 5 )


		bSizer18.Add( bSizer76, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Trin1Frame
###########################################################################

class Trin1Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		horizontal = wx.BoxSizer( wx.VERTICAL )

		self.Tretrin_Title = wx.StaticText( self, wx.ID_ANY, u"TRE-TRINS REGLEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tretrin_Title.Wrap( -1 )

		self.Tretrin_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Tretrin_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Tretrin_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		horizontal.Add( self.Tretrin_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		horizontal.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.t1 = wx.StaticText( self, wx.ID_ANY, u"TRIN 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t1.Wrap( -1 )

		self.t1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer24.Add( self.t1, 0, wx.ALL, 5 )


		bSizer24.Add( ( 50, 0), 0, wx.EXPAND, 5 )

		self.ko = wx.StaticText( self, wx.ID_ANY, u"f(x) = x^2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ko.Wrap( -1 )

		bSizer24.Add( self.ko, 0, wx.ALL, 5 )


		bSizer24.Add( ( 50, 0), 0, wx.EXPAND, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"f'(x) = delta y / delta x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		bSizer24.Add( self.m_staticText37, 0, wx.ALL, 5 )


		horizontal.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"f(x_0) = x_0^2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer20.Add( self.m_staticText22, 0, wx.ALL, 5 )


		bSizer20.Add( ( 50, 0), 0, wx.EXPAND, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"f(x_0 + delta x) = (x_0 + delta x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer20.Add( self.m_staticText23, 0, wx.ALL, 5 )


		horizontal.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Hældning = Differenskvotienten:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer21.Add( self.m_staticText24, 0, wx.ALL, 5 )


		horizontal.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"delta f(x) / delta x = (f(x_0 + delta x) - f(x_0)) / delta x = ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer22.Add( self.m_staticText25, 0, wx.ALL, 5 )


		horizontal.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"((x_0 + delta x)^2 -(x_0)^2) / delta x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer241.Add( self.m_staticText28, 0, wx.ALL, 5 )


		horizontal.Add( bSizer241, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )


		bSizer25.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"TRIN 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button10, 0, wx.ALL, 5 )


		horizontal.Add( bSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( horizontal )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Trin2Frame
###########################################################################

class Trin2Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.Tretrin_Title = wx.StaticText( self, wx.ID_ANY, u"TRE-TRINS REGLEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tretrin_Title.Wrap( -1 )

		self.Tretrin_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Tretrin_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Tretrin_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer26.Add( self.Tretrin_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer26.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.t2 = wx.StaticText( self, wx.ID_ANY, u"Trin 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t2.Wrap( -1 )

		self.t2.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer27.Add( self.t2, 0, wx.ALL, 5 )


		bSizer27.Add( ( 50, 0), 0, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Reducering af differenskvotienten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer27.Add( self.m_staticText34, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Første kvadratsætning:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )

		bSizer28.Add( self.m_staticText35, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer28, 0, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"(x_0^2 + delta x^2 + 2x_0 * delta x - x_0^2) / delta x   -->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer29.Add( self.m_staticText36, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"(dela x^2 + 2x_0 * delta x) / delat x   -->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		bSizer30.Add( self.m_staticText37, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer30, 0, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Fælles faktor udenfor parantes: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )

		bSizer31.Add( self.m_staticText38, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer31, 0, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"(dela x (delta x + 2x_0)) / delta x = delta x + 2x_0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer32.Add( self.m_staticText40, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer32, 0, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )


		bSizer35.Add( ( 0, 20), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"TRIN 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer35, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Trin3Frame
###########################################################################

class Trin3Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.Tretrin_Title = wx.StaticText( self, wx.ID_ANY, u"TRE-TRINS REGLEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tretrin_Title.Wrap( -1 )

		self.Tretrin_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Tretrin_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Tretrin_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer33.Add( self.Tretrin_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer33.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Trin 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer34.Add( self.m_staticText44, 0, wx.ALL, 5 )


		bSizer34.Add( ( 50, 0), 0, wx.EXPAND, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Bestemmer differentialkvotienten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		bSizer34.Add( self.m_staticText45, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer34, 0, wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"lim  delta x --> 0 (delta x + 2x_0) = 2x_0   Fordi delta x = 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		bSizer37.Add( self.m_staticText47, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer37, 0, wx.EXPAND, 5 )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )


		bSizer39.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Afledende funktion: f'(x) = 2x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer39.Add( self.m_staticText58, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer39, 0, wx.EXPAND, 5 )

		bSizer391 = wx.BoxSizer( wx.VERTICAL )


		bSizer391.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_staticText581 = wx.StaticText( self, wx.ID_ANY, u"Differentialkvotienten: f'(x) = 2x_0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )

		bSizer391.Add( self.m_staticText581, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer391, 1, wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.forside_butt, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer75, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class IntFrame
###########################################################################

class IntFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,517 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )

		self.Inte_Title = wx.StaticText( self, wx.ID_ANY, u"INTEGRATIONSREGNING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Inte_Title.Wrap( -1 )

		self.Inte_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Inte_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Inte_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical.Add( self.Inte_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Her kan du få afledt din funktion, få udregnet din funktion ved ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer21.Add( self.m_staticText34, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"hjælp af kædereglen og få beregner integration ved substitution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		bSizer21.Add( self.m_staticText35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer21.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		vertical.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Afled din funktion", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer53.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Kædereglen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer53.Add( self.m_button16, 0, wx.ALL, 5 )


		vertical.Add( bSizer53, 0, wx.ALIGN_CENTER, 5 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Integration ved substitution (ubestemt integral)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button17, 0, wx.ALL, 5 )


		vertical.Add( bSizer58, 0, wx.ALIGN_CENTER, 5 )

		bSizer78 = wx.BoxSizer( wx.VERTICAL )

		self.m_button171 = wx.Button( self, wx.ID_ANY, u"Integration ved substitution (bestemt integral)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.m_button171, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( bSizer78, 1, wx.EXPAND, 5 )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )


		bSizer77.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( bSizer77, 1, wx.EXPAND, 5 )


		self.SetSizer( vertical )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class AfledIntFrame
###########################################################################

class AfledIntFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical1 = wx.BoxSizer( wx.VERTICAL )

		self.AdledInt_Title = wx.StaticText( self, wx.ID_ANY, u"AFLED DIN FUNKTION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AdledInt_Title.Wrap( -1 )

		self.AdledInt_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.AdledInt_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.AdledInt_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical1.Add( self.AdledInt_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.AdledInt_Title1 = wx.StaticText( self, wx.ID_ANY, u"(INTEGRATION)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AdledInt_Title1.Wrap( -1 )

		self.AdledInt_Title1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.AdledInt_Title1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.AdledInt_Title1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical1.Add( self.AdledInt_Title1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical1.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		vertical2 = wx.BoxSizer( wx.VERTICAL )

		self.indsætInt = wx.TextCtrl( self, wx.ID_ANY, u"Indsæt din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		vertical2.Add( self.indsætInt, 0, wx.ALL, 5 )


		vertical1.Add( vertical2, 0, wx.ALIGN_CENTER, 5 )

		vertical = wx.BoxSizer( wx.VERTICAL )


		vertical.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.okjinhuj80unih = wx.StaticText( self, wx.ID_ANY, u"Din afledte funktion er:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.okjinhuj80unih.Wrap( -1 )

		vertical.Add( self.okjinhuj80unih, 0, wx.ALL, 5 )

		resultatIntChoices = []
		self.resultatInt = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,50 ), resultatIntChoices, 0 )
		vertical.Add( self.resultatInt, 0, wx.ALL, 5 )


		vertical1.Add( vertical, 0, wx.ALIGN_CENTER, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )


		bSizer74.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer74.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical1.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( vertical1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class KædeFrame
###########################################################################

class KædeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer66 = wx.BoxSizer( wx.VERTICAL )

		self.Kæde_Title = wx.StaticText( self, wx.ID_ANY, u"KÆDEREGLEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Kæde_Title.Wrap( -1 )

		self.Kæde_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Kæde_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Kæde_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer66.Add( self.Kæde_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer66.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, u"Indtast din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		bSizer67.Add( self.m_textCtrl17, 0, wx.ALL, 5 )


		bSizer67.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		bSizer66.Add( bSizer67, 0, wx.ALIGN_CENTER, 5 )

		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"f(t) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		bSizer68.Add( self.m_staticText98, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer68.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"f'(t) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		bSizer68.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		bSizer66.Add( bSizer68, 0, wx.ALIGN_CENTER, 5 )

		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText981 = wx.StaticText( self, wx.ID_ANY, u"t(x) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText981.Wrap( -1 )

		bSizer681.Add( self.m_staticText981, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer681.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer681.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		self.m_staticText991 = wx.StaticText( self, wx.ID_ANY, u"t'(x) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText991.Wrap( -1 )

		bSizer681.Add( self.m_staticText991, 0, wx.ALL, 5 )

		self.m_textCtrl191 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer681.Add( self.m_textCtrl191, 0, wx.ALL, 5 )


		bSizer66.Add( bSizer681, 0, wx.ALIGN_CENTER, 5 )

		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText105 = wx.StaticText( self, wx.ID_ANY, u"h'(x) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )

		bSizer72.Add( self.m_staticText105, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer72.Add( self.m_textCtrl25, 0, wx.ALL, 5 )


		bSizer66.Add( bSizer72, 0, wx.ALIGN_CENTER, 5 )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )


		bSizer73.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer66.Add( bSizer73, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer66 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class SubUbFrame
###########################################################################

class SubUbFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,478 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.SubUb_Title = wx.StaticText( self, wx.ID_ANY, u"INTEGRATION VED SUBSTITUTION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubUb_Title.Wrap( -1 )

		self.SubUb_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.SubUb_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SubUb_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer79.Add( self.SubUb_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.SubUb_Title1 = wx.StaticText( self, wx.ID_ANY, u"(UBESTEMT INTEGRAL)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubUb_Title1.Wrap( -1 )

		self.SubUb_Title1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.SubUb_Title1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SubUb_Title1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer79.Add( self.SubUb_Title1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer79.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, u"Indtast din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		bSizer67.Add( self.m_textCtrl17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer67.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		bSizer79.Add( bSizer67, 0, wx.EXPAND, 5 )

		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"t =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		bSizer68.Add( self.m_staticText98, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer68.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"t' =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		bSizer68.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer68, 0, wx.ALIGN_CENTER, 5 )

		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText981 = wx.StaticText( self, wx.ID_ANY, u"dt/dx =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText981.Wrap( -1 )

		bSizer681.Add( self.m_staticText981, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer681.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer681, 0, wx.ALIGN_CENTER, 5 )

		bSizer6811 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9811 = wx.StaticText( self, wx.ID_ANY, u"Resultat =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9811.Wrap( -1 )

		bSizer6811.Add( self.m_staticText9811, 0, wx.ALL, 5 )

		self.m_textCtrl1811 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer6811.Add( self.m_textCtrl1811, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer6811, 0, wx.ALIGN_CENTER, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )


		bSizer74.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer74.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer79.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer79 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class SubBFrame
###########################################################################

class SubBFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,538 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.SubB_Title = wx.StaticText( self, wx.ID_ANY, u"INTEGRATION VED SUBSTITUTION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubB_Title.Wrap( -1 )

		self.SubB_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.SubB_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SubB_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer79.Add( self.SubB_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.SubB_Title1 = wx.StaticText( self, wx.ID_ANY, u"(BESTEMT INTEGRAL)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubB_Title1.Wrap( -1 )

		self.SubB_Title1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.SubB_Title1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SubB_Title1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer79.Add( self.SubB_Title1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer79.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, u"Indtast din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		bSizer67.Add( self.m_textCtrl17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer67.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		bSizer79.Add( bSizer67, 0, wx.EXPAND, 5 )

		bSizer682 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText982 = wx.StaticText( self, wx.ID_ANY, u"a =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText982.Wrap( -1 )

		bSizer682.Add( self.m_staticText982, 0, wx.ALL, 5 )

		self.m_textCtrl182 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer682.Add( self.m_textCtrl182, 0, wx.ALL, 5 )


		bSizer682.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		self.m_staticText991 = wx.StaticText( self, wx.ID_ANY, u"b =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText991.Wrap( -1 )

		bSizer682.Add( self.m_staticText991, 0, wx.ALL, 5 )

		self.m_textCtrl191 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer682.Add( self.m_textCtrl191, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer682, 0, wx.ALIGN_CENTER, 5 )

		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"t =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		bSizer68.Add( self.m_staticText98, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer68.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"t' =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		bSizer68.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer68, 0, wx.ALIGN_CENTER, 5 )

		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText981 = wx.StaticText( self, wx.ID_ANY, u"dt/dx =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText981.Wrap( -1 )

		bSizer681.Add( self.m_staticText981, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer681.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer681, 0, wx.ALIGN_CENTER, 5 )

		bSizer6811 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9811 = wx.StaticText( self, wx.ID_ANY, u"Resultat =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9811.Wrap( -1 )

		bSizer6811.Add( self.m_staticText9811, 0, wx.ALL, 5 )

		self.m_textCtrl1811 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer6811.Add( self.m_textCtrl1811, 0, wx.ALL, 5 )


		bSizer79.Add( bSizer6811, 0, wx.ALIGN_CENTER, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )


		bSizer74.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.forside_butt = wx.Button( self, wx.ID_ANY, u"Forside", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer74.Add( self.forside_butt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer79.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer79 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


