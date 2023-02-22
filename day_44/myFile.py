from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle[1:]
        self.array = rectangle[0][0]
        self.__doanywork()


    def __doanywork(self):
        myList = []
        for item in self.rectangle:
            if len(item) == 5:
                self.updateSubrectangle(*item)
                myList.append(None)
            elif len(item) == 2:
                myList.append(self.getValue(*item))
        print(myList)


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.array[i][j] = newValue
    

    def getValue(self, row: int, col: int) -> int:
        return self.array[row][col]
        




# myArray = [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
# instance = SubrectangleQueries(myArray)





# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)




# Input
# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
# Output
# [null,1,null,5,5,null,10,5]
# Explanation
# SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
# // The initial rectangle (4x3) looks like:
# // 1 2 1
# // 4 3 4
# // 3 2 1
# // 1 1 1
# subrectangleQueries.getValue(0, 2); // return 1
# subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
# // After this update the rectangle looks like:
# // 5 5 5
# // 5 5 5
# // 5 5 5
# // 5 5 5 
# subrectangleQueries.getValue(0, 2); // return 5
# subrectangleQueries.getValue(3, 1); // return 5
# subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
# // After this update the rectangle looks like:
# // 5   5   5
# // 5   5   5
# // 5   5   5
# // 10  10  10 
# subrectangleQueries.getValue(3, 1); // return 10
# subrectangleQueries.getValue(0, 2); // return 5



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [letter for letter in s]
        word2 = [letter for letter in t]
        for let in s:
            if let not in word2:
                return False
            else:
                word1.remove(let)
                word2.remove(let)
        return word1 == word2

s = "dgqztusjuu"
t = "dqugjzutsu"
a = Solution()
print(a.isAnagram(s, t))