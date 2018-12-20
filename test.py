import unittest
import buendia_tree
from pyDatalog import pyDatalog

class TestParentRelations(unittest.TestCase):
    def setUp(self):
        buendia_tree.main()
    def test_parent_child(self):
        query = 'parent(X, "Amaranta Buendia")'
        answers = sorted(pyDatalog.ask(query).answers)
        expected_answers = sorted([('Ursula Iguaran',), ('Jose Arcadio Buendia',)])
        self.assertEqual(answers,expected_answers)
    def test_father_child(self):
        query = 'father(X, "Amaranta Buendia")'
        answers = pyDatalog.ask(query).answers
        expected_answers = [('Jose Arcadio Buendia',)]
        self.assertEqual(answers,expected_answers)
    
    def test_mother_child(self):
        query = 'mother(X, "Amaranta Buendia")'
        answers = pyDatalog.ask(query).answers
        expected_answers = [('Ursula Iguaran',)]
        self.assertEqual(answers,expected_answers)

    def test_bastard(self):
        query = 'bastard(X)'
        answers = pyDatalog.ask(query).answers
        expected_answers = ('Aureliano (III)',)
        self.assertIn(expected_answers, answers)

class TestFamily(unittest.TestCase):
    def setUp(self):
        buendia_tree.main()
    def test_siblings(self):
        query = 'sibling(X, "Colonel Aureliano Buendia")'
        answers = sorted(pyDatalog.ask(query).answers)
        expected_answers = sorted([("Jose Arcadio Buendia (II)", ), ("Amaranta Buendia", )])
        self.assertEqual(expected_answers, answers)
    def test_brother(self):
        query = 'brother(X, "Colonel Aureliano Buendia")'
        answers = pyDatalog.ask(query).answers
        expected_answers = [("Jose Arcadio Buendia (II)", )]
        self.assertEqual(expected_answers, answers)
    
    def test_sister(self):
        query = 'sister(X, "Colonel Aureliano Buendia")'
        answers = pyDatalog.ask(query).answers
        expected_answers = [("Amaranta Buendia", )]
        self.assertEqual(expected_answers, answers)
    
    def test_cousin(self):
        query = 'cousin(X, "Aureliano Jose Buendia")'
        answers = pyDatalog.ask(query).answers
        expected_answers = [("Arcadio (Jose Arcadio III)", )]
        self.assertEqual(expected_answers, answers)
    

def main():
    buendia_tree.main()
    query = "parent(X, Y)"
    answers = pyDatalog.ask(query).answers
    for ans in answers:
        print(ans)
    pass

if __name__ == "__main__":
    main()  