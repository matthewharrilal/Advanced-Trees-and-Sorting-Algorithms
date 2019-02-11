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

        for index in range(0, len(word)):

            current_letter = word[index]
            current_node = TrieTrieeNode(current_letter)
            # print(root_node.references)
            # print("")
            position = self.__alphabet_index_helper(current_letter)

            # print(root_node.data,root_node.references, root_node.references[position].data)

            # If at the position there is no value meaning that there is no more pathway
            if root_node.references[position] is None:
                print("FOUND NO MORE PATHWAY", current_letter)
                return False
            # print(current_node.references)
            root_node = root_node.references[position]

        if root_node.flag == False:  # If it was a search miss meaning we found it but the flag wasn't marked
            return False
        return True

    def __alphabet_index_helper(self, letter):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        return alphabet.index(letter)

    def insert(self, word):
        # Insert a given word into the Trie Tree

        # Whats auto updating our root node

        # Why do we we need recursion because cant we update every iteration the node to be the previous node

        # Would we lose the root node if we change the value ... not if we store it

        root_node = self.root

        for index in range(0, len(word)):
            # Getting each letter in the word
            current_letter = word[index]
            current_node = TrieTrieeNode(current_letter)

            # What if a pathway already exists?
            position = self.__alphabet_index_helper(current_letter)
            root_node.references[position] = current_node
            # print(root_node.data,root_node.references, current_node.data)

            root_node = root_node.references[position]  # Go one level deeper
            # print("")

        root_node.flag = True  # To mark that the end of sequence occured here
        return root_node  # Stub

    def delete(self, word):
        # Delete a given node from the Trie Tree
        pass
