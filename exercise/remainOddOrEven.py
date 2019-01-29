def remainOddOrEven(int_list):
    """Delete odd or even int by length of list
    
    Arguments:
        int_list {[list of int]} -- [outlier deleted list]
    
    Returns:
        [list of int] -- [only odd or even ints]
    """
    even=[]
    odd=[]
    for i in int_list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
    if len(int_list)%2==0:
        modified_list = even
    else:
        modified_list = odd
    return modified_list

