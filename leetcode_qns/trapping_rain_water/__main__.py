class Solution:
    def trap(self, height: List[int]) -> int:
        # find global maximum
        global_max = 0
        for h in height:
            global_max = max(global_max, h)
        if global_max == 0:
            return 0
        # find first and last global maximum
        first_max = -1
        last_max = -1
        for i, h in enumerate(height):
            if h == global_max:
                if first_max == -1:
                    first_max = i
                last_max = i
        # calculate non-trapped up to first maximum
        non_trapped_area = 0
        local_max = 0
        for i in range(0, first_max + 1):
            h = height[i]
            if h > local_max:
                non_trapped_area += i * (h - local_max)
                local_max = h
        # add non-trapped after last maximum
        local_max = 0
        height_len = len(height)
        for i in range(height_len - 1, first_max - 1, -1):
            h = height[i]
            if h > local_max:
                non_trapped_area += (height_len - 1 - i) * (h - local_max)
                local_max = h
        # note in the middle of the two maximums, all the water is trapped
        # also note the case where there is only one maximum, this still holds
        return global_max * height_len - non_trapped_area - sum(height)
