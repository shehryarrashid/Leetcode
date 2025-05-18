'''
Squares of a sorted array:

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

'''

# Two pointer approach

class Solution:

    # sqares the array
    
    def sorted_squares(self,num: list[int]) -> list[int]:
       
        p = self.positive_index(self,num)
        n = p - 1
        sorted = []

        while n >= 0 and p < len(num):
        
            if(num[n]**2 < num[p]**2):

                sorted.append(num[n]**2)
                n -= 1
            else:
                sorted.append(num[p]**2)
                p += 1
        
        # Handling the missing values

        while p < len(num):
            sorted.append(num[p]**2)
            p += 1
        
        while n >= 0:
            sorted.append(num[n]**2)
            n -= 1

        return sorted

    # Gets the index where the positive number begin

    def positive_index(self,num: list[int]) -> int:
        i = 0
        while(i < len(num) and num[i] < 0):
            i += 1
        
        return i

    def main(self):
        print(self.sorted_squares(self,[-4,-1,0,2,3,9,10]))

Solution.main(Solution)