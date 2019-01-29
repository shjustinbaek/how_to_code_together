def readInputTextFile(filename):
    """Read input file(filename) and return list of int

    Arguments:
        filename {[string]} -- [name of input file]

    Returns:
        [list of int] -- [input list]
    """
    with open(filename, 'r') as f:
        line = f.read()
        str_int_list = line.split()
        int_list = []
        for i in str_int_list:
            int_list.append(int(i))
    return int_list
