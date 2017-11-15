class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique = set(candies)
        num_unique = len(unique)
        half_candies = len(candies)/2
        
        if num_unique < half_candies:
            return num_unique
        else:
            return half_candies