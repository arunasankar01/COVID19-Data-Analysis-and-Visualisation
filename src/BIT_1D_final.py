# -*- coding: utf-8 -*-
"""
Created on Sat May 1 09:39:37 2021

@author: aruna
"""

class BIT:
        
    def __init__(self,arr,n):
        """"Initializing the BIT in O(n*log(n)) time"""
        self.size=n
        self.array=arr
        self.BITarr = [0]*(self.size+1)
        for index in range(len(self.array)):
            self.update(index,self.array[index])
        print("BITarr: ",self.BITarr)
        
                
    def sum_query(self, index):
        """Computing sum of elements in range [0,idx] """
        index += 1
        result = 0
        while index>0:
            result += self.BITarr[index]
            index -= index & (-index)
        return result
    
    def update(self, index, value):
        """Adding a value to the index-th element"""
        
        index += 1
        while index <= len(self.array):
            self.BITarr[index] += value
            index += index & (-index)
    

    def range_sum(self, start_index, end_index):
        """Computing the range sum [start_index, end_index]"""
        
        return self.sum_query(end_index) - self.sum_query(start_index - 1)


if __name__ == '__main__':
    arr=[3,2,-1,6,5,4,-3,3,7,2,3]
    print("Array:",arr)
    bit = BIT(arr,len(arr))
    
    print("Prefix sum of elements in range [0,10]:", bit.sum_query(10))
    print("Prefix sum of elements in range [0,6]:", bit.sum_query(6))
    print("Range sum of elements in [2,5]:", bit.range_sum(2,5))
    print()
    bit.update(4, 2)
    print("Change the value of element at pos 4 to 7")
    new_array = [bit.range_sum(index, index) for index in range(len(arr))]
    print("Updated Array:",new_array)
    print()
    print("Prefix sum of elements in range [0,10]:", bit.sum_query(10))
    print("Prefix sum of elements in range [0,6]:", bit.sum_query(6))
    print("Range sum of elements in [2,5]:", bit.range_sum(2,5))
    print()  