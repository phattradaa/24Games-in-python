import sys
import pandas as pd
sys.setrecursionlimit(2000000)

class Solution(object):
    def judge_point_24(self, nums):
        if len(nums) == 1:
            return nums[0] == 24 or abs(nums[0] - 24.0) <= 0.1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                indexes = set([x for x in range(len(nums))])
                indexes.remove(i)
                indexes.remove(j)
                operations = []
                operations.append(float(nums[i]) + float(nums[j]))
                operations.append(float(nums[i]) - float(nums[j]))
                operations.append(float(nums[j]) - float(nums[i]))
                operations.append(float(nums[i]) * float(nums[j]))
                if nums[j] != 0:
                    operations.append(float(nums[i] / float(nums[j])))
                if nums[i] != 0:
                    operations.append(float(nums[j] / float(nums[i])))
                next_items = [nums[index] for index in indexes]
                for x in operations:
                    if self.judge_point_24(next_items + [x]) == True:
                        return True
        return False


def main():
    nums = []
    nums_True = []
    nums_False = []
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    nums.append([i, j, k, l])
    # print(nums)
    for i in range(len(nums)):
        twentyfour = Solution()
        if twentyfour.judge_point_24(nums[i]) == True: 
            nums_True.append(nums[i])
        else : 
            nums_False.append(nums[i])
    
    frame_True = {'Number':nums_True}
    true = pd.DataFrame(frame_True)
    true.to_csv("AnswerTrue.csv",header=True,index=False)
    frame_False = {'Number':nums_False}
    false = pd.DataFrame(frame_False)
    false.to_csv("AnswerFalse.csv",header=True,index=False)
    
        
main()

