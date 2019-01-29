def deleteOutlier(int_list):
    """Delelte outlier (not 10-20) int
    
    Arguments:
        int_list {[list of int]} -- [input list]
    
    Returns:
        [list of int] -- [outlier deleted list]
    """
    i=0
    modified_list = []

    while i < len(int_list):
        if 10 <= int_list[i] and int_list[i] <= 20:
            modified_list.append(int_list[i])
        i+=1
    return modified_list