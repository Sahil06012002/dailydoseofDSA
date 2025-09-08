from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)) :
            currX , currY = points[i]
            for j in range(len(points)) :
                if j == i :
                    continue
                checkX, checkY = points[j]
                insideRect = False
                if checkX <= currX and checkY >= currY :
                    for k in range(len(points)) :
                        if k == j or k == i :
                            continue
                        rectX , rectY = points[k]
                        # point lies inside the rect including the boundries
                        if checkX <= rectX <= currX and currY <= rectY <= checkY :
                            insideRect = True
                            break

                    if not insideRect :
                        count += 1
        return count


        