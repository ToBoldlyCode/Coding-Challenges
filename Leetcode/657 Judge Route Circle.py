class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        chart = {
            'R':[1, 0],
            'L':[-1, 0],
            'U':[0, 1],
            'D':[0, -1]
        }
        position = [0,0]
        for move in moves:
            update = chart[move]
            position = [position[0]+update[0], position[1]+update[1]]
            
        return position == [0,0]