#!/usr/bin/env python3
"""Multilanguage Hello World program in Python.

This program will print "Hello World" depending on the locally configured 
language.

Requirements:
- LANG variable must be set with a valid language (e.g. "export LANG=pt_BR)

How to run:
python3 hello.py
or
./hello.py
groselha
"""
__version__ = "0.0.1"
__author__ = "Theles Silveira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

#This program print "Hello, World!" on screen.
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
if current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)