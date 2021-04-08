import sys

def set_intersection(c1, c2):
    s1, s2 = set(c1.split()), set(c2.split())
    return len(s1 & s2) / len(s1 | s2)


def find_similarity(f1, f2, metric=set_intersection):
    """
    Finds similarity between two corpora using the metric passed.
    f1: path to file 1
    f2: path to file 2
    metric: (default set_intersection) Similarity metric to be used
    """
    #TODO: preprocessing (removing punctuations and stopwords)

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
    except:
        print("!!! INVALID COMMAND LINE INPUTS !!!")
        exit()
    print(find_similarity(f1, f2))