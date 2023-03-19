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



class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
    
    def removeNode(self,n):
        slow=self.head
        fast=self.head
        count=1
        
        while count <=n:
            fast=fast.next
            count+=1
        if fast is None:
            self.head.value=self.head.next.value
            self.head.next=self.head.next.next
            return
        while fast.next is not None:
            slow= slow.next
            fast =fast.next
        slow.next=slow.next.next
    
    def display(self):
        temp = self.head
 
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        



# if __name__ == '__main__':
 
#     # Start with the empty list
#     llist = LinkedList()
 
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     fourth = Node(4)
#     fifth = Node(5)
 
#     llist.head.next = second  # Link first node with second
#     second.next = third  # Link second node with the third node
#     third.next = fourth
#     n=2 


#     print(llist.removeNode(n))
#     llist.display()
    


# Longest Substring Without Repeating Characters
#satisfies only 2 cases
def lengthOfLongestSubstring(s):
    print(s)
    count=1
    for i in range(len(s)-1):
        for j in range(i+1,len(s)-1):
            if s[i] == s[j]:
                print(s[i],s[j])
                break
            else:
                count+=1
    return print(count)

#satisfies all cases
def lengthOfLongestSubstring2(s):
    n=len(s)
    subset=""
    subset_len=0
    if len(s) == 1: return 1
    for i in range(n):
        if s[i] not in subset:
            subset+=s[i]
            print(subset)
            
        else:
           
            subset= subset[subset.index(s[i])+1:] + s[i]
            
        
        if len(subset)>subset_len:
            subset_len=len(subset)

    return subset_len
            

# Permutation in String

def toString(List):
    all_combs=[]
    all_combs.append(''.join(List))
    return pall_combs

def permute(s,l,r):
    s1=list(s)
    
    if l == r :
        return s1
    else:
        for i in range(l,r):
            print(i)
            s1[l], s1[i]=s1[i],s1[l]
            permute(s1, l+1, r)
            s1[l],s1[i]=s1[i],s1[l]

    
def checkInclusion2(s1,s2):
    l=0
    s = list(s1)
    r=len(s1)
    perms=[]
    is_perm=[]
    count=0
    
    def permute2(s,l,r):
        # s1=list(s)
    
        if l == r :
            return perms.append(''.join(s))
        else:
            for i in range(l,r):
                
                s[l], s[i]=s[i],s[l]
                permute2(s, l+1, r)
                s[l],s[i]=s[i],s[l]

    permute2(s,l,r)
    print(perms)
    for i in perms:
        if i in s2:
            is_perm.append(True)
        else:
            is_perm.append(False)
    # print(is_perm)
    for j in range(len(is_perm)):
        if is_perm[j] == True:
            count+=1
    
    if count > 0:
        return True
    else:
        return False


def checkInclusion(a,s2):
    
    prev_state={}
    temp=''
    
    
    if a not in s2:
        # print(a,s2,'first')
        temp=False
        prev_state.update({'False':False})
        

        return prev_state
    elif a in  s2:
        # print(a,s2,'second')
        temp=True
        prev_state.update({'True':True})
        return prev_state

   

def using_two_pointers(s1,s2):
    # print(s1,s2)
    len_s1=len(s1)
    len_s2= len(s2)
    i=0
    j=i+1
    end=0
    first_responder=False
    while i<j and end <= len_s2:
        # print(end)
        if s2[i] in list(s1):
            first_responder=True
            if s2[j] in list(s1):
                print(s2[i],s2[j],'found 2')
                return True
                break

            if j == len_s2-1:
                if first_responder == True:
                    return True
                    break
                else:
                    return False
                    break
            else:
                print('inside else')
                i+=1
                j+=1
        if i and j == len_s2:
                
                return False
                break
        else:
            print('outside else')
            i+=1
            j+=1
        end+=1
        
  

    
# sliding window appraoch only one that works perfectly

def sliding_window(s1,s2):
    if len(s1)> len(s2): return False
    s1_count=[0]*26
    s2_count=[0]*26

    for i in range(len(s1)):
        s1_count[ord(s1[i])-ord('a')]+=1
        s2_count[ord(s2[i])-ord('a')] +=1
    
    matches=0
    for i in range(26):
        matches += ( 1 if s1_count[i] == s2_count[i] else 0)

    l=0
    for r in range(len(s1),len(s2)):
        if matches == 26: return True

        index = ord(s2[r])-ord('a')
        s2_count[index]+=1
        if s1_count[index] == s2_count[index]:
            matches+=1
        elif s1_count[index]+1 == s2_count[index]:
            matches-=1
        
        index = ord(s2[l])-ord('a')
        s2_count[index]-=1
        if s1_count[index] == s2_count[index]:
            matches+=1
        elif s1_count[index]-1 == s2_count[index]:
            matches-=1
        l+=1

    return matches == 26




def findAnagrams(s,p):
    if len(p)> len(s): return []
    s_count= [0]*26
    p_count=[0]*26
    match_index=[]

    for i in range(len(p)):
        p_count[ord(p[i])-ord('a')] +=1
        s_count[ord(s[i])-ord('a')]+=1
        
    matches=0
    for i in range(26):
        matches += (1 if p_count[i] == s_count[i] else 0)
        if matches == 26:
            match_index.append(0)
    l=0
    for r in range(len(p),len(s)):
        index = ord(s[r])-ord('a')
        s_count[index]+=1
        if p_count[index] == s_count[index]:
            matches+=1
            print(s[r])
            if matches ==26:
                match_index.append(l+1)
    
        elif p_count[index]+1 == s_count[index]:
            matches-=1
            

        index = ord(s[l])-ord('a')
        s_count[index]-=1
        if p_count[index] == s_count[index]:
            matches+=1
            print(s[r])
            if matches ==26:
                match_index.append(l+1)
        elif p_count[index]-1 == s_count[index]:
            matches-=1
        l+=1
    return match_index

    
# s='acdcaeccde'
# p='c'
# print(findAnagrams(s, p))



def square_digits(num):
    len_num=str(num)
    i=0
    j=i+1
    concat=[]
    if num == 0 : return 0
    while j<len(len_num):
        
        concat.append(str(int(len_num[i])**2))
        concat.append(str(int(len_num[j])**2))
        i+=1
        j+=2
        
    return "".join(concat)


  
#Find Panagram
def is_panagram(s):
    s_lower=s.lower()
    
    s_count=[0]*26
    
    for i in range(len(s_lower)):
        if ord(s_lower[i])< 97:
            continue
        if ord(s_lower[i])>122:
            continue
        else:
            s_count[ord(s_lower[i])-ord('a')]+=1
    
    for i in range(len(s_count)):
        if s_count[i]== 0:
            return False
            break

    return True
            


    
# print(s_lower.replace("?", "").replace(",","").replace("!", "").replace(" ",""))

def DNA_strand(dna):
    i=0
    j=len(dna)
    list_dna=list(dna)
    complete_strand=[]
    for i in range(j):
        if dna[i] == "A":
            complete_strand.append("T")
        elif dna[i]=="T":
            complete_strand.append("A")
        elif dna[i]=="C":
            complete_strand.append("G")
        elif dna[i] == "G":
            complete_strand.append("C")
    return ''.join(complete_strand)

  
# def sum_two_smallest_numbers(numbers):
#     i=0
#     j=i+1
#     temp=None
#     while j <len(numbers):
#         print(i,j)
#         if numbers[i] >numbers[j]:
#             temp=numbers[j]
#             numbers[j]=numbers[i]
#             numbers[i]=temp
#             i+=1
#             j+=1
#         elif numbers[i]< numbers[j]:
#             i+=1
#             j+=1
        
#     return  numbers

def pig_it(text):
    split_txt= text.split()
    ay_txt=[]
    for i in split_txt:
        if len(i)==1:
            if ord(i)<65 or ord(i) >122:
                ay_txt.append(i)
            else:
                ay_txt.append(i+'ay')
        else:
            ay_txt.append(i[1:]+i[0]+'ay')
    return ' '.join(ay_txt)
        
#Valid Parenthesis
def valid_parenthesis(string):
    map_str=[0]*2
    count=0
    if len(string)==1:return False

    for i in range(len(string)):
        if ord(string[i]) == 40:
            map_str[0]+=1
        elif ord(string[i])== 41:
            map_str[1]+=1
        
    return True if map_str[0] == map_str[1] else  False

def valid_parenthesis2(string):
    list_str=list(string)
    res=[]

    for i in range(len(list_str)):
        if list_str[i] == 0:
            continue

        if ord(list_str[i]) == 40:
          
            for j in range(i+1,len(list_str)):
                if list_str[j] == 0:
                    continue
                if ord(list_str[j]) == 41:
                    list_str[i]=0
                    list_str[j]=0
                    res.append(string[i])
                    res.append(string[j])
                    

                    break
        if ord(string[i])==41:
            continue
    
    return True if len(res)== string.count('(')+string.count(')') else False
        

# )(()))

def solution(s):
    list_s=list(s)
    res=[]
    for i in range(0,len(s)):
        if list_s[i]==0:
            continue
        if len(s) %2 ==0:
            if i==len(s)-1:
                break
            else:
                res.append(list_s[i]+list_s[i+1])
                list_s[i]=0
                list_s[i+1]=0
        elif len(list_s) %2 != 0:
            if i == len(list_s)-1:
                res.append(list_s[i]+'_')
                break
            else:
                res.append(list_s[i]+list_s[i+1])
                list_s[i]=0
                list_s[i+1]=0      
    return res


def solution2(s):
    result = []
    if len(s) % 2:
        s += '_'
        print(s)
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
def wave(people):
    
    res=[]
    
    for i in range(len(people)):
        if people[i]==" ":
            continue
        else:
            list_people=list(people)
            list_people[i]=people[i].upper()
            res.append(''.join(list_people))
    return res

    
   

        
def withdraw(n):
    amount_50=0
    amount_20=0
    amount_100=0

    amount_100=n//100
    amount=n%100
    print(amount)
    
    if amount%50 != 0:
        amount_20=amount//20
    else:
        amount_50=amount//50
    print(amount_100,amount_50,amount_20)


def withdraw2(amount):
  #Init
  result = [0,0,0]
  
  # for 100
  remainder = amount % 100
  if (remainder == 10 or remainder == 30) and (amount >= 100): 
    result[0] = int(amount / 100)-1
    
  else: 
    result[0] = int(amount / 100)
  amount -= result[0] * 100
	
  #for 50
  if(amount % 20 == 0):
    result[1] =  0 
  elif(amount < 50): 
    result[1] = 0 
  else: 
    result[1] = 1
  amount -= result[1] * 50
	
  #for 20
  result[2] = int(amount / 20)
  return(result)      


def withdraw3(n):
    result=[0,0,0]
    amount = n%100
    if (amount%100 == 10 or amount%100==30 ) and amount>=100:
        result[0]=(n/2)-1
    else:
        result[0]=n//2
    amount-= result[0]*100


def withdraw4(n):
    n50 = 0
    n20, r = divmod(n, 20)
    print(n20,r)
    if r == 10:
        n20 -= 2
        n50 += 1
    n100, n20 = divmod(n20, 5)
    return [n100, n50, n20]


def check(n):
    n50=0
    n20 ,r = divmod(n, 20)
    if r==10:
        n20-=2
        n50+=1
    n100,n20=divmod(n20, 5)
    return [n100,n50,n20]


def cakes(recipe,availible):
    res=[]
    for i in availible:
        for j in recipe:
            
            if i==j:
                if recipe[j]>availible[i]:
                    continue
                else:
                    print(i)
                    res.append(availible[i]//recipe[j] if availible[i]>recipe[j]else recipe[j]//availible[i])
            else:
                continue
    return sorted(res)[0] if len(recipe)==len(res) else 0


def make_readable(s):
    print((s//60)//60)
    print((s//60)%60)
    print((s%60)%60)
    return str((s//60)//60).zfill(2)+":"+str((s//60)%60).zfill(2)+":"+str((s%60)%60).zfill(2)
   


def move_zeros(lst):
    n=len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]==0:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
def move_zeros2(lst):
    for i in lst:
        if i==0:
            lst.remove(i)
            lst.append(0)
    return lst    
            
  
lst= [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def is_interesting(number, awesome_phrases):
    lst_num=list(str(number))
    if len(str(number+2))< 3: 
        return 0 
    if number+2< 98:
        return 0
    if number == 98 or number == 99:
        return 1


    for i in range(0,3):
        print(number)
        temp_lst_num=''.join(lst_num)
        lst_num=list(str(int(temp_lst_num)+1 if i==2 else int(temp_lst_num)+i))
        lst_range_asc=[str(x) for x in range(int(lst_num[0]) , 10 if lst_num[-1] == '0' else int(lst_num[-1])+1)]
        lst_range_dec=[str(x) for x in range(int(lst_num[-1]),int(lst_num[0])+1)]
        print(temp_lst_num)
      
       
        
        if number+i in awesome_phrases:
            return 2 if i == 0 else 1 

        elif ''.join(lst_num[::-1]) == str(number+i):
            print('palin')
            return 2 if i == 0 else 1

        elif set(lst_num[1:]) == {'0'}:
            print('zeros')
            return 2 if i == 0 else 1
        
        elif ''.join(lst_num) == ''.join(lst_range_asc+['0']if lst_num[-1]=='0'else lst_range_asc):
            print('asc',i) 
            return 2 if i == 0 else 1

        elif ''.join(lst_num) == ''.join(reversed(lst_range_dec)):
            print('dec',i)
            return 2 if i == 0 else 1
        else:
            if i==2 : return 0


         # uses backtracking
        # lst_range_asc=[str(x) for x in range(int(lst_num[0]) , 10 if lst_num[-1] == '0' else int(lst_num[-1])+1)]
        # lst_range_dec=[str(x) for x in range(int(lst_num[-1]),int(lst_num[0])+1)]
    
    

        # if len(str(number))< 3: 
        #     return 0
        # if number in awesome_phrases: 
        #     return 2 
        # if ''.join(lst_num[::-1]) == str(number):
        #     print(count,'c') 
        #     return 2
        # if set(lst_num[1:]) == {'0'}: 
        #     return 2
        # if ''.join(lst_num) == ''.join(lst_range_asc+['0']if lst_num[-1]=='0'else lst_range_asc): 
        #     return 2
        # if ''.join(lst_num) == ''.join(reversed(lst_range_dec)):
        #     return 2
    
        # else:
        #     # print(count)
       
        #     return is_interesting(number+1, awesome_phrases)




def first_non_repeating_letter(string):
    for i in range(len(string)):
        count=0
        res=[]
       
        for j in range(i,len(string)):
            print(res,j)
            # print(j,'j')
            # print(string[j])
            if string[i]==string[j]:
                res.append(True)
                continue
            if string[i] != string[j]:
                res.append(False)
            if j == len(string)-1:
                if False in res:
                    return string[j]
                    break


                

        


def dirReduc(arr):
    for i in range(len(arr)):
        print(i)
        if i == len(arr)-1:
            break
        if arr[i] == "NORTH":
            if arr[i+1] == "SOUTH":
                arr[i],arr[i+1]=0,0
                continue
        elif arr[i] == "SOUTH":
            if arr[i+1] == "NORTH":
                arr[i],arr[i+1]=0,0
        elif arr[i] == "EAST":
            if arr[i+1] == "WEST":
                arr[i],arr[i+1]=0,0
                continue
        elif arr[i] == "WEST":
            if arr[i+1] == "EAST":
                arr[i],arr[i+1]=0,0
                continue
   
    temp=[k for k in arr if k != 0]
    for j in range(len(temp)):
        if j == len(temp)-1:
            break
        
        if temp[j] == "NORTH":
            if temp[j+1] == "SOUTH":
                temp[j],temp[j+1]=0,0
                continue
        elif temp[j] == "SOUTH":
            if temp[j+1] == "NORTH":
                temp[j],temp[j+1]=0,0
        elif temp[j] == "EAST":
            if temp[j+1] == "WEST":
                temp[j],temp[j+1]=0,0
                continue
        elif temp[j] == "WEST":
            if temp[j+1] == "EAST":
                temp[j],temp[j+1]=0,0
                continue
    temp2=[k for k in temp if k != 0]
        
    return temp2
def find_out_mr_wrong(conversation):
    mapped_form={}
    fact_chk=[]
    len_convo=len(conversation)
    for i in range(len_convo):
        get_name = conversation[i].split(":")
        get_pos = get_name[1]
        for j in range(len(get_pos)):
            if get_pos[j].isnumeric():
                
                mapped_form[get_name[0]] = get_pos[j]
            
        if i == len_convo-1:
            for k in get_name[1].split(" "):
                if k == 'behind':
                    fact_chk.insert(0,'Peter')
                    fact_chk.insert(1, get_name[1].split(" ")[-1][:-1])
                    
                if k == 'front':
                    fact_chk.insert(0, get_name[1].split(" ")[-1][:-1])
                    fact_chk.insert(1,'Peter')
    
    for key, value in mapped_form.items():

        for j in range(0,len(fact_chk),2):
            keys=list(mapped_form.keys())
            if key == fact_chk[j]:
                if list(mapped_form)[keys.index(key)+1] == fact_chk[j+1]:
                    return  'Tom' if  list(mapped_form).index(fact_chk[j+1]) != mapped_form[fact_chk[j+1]] else null

    
         

                    
                    
                
    
    print(mapped_form)
    print(fact_chk)





conversation=[
"John:I'm in 1st position.",
"Peter:I'm in 2nd position.",
"Tom:I'm in 1st position.",
"Peter:The man behind me is Tom."
]
print(find_out_mr_wrong(conversation))

    

    
 
   
    



