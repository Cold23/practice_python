def recursive_remove_duplicates(x):
    res = []
    for elem in x :
        if elem not in res :
            res.append(elem)
    print(res)

def non_recursive_remove_duplicates(x):
    res = list(dict.fromkeys(x))
    print(res)

if __name__ == "__main__":
    x = [1,1,1,3,4,5,6,3,6,8,12,1,3,4,5]
    non_recursive_remove_duplicates(x)