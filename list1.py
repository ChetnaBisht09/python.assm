l=[]

def append1(x):
    l.append(x)
    print("after append:",l)

def extend1(lst):
    l.extend(lst)
    print("after extends:",l)

def pop():
    value=l.pop()
    print("after pop:",l)
    return value

def remove1(x):
    l.remove(x)
    print ("after remove:",l)