def countNumOfUnique(int_list):
    """Count number of diff int
    
    Arguments:
        int_list {[list of int]} -- [only odd or even ints]
    
    Returns:
        [int] -- [number of diff int]
    """
    num_of_uniq = 0
    list_of_uniq = []
    for i in int_list:
        if (i not in list_of_uniq):
            list_of_uniq.append(i)
            num_of_uniq = num_of_uniq + 1
    
    return num_of_uniq