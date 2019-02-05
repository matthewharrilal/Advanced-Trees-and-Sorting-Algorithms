#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    minimum, maximum = min(numbers), max(numbers)
    count_array = [0] * ((maximum + 1) - minimum)
    offset = minimum
    output = [0] * len(numbers)


    for index in range(0, len(numbers)):
        current_element = numbers[index]
        # if count_array[current_element - offset] > 0: # Meaning that we've seen an occurence
        count_array[current_element - offset] += 1
    
    i = 0
    for num in range(len(count_array)): # Represents the index which is the value in input
        for occurence in range(count_array[num]): # Iterate over how many times you see that specific element
            numbers[i] = num + offset
            i  +=  1
    
    

  return numbers
    
def bucket_sort(numbers, num_buckets=5):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # minimum,maximum = min(number), max(number)
    range_num = len(numbers) // num_buckets
    buckets = [[] for _ in range(range_num + 1)]
    # print(buckets[5])
    
    for index, number in enumerate(numbers):
      # Two cases number 15 and number 3
      print(number)
      bucket_index, remainder = divmod(number , range_num)

      if remainder > 0:
        buckets[bucket_index].append(number)
      else:
        buckets[bucket_index - 1].append(number)
      

    return buckets