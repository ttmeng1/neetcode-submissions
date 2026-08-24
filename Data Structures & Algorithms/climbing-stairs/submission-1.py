class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i: int, n: int, memo: List[int]):
        if i > n:
            # if step goes past target, doesn't count
            return 0
        elif i == n:
            return 1
        # can move up by either 1 step or 2
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]