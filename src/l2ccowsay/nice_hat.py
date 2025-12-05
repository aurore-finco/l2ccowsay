# -*- coding: utf-8 -*-
"""
Created on Thu May 15 15:13:55 2025

@author: Modoukpè
"""

from l2ccowsay.characters import STEGOSAURUS


def stegosauring(txt: str = "Nice hat"):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + STEGOSAURUS


print(stegosauring())
