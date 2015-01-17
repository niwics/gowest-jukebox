#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Main application module
# @author: www.niwi.cz

import wx

from app import App
from main_frame import MainFrame


def main():
    """
    Main app function - initializes the WX GUI.
    :return: None (infinite WX loop)
    """

    # init app settings
    App.load_settings_from_db()

    # GUI
    app = wx.App()
    MainFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()
