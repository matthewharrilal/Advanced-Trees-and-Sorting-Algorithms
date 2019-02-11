class TrieTrieeNode(object):
    def __init__(self, data):
        # What does a node in a Trie Tree consist of an array references, each node contains data, and a flag representing that the end of a sequence exists
        self.flag = False
        self.data = data
        self.references = [] # Using an array to represent the node's references