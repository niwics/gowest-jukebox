# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Main GUI Frame
# @author: www.niwi.cz

import wx

from settings_dialog import SettingsDialog

APP_NAME = "GoWest Jukebox"

APP_SETTINGS = 1
APP_EXIT = 2


class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        """
        Init GUI
        :param args:
        :param kwargs:
        :return: None
        """
        super(MainFrame, self).__init__(None)

        self.init_ui()

    def init_ui(self):
        """
        Initializes the window GUI.
        :return:
        """
        menu_bar = wx.MenuBar()
        app_menu = wx.Menu()

        # menu items
        settings_item = wx.MenuItem(app_menu, APP_SETTINGS, '&Settings\tCtrl+S')
        settings_item.SetBitmap(wx.Bitmap('cog.png'))
        app_menu.AppendItem(settings_item)

        quit_item = app_menu.Append(APP_EXIT, 'Quit', 'Quit')
        quit_item.SetBitmap(wx.Bitmap('door_out.png'))

        menu_bar.Append(app_menu, '&Application')
        self.SetMenuBar(menu_bar)

        # menu actions
        self.Bind(wx.EVT_MENU, self.display_settings_action, id=APP_SETTINGS)
        self.Bind(wx.EVT_MENU, self.quit_action, id=APP_EXIT)

        #self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL) #TODO show fullscreen
        self.SetTitle(APP_NAME)
        self.Centre()
        self.Show(True)

    def display_settings_action(self, e):
        """
        Action handler for displaying the settings dialog.
        :param e:
        :return: None
        """
        dialog = SettingsDialog(None)
        dialog.ShowModal()
        dialog.Destroy()

    def quit_action(self, e):
        """
        Action handler for exiting the application.
        :param e:
        :return: None
        """
        self.Close()