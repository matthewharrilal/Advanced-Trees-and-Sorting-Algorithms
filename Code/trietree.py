

class TrieTrieeNode(object):

    def __init__(self, data):
        # What does a node in a Trie Tree consist of an array references, each node contains data, and a flag representing that the end of a sequence exists
        self.flag = False
        self.data = data
        # Since we know that every node has references containing up to 26 null node values
        self.references = [None] * 26
        self.number_of_active_references = 0


class TrieTree(object):
    def __init__(self, vocabulary=None):
        # root node will always be an empty string
        self.root = TrieTrieeNode(" ")
        # User will pass in an array of vocabulary words ... for every word we want to insert it into our tree
        if len(vocabulary) > 0:
            for word in vocabulary:
                self.insert(word)

    def search(self, word):
        # Find a node in the given trie tree given the name of the word
        root_node = self.root
        for index in range(0, len(word)):

            current_letter = word[index]
            position = self.__alphabet_index_helper(current_letter)

            if root_node.references[position] is None:
                return False

            root_node = root_node.references[position]

        # Instead of checking for the flag at that point walk all walks to see available words

        # Two base cases if the element is a flag and if there are no more references

        # if root_node.flag == False:
        #     return False
        # return True

        return root_node

    # ASCII CODE REFACTOR
    def __alphabet_index_helper(self, letter):
        # BREAKS WITH APOSTROPHES
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print(letter)
        return alphabet.index(letter.lower())

    def insert(self, word):
        # Insert a given word into the Trie Tree

        root_node = self.root

        for index in range(0, len(word)):
            # Getting each letter in the word
            current_letter = word[index]
            current_node = TrieTrieeNode(current_letter)

            # What if a pathway already exists? Dont want to overwrite it becasue a flag there might be set
            position = self.__alphabet_index_helper(current_letter)

            if root_node.references[position] is None:

                root_node.references[position] = current_node
                root_node.number_of_active_references += 1
            root_node = root_node.references[position]  # Go one level deeper

        root_node.flag = True  # To mark that the end of sequence occured here

    def delete(self, word):
        '''Delete the node from the tree'''
        # Dont want to use search function because it would return a copy of the node we need to alter the nodes in place
        root_node = self.root
        parent_node = None

        # First check if word is contained inside trie tree
        if self.search(word) is False:
            raise ValueError("Can't delete a word that does not exist")

        for index in range(0, len(word)):
            current_letter = word[index]

            # Have to find where the last element is positioned
            position = self.__alphabet_index_helper(current_letter)

            parent_node = root_node
            root_node = root_node.references[position]

        # Found the end of the sequence first set flag to false
        root_node.flag = False

        # Then check if it had references
        if root_node.number_of_active_references == 0:
            # Find parent node and set root node in parent node references to null
            index = self.__alphabet_index_helper(root_node.data)
            parent_node.references[index] = None  # Erase its history

        return word

    def recursiveWalk(self, word, node=None, output=None, concat=None):

        # Firstly what point do we need to get to to execute this function we first need to get that node's references
        if node is None and concat is None:
            node = self.search(word)  # Find where the prefix ends
            output = []
            concat = "" + word

        # Whats the base case? # when do we want this to stop
        if node.flag is True:
            output.append(concat)

        if node.number_of_active_references == 0:  # meaning we went as deep as we can
            return

        for reference in node.references:  # Because every iteration of for loop starts from beginning of top level node's references

            if reference is not None:
                concat += reference.data  # THIS LINE RIGHT HERE
                self.recursiveWalk(word, reference, output, concat)
                concat = "" + word  # When the recursive stack resolves reset the concatenation

        return output


#  # Search for different keys
    # output = ["Not present in trie","Present in trie"]


#     print("{} ---- {}".format("the",output[t.search("the")]))
#     print("{} ---- {}".format("these",output[t.search("these")]))
#     print("{} ---- {}".format("their",output[t.search("their")]))
#     print("{} ---- {}".format("thaw",output[t.search("thaw")]))
