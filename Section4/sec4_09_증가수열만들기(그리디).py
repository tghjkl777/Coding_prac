import sys

sys.stdin=open("input_9.txt","rt")

n=int(input())


array=list(map(int, input().split()))


cnt=0
string=""
last=0

while array :
    left=array[0]
    right=array[len(array)-1]

    if left < last and right <last :
        break


    elif left > last and right < last :
        cnt+=1
        string+="L"
        last=left
        array.pop(0)
    elif left < last and right > last :
        cnt+=1
        string+="R"
        last=right
        array.pop()
    else :
        if left <right :
            cnt += 1
            string += "L"
            last = left
            array.pop(0)
        else :
            cnt += 1
            string += "R"
            last = right
            array.pop()

print(cnt)
print(string)