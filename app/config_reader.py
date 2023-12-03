#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import PATH, CONFIGURATIONS
import toml
import os

def find_configuration_folder() -> None:
    result = os.path.exists("./pjm")
    if not result:
        print("The configuration folder is not present")
        create_config = input("You would like to create it? (Y/n)[Y]  ")
        if "Y" in create_config or create_config=="":
            print("Creating configuration folder...")
            try:
                os.mkdir("./pjm")
            except Exception as e:
                print(e)
                print(f"Something went wrong while creating configuration folder")
        else:
            print("OK THEN SEE YOU LATER <3")




            

def load_configurations() -> dict:
    global CONFIGURATIONS
    result = [os.path.join(PATH, file) for file in os.listdir(PATH)]

    try:
       return toml.load(result)
    except Exception as e:
        print(e)
        print("Unable to load configuration, please verify configuration syntax")


