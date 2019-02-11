class TrieTrieeNode(object):
    def __init__(self, data):
        # What does a node in a Trie Tree consist of an array references, each node contains data, and a flag representing that the end of a sequence exists
        self.flag = False
        self.data = data
        # Since we know that every node has references containing up to 26 null node values
        self.references = [None] * 26


class TrieTree(object):
    def __init__(self, vocabulary=None):
        # root node will always be an empty string
        self.root = TrieTrieeNode(" ")
        # User will pass in an array of vocabulary words ... for every word we want to insert it into our tree
        if len(vocabulary) > 0:
            for word in vocabulary:
                self.insert(word)

    def find(self, word):
        # Find a node in the given trie tree given the name of the word
        root_node = self.root
        concat = ""
        for index in range(0, len(word)):

            current_letter = word[index]
            concat += current_letter
            position = self.__alphabet_index_helper(current_letter)

            if root_node.references[position] is None:
                return False

            root_node = root_node.references[position]

        print(concat, root_node.data, root_node.flag)
        if root_node.flag == False:
            return False
        return True

    def __alphabet_index_helper(self, letter):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        return alphabet.index(letter)

    def insert(self, word):
        # Insert a given word into the Trie Tree

        root_node = self.root
        concat = ""

        for index in range(0, len(word)):
            # Getting each letter in the word
            current_letter = word[index]
            current_node = TrieTrieeNode(current_letter)
            concat += current_letter

            # What if a pathway already exists? Dont want to overwrite it becasue a flag there might be set
            position = self.__alphabet_index_helper(current_letter)

            if root_node.references[position] is None:

                root_node.references[position] = current_node

            root_node = root_node.references[position]  # Go one level deeper

        root_node.flag = True  # To mark that the end of sequence occured here

    def find_parent_reference(self, node):
        '''Find the Parent Node of the given word in the trie'''

    def delete(self, word):
        '''Delete the node from the tree'''
        # Dont want to use search function because it would return a copy of the node we need to alter the nodes in place

        # First check if word is contained inside trie tree
        if self.find(word) is False:
            raise ValueError("Can't delete a word that does not exist")

#  # Search for different keys
    # output = ["Not present in trie","Present in trie"]


#     print("{} ---- {}".format("the",output[t.search("the")]))
#     print("{} ---- {}".format("these",output[t.search("these")]))
#     print("{} ---- {}".format("their",output[t.search("their")]))
#     print("{} ---- {}".format("thaw",output[t.search("thaw")]))
