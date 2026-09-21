from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        """
        easy | LC #109
        """
        if not nums:
            return 0
        seen = set()
        longest = 0
        for n in nums:
            if n - 1 not in seen:
                curr = n
                streak = 1
                while curr + 1 in seen:
                    curr += 1
                    streak += 1
                longest = max(longest, streak)
            seen.add(n)
        return longest


if __name__ == "__main__":
    print(Solution().solve([100, 4, 200, 1, 3, 2]))
