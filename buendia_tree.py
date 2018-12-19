# -*- coding: latin-1 -*-
from pyDatalog import  pyDatalog
import data
import logic

def initialize():
    variables = 'V, W, X, Y, Z'
    functions = 'gender, buendia_blood, buendia, bastard, inbred, parent, mother, father, sibling, brother, sister, child, daughter, son, married, wife, husband, decendent, ancestor, aunt, uncle, cousin'
    pyDatalog.create_terms(variables + ', ' + functions)

def load_data():
    generations = data.load_data(pyDatalog)
    return generations

def load_logic():
    logic.load_logic(pyDatalog)

def main():
    initialize()
    generations = load_data()
    load_logic()
    query = "parent(X, Y)"
    answers = pyDatalog.ask(query).answers
    for ans in answers:
        print(repr(ans[0]).encode('utf-8'))

if __name__ == "__main__":
    main()
    pass



