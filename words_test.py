import unittest
from words import FoodStore

class TestWordDictionary(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_document_representation(self):
        words = "hot,chocolate,milk"
        fs = FoodStore()       
        fs.foodList = words
        print "If our list of all words is this: [ 'hot', 'chocolate', 'milk']"
        
        print "The document 'hot chocolate' is represented as : [1 1 0]"
        self.assertEqual( fs.documentList["hot chocolate"], [1, 1, 0])

        print "The document 'hot milk' is represented as : [1 0 1]"
        self.assertEqual( fs.documentList["hot milk"], [1, 0, 1])

    def test_search_query(self):
        words = "hot,chocolate,milk"
        fs = FoodStore()       
        fs.foodList = words
            
        print "The search query 'hot chocolate' is represented as : [1 1 0]"
        self.assertEqual( fs.searchQuery("hot chocolate"), [1, 1, 0])

        print "The search query 'chocolate' is represented as : [0 1 0]"
        self.assertEqual( fs.searchQuery("chocolate"), [0, 1, 0])

    def test_search_functionality(self):
        words = "hot,chocolate,milk"
        fs = FoodStore()       
        fs.foodList = words
            
        print "The matching documents obtained on searching 'hot chocolate' are:"
        print fs.matchingDocuments("hot chocolate")
        print "Checking if re-ordering of strings in search query returns same result"
        self.assertEqual( fs.matchingDocuments("hot chocolate"), fs.matchingDocuments("chocolate hot"))
 
if __name__ == '__main__':
    unittest.main()