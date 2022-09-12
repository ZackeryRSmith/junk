#!/usr/bin/python
# -*- coding: utf-8 -*-
# A one line script that converts python code into one line... How useful

# Reads all code from "code.py", and the output code goes to "out.py"                                                                                  
with open("code.py", "r") as c, open("out.py", "w+") as o: o.write(f"exec({str(bytes(c.read(), 'utf-8'))})")
