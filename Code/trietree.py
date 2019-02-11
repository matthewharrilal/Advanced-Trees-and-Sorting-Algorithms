class TrieTrieeNode(object):
    def __init__(self, data):
        # What does a node in a Trie Tree consist of an array references, each node contains data, and a flag representing that the end of a sequence exists
        self.flag = False
        self.data = data
        self.references = [] # Using an array to represent the node's references ... an array of trie tree node objects



class TrieTree(object):
    def __init__(self, vocabulary=None):
        # User will pass in an array of vocabulary words ... for every word we want to insert it into our tree
        if len(vocabulary) > 0:
            for word in vocabulary:
                self.insert(word)

    def find(self, word):
        # Find a node in the given trie tree given the name of the word
        pass

    def __alphabet_index_helper(self, letter):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        return alphabet.index(letter)
    

    def insert(self, word):
        # Insert a given word into the Trie Tree

        # Our root node is always an empty string to represent that any word can be inserted
        empty_string = ""
        root_node = TrieTrieeNode(empty_string)

        root_node.references = [None] * 26 # Allocating the references

        # Now that we have the node's references now as we iterate over each letter in the string as the iterations go deeper
        
        
        for index in range(0, len(word)):
            # Getting each letter in the word
            current_letter = word[index]
            current_node = TrieTrieeNode(current_letter)


    
    def delete(self, word):
        # Delete a given node from the Trie Tree
        pass