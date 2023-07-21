def twoSum(array, target):
    dict={}
    for i in range(len(array)):
        k=target-array[i]
        if k in dict:
            return [dict[k],i]
        else:
            dict[array[i]]=i
if __name__ == '__main__':
    array=list(map(int,input().split()))
    target=int(input())
    print(twoSum(array,target))