from trietree import TrieTrieeNode
from trietree import TrieTree


def autocomplete_setup(vocabulary):
    t = TrieTree(vocabulary)
    return t


def autocomplete(vocabulary):

    return autocomplete_setup(vocabulary).recursiveWalk("ca")


if __name__ == '__main__':


    with open("random.txt") as file:
        lines = [line.strip() for line in file]
    # for word in lines:
    #     word = word.lower()
    
    print(autocomplete(lines))
    
    
