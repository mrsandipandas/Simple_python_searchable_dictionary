import itertools

class FoodStore(object):
    
    def __init__(self):
    	# Create a food dictioanry for easy indexing in creating the query string
        # eg. {'hot': 0, 'chocolate': 1, 'milk': 2}
    	self.foods = {}

        # Document sore is a dictioanry containing all the combinations of search strings as keys
        # In the values the corresponding binary vectors are present
        # eg. {
        #      'hot chocolate': [1, 1, 0], 
        #      'chocolate milk': [0, 1, 1], 
        #      'hot chocolate milk': [1, 1, 1], 
        #      'chocolate': [0, 1, 0], 
        #      'hot': [1, 0, 0], 
        #      'hot milk': [1, 0, 1], 
        #      'milk': [0, 0, 1]
        #     } 
    	self.documentStore = {}

    #Getter
    @property
    def documentList(self):
        return self.documentStore

    #Getter
    @property
    def foodList(self):
        return self.foods

    # Setter, stores foods in a list
    @foodList.setter
    def foodList(self, value):
    	if "," in value:
    		foodItems = value.split(",")
    		count = len(foodItems)
    		for i in range(count):
    			self.foods[foodItems[i]] = i

    		# update document vector with all combinations
    		self.__documentList(foodItems)
    	else:
            raise Exception("Please provide comma seperated words!")
    
    # Create the document list with all combinations        
    def __documentList(self, items):
    	size = len(items)
    	for i in xrange(1,len(items)+1):
            # Create all combinations of search strings from the word list
   			combinations = list(itertools.combinations(items,i)) 			
   			for item in range(len(combinations)):  
                # Initialize an array as size of the list
   				vector = [0] * size				
				for element in combinations[item]:
					# Mark '1' in vector for matched conditions
					vector[self.foods[element]] = 1
				# Store the document as specified by search string
				self.documentStore[' '.join(combinations[item])] = vector
    
    def searchQuery(self, query):
        size = len(self.foods)
        # Initialize an array as size of the list
        vector = [0] * size	
        queryItems = query.split(" ")
        for element in queryItems:
            # Mark '1' in vector for matched conditions
            if element in self.foods:
                vector[self.foods[element]] = 1
        return vector

    def matchingDocuments(self, query):
        matched = []
        maximum = 0
        queryVector = self.searchQuery(query)
        for key in self.documentStore.iterkeys():
            current = self.scalarProduct(queryVector, self.documentStore[key])
            # If more than one documents are matching then keep track of all in all cases
            # Update the maximum scalar product
            if current == maximum:
                matched.append(key)
                maximum = current
            elif current > maximum:
                matched[:] = []
                matched.append(key)
                maximum = current
        return matched


    def scalarProduct(self, queryVector, documentVector):
        return sum(p*q for p,q in zip(queryVector, documentVector))
