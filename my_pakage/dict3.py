dict={}

def len3():
    print("lenth of dictionary:",len(dict))
    return len(dict)

def add3(k,v):
    dict[k]=v
    print("after add:",dict)

def keys3():
    print("keys:",list(dict.keys()))
    retun list(dict.keys())

def values3():
    print ("value:",list(dict.values()))
    return list(dict.values())