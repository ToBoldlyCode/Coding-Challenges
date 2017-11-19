# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #recursive solution
        #if nums is not null
        if nums:
            #find the index of the maximum number in the array
            i = nums.index(max(nums))
            #make that number the root
            root = TreeNode(nums[i])
            #slice the array up to root index for the left subtree
            root.left = self.constructMaximumBinaryTree(nums[:i])
            #slice the array past the root index for the right subtree
            root.right = self.constructMaximumBinaryTree(nums[i+1:])
            #return the root
            return root
        #else return null