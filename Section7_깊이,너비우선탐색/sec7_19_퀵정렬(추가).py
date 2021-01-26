def Qsort(lt,rt) :
    if lt <rt :
        pivot=arr[rt]
        pos=lt
        for i in range(lt,rt) :
            if arr[i] <= pivot :
                # tmp=arr[pos]
                # arr[pos]=arr[i]
                # arr[i]=tmp
                arr[i],arr[pos]=arr[pos],arr[i]  # swap 과정 한줄에 가능하다.
                pos+=1

        arr[rt],arr[pos]=arr[pos],arr[rt]
        Qsort(lt,pos-1)
        Qsort(pos+1, rt)

if __name__=="__main__" :
    arr=[23,11,45,36,15,67,33,21]
    print("Before :", end=" ")
    print(arr)


    Qsort(0,len(arr)-1)
    print("After", end=" ")
    print(arr)

