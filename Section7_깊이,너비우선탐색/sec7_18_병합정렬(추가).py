def Dsort(lt,rt):

    if lt < rt :
        mid= (lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)

        ###이 함수 본연의 일  : 정렬된 두 리스트 합치기
        p1=lt
        p2=mid+1
        tmp=[]

        while p1<=mid and p2<=rt : # 둘중에 하나가 틀리면 끝나는 것임.
            if arr[p1]<arr[p2] :
                tmp.append(arr[p1])
                p1+=1
            else :
                tmp.append(arr[p2])
                p2+=1


        if p1 <=mid :
            tmp+=arr[p1:mid+1]
        if p2 <=rt :
            tmp+=arr[p2 :rt+1]

        for i in range (len(tmp)) :
            arr[lt+i]=tmp[i]  # 위치 인덱스 고려해야 한다.

if __name__=="__main__" :
    arr=[23,11,45,36,15,67,33,21]
    print("Before :", end=" ")
    print(arr)


    Dsort(0,len(arr)-1)
    print("After", end=" ")
    print(arr)


