class Solution:
    def rotate(self, matrix): 
    
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for x in range(len(matrix)):
            matrix[x] = matrix[x][::-1]

matr = [[1,2,3],
        [4,5,6],
        [7,8,9]]


obj = Solution()
obj.rotate(matr)

print(matr)

from random import randint
class Solution:
    def twoSum(self, nums, m): 
        
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == m:
                    return ([i,j])
                  
nums = [randint(2,20) for _ in range(1,10)]
m = 9

obj = Solution()
result = obj.twoSum(nums, m)
print(nums)
print(result)