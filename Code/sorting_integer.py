#!python



def count_sort(numbers):
  minimum, maximum = min(numbers), max(numbers)
  count_array = [0] * ((maximum + 1) - minimum)
  offset = minimum
  output = [0] * len(numbers)


  for index in range(0, len(numbers)):
    current_element = numbers[index]
    if count_array[current_element - offset] > 0: # Meaning that we've seen an occurence
      count_array[current_element - offset] += 1
    else:
      count_array[current_element - offset] = 1 # Meaning we havent

  for index in range(0, len(count_array) - 1):
    next_index = index + 1

    count_array[next_index] += count_array[index]

  for index,num in enumerate(numbers):
    # print(num, num - offset, count_array)
    output[count_array[num - offset] - 1] = num # Have to subtract by 1 to represent index
    count_array[num - offset] -= 1 # Decrement the number of occurences we accounted for by 1

  return output
    

def bucket_sort(numbers, num_buckets=10):
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
