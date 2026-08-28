class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        water = 0
        left = 0
        right = n - 1
        left_height = 0
        right_height = 0

        while left <= right:
            l = height[left]
            r = height[right]

            if l <= r:
                if l >= left_height:
                    left_height = l
                else:
                    water += left_height - l
                left += 1
            else:
                if r >= right_height:
                    right_height = r
                else:
                    water += right_height - r
                right -= 1

        return water