import sys
from readInputTextFile import readInputTextFile
from deleteOutlier import deleteOutlier
from remainOddOrEven import remainOddOrEven
from countNumOfUnique import countNumOfUnique

def myOwnCounter(filename):

    int_list = readInputTextFile(filename)
    int_list = deleteOutlier(int_list)
    int_list = remainOddOrEven(int_list)
    num_of_uniq = countNumOfUnique(int_list)
    
    return num_of_uniq

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = "input.txt"
    else:
        filename = sys.argv[1]
    print("Answer in {}".format(myOwnCounter(filename)))
