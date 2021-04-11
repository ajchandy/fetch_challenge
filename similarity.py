import sys


def set_intersection(c1, c2):
    s1, s2 = set(c1.split()), set(c2.split())
    return len(s1 & s2) / len(s1 | s2)


def levenshtein(c1, c2):
    s1, s2 = c1.split(), c2.split()
    D = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)] # creates a matrix with all 0's and also accounts for the empty string
    for i in range(1, len(s1)+1): # initialization
        D[i][0] = i
    for j in range(1, len(s2)+1): # initialization
        D[0][j] = j
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1])
            else:
                D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+2)
    return (len(s1) + len(s2) - D[-1][-1]) / (len(s1) + len(s2))


def find_similarity(f1, f2, metric=levenshtein):
    """
    Finds similarity between two corpora using the metric passed.
    f1: path to file 1
    f2: path to file 2
    metric: (default set_intersection) Similarity metric to be used
    """

    c1, c2 = "", ""
    try:
        with open(f1, 'r') as f:
            c1 = f.read().strip()
    except:
        print("!!! CANNOT READ FILE", f1, "!!!")
        return
    try:
        with open(f2, 'r') as f:
            c2 = f.read().strip()
    except:
        print("!!! CANNOT READ FILE", f2, "!!!")
        return
    if len(c1):
        if len(c2):
            return metric(c1, c2)
        else:
            print("!!! EMPTY FILE", f2, "!!!")
    else:
        print("!!! EMPTY FILE", f1, "!!!")


if __name__=="__main__":
    try:
        f1, f2 = sys.argv[1], sys.argv[2]

    except IndexError:
        f1, f2 = input('Enter path to file 1: '), input('Enter path to file 2: ')

    except:
        print("!!! INVALID COMMAND LINE INPUTS !!!")
        exit()
    try:
        metric = ("set_intersection", "levenshtein")[int(input("Which metric do you want to use to compute the similarity? (defaults to levenshtein)\n1. Set Intersection\n2. Levenshtein\n")) - 1]
    except:
        print("!!! INVALID INPUT !!!\nDefaulting to Levenshtein")
        metric = "levenshtein"
    print(find_similarity(f1, f2, eval(metric)))