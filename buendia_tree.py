# -*- coding: latin-1 -*-
from pyDatalog import  pyDatalog
import data
import logic

def initialize():
    variables = 'V, W, X, Y, Z'
    functions = 'gender, buendia_blood, buendia, bastard, inbred, parent, mother, father, sibling, brother, sister, child, daughter, son, married, wife, husband, decendent, ancestor, aunt, uncle, cousin'
    pyDatalog.create_terms(variables + ', ' + functions)

def load_data():
    data.load_data(pyDatalog)

def load_logic():
    logic.load_logic(pyDatalog)

def main():
    initialize()
    load_data()
    load_logic()

if __name__ == "__main__":
    main()
    pass



