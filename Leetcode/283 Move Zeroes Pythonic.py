'''
The classic solution for in-place array manipulation is by using two pointers, but Python is amazing.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for count in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)