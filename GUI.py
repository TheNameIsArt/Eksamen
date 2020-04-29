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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,462 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )


		vertical.Add( ( 0, 30), 0, wx.EXPAND, 5 )

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


		self.SetSizer( vertical )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.vælg_menu = wx.Menu()
		self.diff_menuItem = wx.MenuItem( self.vælg_menu, wx.ID_ANY, u"Differentialregning", wx.EmptyString, wx.ITEM_NORMAL )
		self.vælg_menu.Append( self.diff_menuItem )

		self.int_menuItem = wx.MenuItem( self.vælg_menu, wx.ID_ANY, u"Integrationsregning", wx.EmptyString, wx.ITEM_NORMAL )
		self.vælg_menu.Append( self.int_menuItem )

		self.m_menubar2.Append( self.vælg_menu, u"Vælg funktion" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.vis_diffFrame, id = self.diff_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.vis_intFrame, id = self.int_menuItem.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def vis_diffFrame( self, event ):
		event.Skip()

	def vis_intFrame( self, event ):
		event.Skip()


###########################################################################
## Class DiffFrame
###########################################################################

class DiffFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 741,563 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		vertical = wx.BoxSizer( wx.VERTICAL )


		vertical.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.Mono_Title = wx.StaticText( self, wx.ID_ANY, u"DIFFERENTIALREGNING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Mono_Title.Wrap( -1 )

		self.Mono_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Times New Roman" ) )
		self.Mono_Title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Mono_Title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		vertical.Add( self.Mono_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		vertical.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		vertical1 = wx.BoxSizer( wx.VERTICAL )

		self.indsæt_mono = wx.TextCtrl( self, wx.ID_ANY, u"Indsæt din funktion her", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		vertical1.Add( self.indsæt_mono, 0, wx.ALL, 5 )

		self.afledte_mono = wx.StaticText( self, wx.ID_ANY, u"Afledte funktion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.afledte_mono.Wrap( -1 )

		vertical1.Add( self.afledte_mono, 0, wx.ALIGN_CENTER|wx.ALL|wx.LEFT, 5 )

		result_indsætChoices = []
		self.result_indsæt = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,50 ), result_indsætChoices, 0 )
		vertical1.Add( self.result_indsæt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer71.Add( vertical1, 0, 0, 5 )


		vertical.Add( bSizer71, 1, 0, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Udregn", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button71 = wx.Button( self, wx.ID_ANY, u"3 Trins Reglen", wx.DefaultPosition, wx.DefaultSize, 0 )
		vertical.Add( self.m_button71, 0, wx.ALL, 5 )


		self.SetSizer( vertical )
		self.Layout()
		self.m_menubar5 = wx.MenuBar( 0 )
		self.mono_menu = wx.Menu()
		self.forside_menuItem = wx.MenuItem( self.mono_menu, wx.ID_ANY, u"Forside", wx.EmptyString, wx.ITEM_NORMAL )
		self.mono_menu.Append( self.forside_menuItem )

		self.m_menubar5.Append( self.mono_menu, u"Vælg funktion" )

		self.SetMenuBar( self.m_menubar5 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.udregn )
		self.m_button71.Bind( wx.EVT_BUTTON, self.vis_tre_trin )
		self.Bind( wx.EVT_MENU, self.vis_forside, id = self.forside_menuItem.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def udregn( self, event ):
		event.Skip()

	def vis_tre_trin( self, event ):
		event.Skip()

	def vis_forside( self, event ):
		event.Skip()


###########################################################################
## Class IntFrame
###########################################################################

class IntFrame ( wx.Frame ):

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

		vertical.Add( self.okjinhuj80unih, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		resultatIntChoices = []
		self.resultatInt = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,50 ), resultatIntChoices, 0 )
		vertical.Add( self.resultatInt, 0, wx.ALL, 5 )


		vertical1.Add( vertical, 0, wx.ALIGN_CENTER, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )


		vertical1.Add( bSizer74, 1, wx.EXPAND, 5 )


		self.SetSizer( vertical1 )
		self.Layout()
		self.m_menubar5 = wx.MenuBar( 0 )
		self.afledInt_menu = wx.Menu()
		self.forside_menuItem = wx.MenuItem( self.afledInt_menu, wx.ID_ANY, u"Forside", wx.EmptyString, wx.ITEM_NORMAL )
		self.afledInt_menu.Append( self.forside_menuItem )

		self.m_menubar5.Append( self.afledInt_menu, u"Vælg funktion" )

		self.SetMenuBar( self.m_menubar5 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FejlFrame
###########################################################################

class FejlFrame ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 304,118 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )


		bSizer62.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Error 404 (Invalid Input)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		bSizer62.Add( self.m_staticText69, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Okay", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer62.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer61.Add( bSizer62, 1, wx.EXPAND, 5 )


		bSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer61 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.afslut )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def afslut( self, event ):
		event.Skip()


