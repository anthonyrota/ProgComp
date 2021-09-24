from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)

        def encode_line(a, b):
            dY = b[1]-a[1]
            dX = b[0]-a[0]
            if dX == 0:
                return f"{a[0]:.10f},"
            if dY == 0:
                return f",{a[1]:.10f}"
            m = (b[1] - a[1]) / (b[0] - a[0])
            x_int = a[0] - a[1]/m
            y_int = a[1] - m*a[0]
            if x_int == 0 and y_int == 0:
                return f"{m:.10f}"
            return f"{x_int:.10f},{y_int:.10f}"
        lines = defaultdict(int)
        for i, a in enumerate(points):
            counted_lines = {}
            for j, b in enumerate(points):
                if j >= i:
                    break
                line = encode_line(a, b)
                if not line in counted_lines:
                    counted_lines[line] = True
                    lines[line] += 1
        return max(lines.values()) + 1
