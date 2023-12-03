#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config_reader import load_configurations
from frontend import main_menu

PATH="~/.pjm"
CONFIGURATIONS = None 




if __name__ == "__main__":
    CONFIGURATIONS = load_configurations()
    main_menu(CONFIGURATIONS)
   
