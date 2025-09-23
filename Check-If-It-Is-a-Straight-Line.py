class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope should be the same, where y=mx+b
        # slope is (y2-y1)/(x2-x1)
        if(coordinates[1][0] - coordinates[0][0]) == 0:
            for i in coordinates:
                if i[0] != coordinates[0][0]:
                    return False
            return True
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[0][0]) == 0:
                return False
            if ((coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])) != slope:
                return False
        return True