#!python
from sorting_iterative import bubble_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions? #O(n) due to n being the number of elements in both lsts iterating over each once
    TODO: Memory usage: ??? Why and under what conditions?""" # o(n) because output grows as input grows
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    # Pointers to elements in corresponding item lsts
    left_counter = 0 
    right_counter = 0
    sorted_lst = [] # Lst containing sorted output

    # Iterating over corresponding elements until one index goes out of range
    while left_counter < len(items1) and right_counter < len(items2):

        # Checking for order in which elements should be outputted to sorted array
        if items1[left_counter] < items2[right_counter]:
            sorted_lst.append(items1[left_counter])
            left_counter += 1
        elif items1[left_counter] > items2[right_counter]:
            sorted_lst.append(items2[right_counter])
            right_counter += 1
        else:
            sorted_lst.append(items1[left_counter])
            sorted_lst.append(items2[right_counter])
            left_counter += 1
            right_counter += 1

    # Check which array still has elements remaining, wont execute if lst index is out of range
    while left_counter < len(items1):
      sorted_lst.append(items1[left_counter])
      left_counter += 1
      
    while right_counter < len(items2):
      sorted_lst.append(items2[right_counter])
      right_counter += 1

    return sorted_lst


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    median = len(items) // 2 # Using floor to give us equal halves
    left_half = items[:median + 1]
    right_half = items[median + 1:]
    return(merge(bubble_sort(left_half), bubble_sort(right_half)))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
