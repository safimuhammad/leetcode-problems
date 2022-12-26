# ROMAN TO INTEGER
def romToint(s):
    r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    # s="LVIII"
    temp = 0
    s_split= [*s]
    min_flag_nan=False
    for i in enumerate(s_split):
        min_flag_nan = False
        
        for j in r:
            if i[1] == j:
                
                # for I
                if i[1] == 'I':
                    if s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'V':
                        temp=(5-1)+temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break

                    elif s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'X':
                        temp=(10-1)+temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break
                    
                  # for X
                if i[1] == 'X':
                    if s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'L':
                        temp=(50-10)+temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break

                    elif s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'C':
                        temp=(100-10)+temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break
                    
                 # for C
                if i[1] == 'C':
                    if s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'D':
                        temp=(500-100)+temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break

                    elif s_split[i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1 ] == 'M':
                        temp=(1000-100) + temp
                        s_split.pop(i[0]+0 if i[0]==len(s_split)-1 else  i[0]+1)
                        break

                   
                if s_split:
                    temp=r[j]+temp 
    return temp

# 1704. Determine if String Halves Are Alike
def halvesAreAlike(s):
    
    s_list= [*s.lower()]
    s_halve_length= int(len([*s])/2)
    s_halve_1= s_list[slice(s_halve_length)]
    s_halve_2=s_list[slice(s_halve_length,len(s_list))]
    print(vowel_checker(s_halve_1))
    if vowel_checker(s_halve_1) == vowel_checker(s_halve_2):
        return True
    else: 
        return False
    



def vowel_checker(s_halve):
    vowels=['a','e','i','o','u']
    print(s_halve)
    vowel_count=0
    for i in s_halve:
        for j in vowels:
            if i == j :
                vowel_count=vowel_count+1
                
    return vowel_count


                


# nums=[1,2,3,1]
# print(dupli(nums))

def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    mid=0

    while low<=high:
        mid = (high +low)//2
        print(mid,'mid',low,'low')
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        
    return -1
# arr=[-1,0,3,5,9,12]
# target=9
# print(binarySearch(arr, target))

def searchInsert(nums,target):
    low=0
    high=len(nums)-1
    mid=0
    new_t=0
    while low<=high:
        mid = (high+low)//2
        if nums[mid]> target:
            if abs(nums[mid]-target) ==1:
                print('i am in more')
                new_t=mid
            high=mid-1
        elif nums[mid]<target:
            if abs(nums[mid]-target) ==1:
                print('i am in less')
                new_t=mid+1
            else:
                new_t=high
            low=mid+1
        else:
            return mid
       
    return new_t

# nums = [1,3,5,6] 
# target = 7



# Two-Pointers Algorithm
nums = [-4,-1,0,3,10]
def twoPointers(nums):
    n=len(nums)
    i=0
    j= n-1
    arr=[0]*n
    ind= n-1
   

    while i<=j:
        if abs(nums[i]) > abs(nums[j]):
            
            arr[ind] = nums[i]**2
            i=i+1

        else:
            arr[ind]=nums[j]**2
            j=j-1
        ind=ind-1
    
    return arr




def sortedSquares(nums):
    n = len(nums)
    start, end = 0, n-1
    res = [0]*n
    idx = n-1
    
    while end > -1 and idx >-1:
        if abs(nums[start]) > abs(nums[end]):
            res[idx] = nums[start] * nums[start]
            start +=1
        else:
            res[idx] = nums[end] * nums[end]
            end -= 1
        idx -= 1
    
    return res


def rotateArray1(arr,n):
    return  arr[-n:] + arr[:-n]
  


def rotateArray2(arr,n):
    k=0
    j=len(arr)-1
    

    for i in range(n):
         arr.insert(k,arr[j])
         arr.pop(j+1)
     
        
    return arr
        



arr=[0]
def moveZeros(arr):
    i=0
    j=len(arr)-1
    

    while i<=j :
        
        
        if arr[i] == 0:
            
            arr.insert(len(arr), arr[i])
            arr.pop(i)
            j=j-1
            
            
        elif arr[j]==0:
            arr.insert(len(arr), arr[j])
            arr.pop(j)
            i=i+1 
  
        else:
           
            j=j-1
    return arr




numbers =[-1,0]
target = -1
def twoSum(numbers,target):
    i=0
    j=len(numbers)-1
    addArr=[]

    while i <=j:
        if (numbers[i]+numbers[j]) >target:
            j-=1
        elif (numbers[i]+numbers[j])< target:
            i+=1
        elif (numbers[i]+numbers[j])==target:
            addArr=[i+1,j+1]
            
            break
        else:
            j-=1
           

s = ["H","a","n","n","a","h"]
def reverseString(s):
    i=0
    j=len(s)-1
    temp1=0
    temp2=0
    while i<=j:
        if i <= j :
            temp1=s[i]
            temp2=j
            s[i]=s[j]
            s[j]=temp1
            i+=1
            j-=1
            
s = "Let's take LeetCode contest"
#this method returns in reversed order
def reverseWords(s):
   
    arrS= list(s)
    i=0
    j=len(arrS)-1
    print(s.split())
    while i<=j:
        if i <= j :
            temp1=arrS[i]
            temp2=j
            arrS[i]=arrS[j]
            arrS[j]=temp1
            i+=1
            j-=1
            strng=[''.join(arrS)]
    return strng

#this method returns in original order        
def reverseWords2(s):
   
    arrS= s.split()
    master_array=[]
    for k in range(len(arrS)):
        sub_array=list(arrS[k])
        i=0
        j=len(sub_array)-1
        while i<=j:
            if i <= j :
                temp1=sub_array[i]
                sub_array[i]=sub_array[j]
                sub_array[j]=temp1
                i+=1
                j-=1
        strng=''.join(sub_array)
        master_array.append(strng)
        
    return ' '.join(master_array)   



