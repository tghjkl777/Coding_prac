import sys

sys.stdin=open("input_2.txt","rt")
tree=list(map(int,input().split()))
tree.insert(0,0)
print(tree)

def front(i) :
    if i> len(tree)-1 :
        return
    else:
        print(tree[i],end=" ")
        front(i*2)
        front(i*2+1)


def mid(i) :
    if i> len(tree)-1 :
        return
    else:
        mid(i*2)
        print(tree[i], end=" ")
        mid(i*2+1)


def back(i) :
    if i> len(tree)-1 :
        return
    else:
        back(i*2)
        back(i*2+1)
        print(tree[i],end=" ")

if __name__=="__main__" :
    i=1

    print("전위 순회 :",end=" ")
    front(i)
    print()
    print("중위 순회 :",end=" ")
    mid(i)
    print()
    print("후위 순회 :",end=" ")
    back(i)
    print()






