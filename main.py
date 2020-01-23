class Solution:
    def __init__(self):
        self.prevItemsDict = {}

    def check(self, checkNumber: int)->bool:
        num = str(checkNumber)

        if self.prevItemsDict.get(num) == True:
            return False

        self.prevItemsDict[num] = True

        sum = 0
        for value in num:
            sum += int(value) * int(value)

        return True if sum == 1 else self.check(sum)

    def isHappy(self, n: int) -> bool:

        return self.check(n)


my = Solution()

ans = my.isHappy(19)
print('ans', ans)

# Runtime: 32 ms, faster than 65.84% of Python3 online submissions for Happy Number.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Happy Number.
