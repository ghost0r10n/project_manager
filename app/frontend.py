#!/usr/bin/env python
# -*- coding: utf-8 -*-
from simple_term_menu import TerminalMenu
import clipboard


def main_menu(configuration:dict):
    print("Please select a project")
    options = [project for project in configuration.keys()]
    terminal_menu = TerminalMenu(options)
    selection = terminal_menu.show()
    print(f"You have selected {options[selection]}!")
    value_selection(configuration, options[selection])

def value_selection(configuration:dict, selected_project:str):
    print("Select value to copy")
    options = [project for project in configuration[selected_project].keys()]
    terminal_menu = TerminalMenu(options)
    selection = terminal_menu.show()
    selected_value = configuration[selected_project][options[selection]]
    clipboard.copy(selected_value)
