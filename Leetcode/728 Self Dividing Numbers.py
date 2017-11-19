class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer_list = []
        
        for number in range(left, right+1):
            self_div = True
            
            for digit in str(number):
                if int(digit) == 0 or number%int(digit) != 0:
                    self_div = False
                    
            if self_div == True:
                answer_list.append(int(number))
                
        return answer_list