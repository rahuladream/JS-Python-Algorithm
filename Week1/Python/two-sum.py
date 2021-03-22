class Solution:
    def twoSum(self, nums, target):
        
        for n1 in range(len(nums)):
            for n2 in range(n1):
                if nums[n1] + nums[n2] == target:
                    return [n1, n2]
    
    def twoSum(self, nums, target):
        pair = dict()
        index = 0
        for n in nums:
            if n in pair:
                return [pair[n], index]
            else:
                pair[target - n] = index
                index += 1


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([3,3], 6))