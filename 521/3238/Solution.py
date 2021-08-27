from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count = count + 1
                result = max(result, count)

        return count


if __name__ == '__main__':
    # begin
    nums = [1, 1, 0, 1, 1, 1]
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums))