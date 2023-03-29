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
    z = True
    while (z) : 
        x = input("Enter your number:").split(" ")
        y = []
        for i in range(len(x)): 
            a = int(x[i])
            y.append(a)
        twentyfour = Solution()
        print(twentyfour.judge_point_24(y))
        
        e = input("Exit:")
        if e == "Yes": 
            z = False 
            break
main()
