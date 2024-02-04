#!/usr/bin/env python
# coding: utf-8

# In[1]:


#created by Nidhi Choudhary


# ####  Brute Force Approach: O(n^2) 

# In[2]:


# Brute Force Approach: O(n^2) 
#     Step 1: Find all subarrays
#     Step 2: Find sum of all subarrays
#     Step 3: Find Max sum and print subarray


# In[3]:


# -2 4 7 -1 6 -11 14 3 -1 -6


# In[4]:


L = [int(x) for x in input("enter list with space").split(" ")]
d= {}
for i in range(0,len(L)):
    sub_array = []
    for j in range(i, len(L)):
        sub_array.append(L[j])
#         print(sum(sub_array), sub_array)
        sub_array_u = sub_array.copy() # imp -> else all values pointing to same list
        d[sum(sub_array)] = sub_array_u
    
max_sum = max(d.keys())
# print(d)
for i in d:
    if i == max_sum:
        print(i, d[i])


# #### Optimized Appoach: O(n)

# In[5]:


# Optimized Appoach
# Kadane's algorithm Approach:
#     Check if Adding Element Increases Sum:
#         If adding the current element to the previous subarray results in a sum greater than the element itself-> update curr_sum
#         Else create new subarray starting from the new element
#     Evaluate and Update:
#         If the current sum is greater than the best sum encountered so far -> update best sum/array


# In[6]:


L = [int(x) for x in input("enter list with space").split(" ")]

# print(L)
# L = [-2,4,7,-1,6,-11,14,3,-1,-6]
# -2 4 7 -1 6 -11 14 3 -1 -6
curr_sum = 0
curr_array = []

best_sum = L[0]
best_array = []

for i in L:
    # if adding new element to prev array is yeilding better sum compared to the new elements alone
    #yes -> add to the current sum and append in the sub array
    if curr_sum + i > i: 
        curr_sum +=i
        curr_array.append(i)
    #no -> update current sum, clear existing subarray create new sub array
    else:
        curr_sum = i # 
        curr_array.clear()
        curr_array.append(i)
    print(curr_sum, curr_array)
    
    if curr_sum > best_sum:
        best_sum = curr_sum
        best_array = curr_array.copy() # imp -> else all values pointing to same list
print("Best subarray sum is : ", best_sum, best_array)

