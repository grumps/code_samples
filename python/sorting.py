# Implimentation of various sorting algorithms for our_lists
##########################

def swappa_list(our_list, low, high):
    our_list[low], our_list[high] = our_list[high], our_list[low]
    return our_list


def selection_sort(our_list):
    """
    Look through the our_list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """

    for start in range(len(our_list)):
        min_index = start
        smallest = our_list[start]
        # find smallest num
        # enumerate DOES NOT WORK
        for key in range(start + 1, len(our_list)):
            if our_list[key] < smallest:
                min_index = key
                smallest = our_list[key]
        if min_index != start:
            swappa_list(our_list, start, min_index)
    return our_list

def insertion_sort(our_list):
    """ 
    Insert (via swaps) the next element in the sorted our_list of the previous
    elements.
    """
    for start in range(1, len(our_list)):
        candidate = our_list[start]
        candidate_index = start - 1
        while candidate_index >= 0:
            if candidate < our_list[candidate_index]:
                swappa_list(our_list, candidate_index, candidate_index + 1)
                candidate_index -= 1
            else:
                break
    return our_list


def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    number_elements = len(our_list)
    # base case
    if number_elements == 1:
        return our_list

    half_index_position = number_elements // 2
    sorted_list = []

    # recursive goodness
    lower_half = merge_sort(our_list[:half_index_position])
    upper_half = merge_sort(our_list[half_index_position:])

    # merging
    while len(lower_half) > 0 and len(upper_half) > 0:
        # who is lower?
        if lower_half[0] <= upper_half[0]:
            sorted_list.append(lower_half.pop(0))
        else:
            sorted_list.append(upper_half.pop(0))
    sorted_list += lower_half + upper_half
    return sorted_list
