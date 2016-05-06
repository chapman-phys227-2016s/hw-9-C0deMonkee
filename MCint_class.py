#! /usr/bin/env python

"""
File: MCint_class.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 9.14
Date: April 3, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Class hierarchy structures
"""
class Integrator(object):
    """Contains an array of integration techniques. The one which was added
    for this exercise is MCint_vec, which is the one which is otherwise documented
    and which has its own test function."""
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
                                  self.__class__.__name__)

    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s



class MCint_vec(Integrator):
    """Uses the Monte Carlo random number generation to integrate the function. This function
    returns an array of function analysis points as well as an array of weight values for those points."""
    def construct_method(self):
        h = float(self.b - self.a) / self.n
        x = np.random.uniform(self.a, self.b, self.n)
        w = np.zeros(len(x)) + h
        return x, w