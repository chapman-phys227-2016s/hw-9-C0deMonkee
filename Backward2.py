#! /usr/bin/env python

"""
File: Backward2.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 9.11
Date: April 3, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implements a backwards differentiation method
"""
import numpy as np
import math
class Backward1(Diff): # Extends
    """
    First order backwards differentiation method
    """
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
    def diff(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff): # Extends
    """
    Second order backwards differentiation method
    """
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
    def diff(self, x):
        f, h = self.f, self.h
        return (f(x-2*h) - 4*f(x-h) + 3*f(x))/ (2*h)