#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#created by Nidhi Choudhary


# #### Solution

# In[ ]:


# 3
# 4 1 2 3 4
# 5 1 1 1 1 1
# 5 1 3 5 7 9


# In[33]:


from typing import List

class Solution:
     
    def getCumulativeSum(self, arr: List[int]) -> List[int]:
        # add your logic here
        list_res = list()
        sum = 0;
        for i in arr:
            sum+=i
            list_res.append(sum)
        return list_res
            
               
        
t= int(input(" no. of test cases "))
for i in range(0, t):
    l_all = [int(k) for k in input(" enter len of list followed by the list ").split(" ")]
    n = l_all[0]
    l = l_all[1:]
    if len(l)==n:
        sol_instance = Solution()
        res_l = sol_instance.getCumulativeSum(l)
        print(res_l)

