# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 10.12.2018 """
import gi
gi.require_version('Gdk', '3.0')
from jira.extension import JiraExtension

__author__ = 'safaariman'


if __name__ == '__main__':
    JiraExtension().run()
