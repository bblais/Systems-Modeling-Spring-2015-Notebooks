#!/usr/bin/env python
import os

value=os.system("ipython notebook")

if value>0:
    value=os.system("ipython notebook --port 9999")

