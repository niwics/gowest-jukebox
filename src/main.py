#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Main application module
# @author: www.niwi.cz

import wx

from main_frame import MainFrame


def main():
    """
    Main app function - initializes the WX GUI.
    :return: None (infinite WX loop)
    """

    app = wx.App()
    MainFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()
