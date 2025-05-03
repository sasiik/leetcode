class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Ошибки:
        # 1. Двигать оба пойтнера сразу - глупость
        # 2. Может срезать сразу все потенциальные решения,
        #    как это было в кейсе [10, 9, 8, 7, ..., 1] (если пойнтер прыгнет сразу далеко)
        # 3. By only updating when you see a strictly taller bar,
        #    you skip all the intermediate positions. Sometimes the best container
        #    is formed by a slightly shorter bar that’s very far from
        #    the opposite boundary—and you never even consider those pairs.

        l = 0
        r = len(height) - 1
        l_touch = 1
        r_touch = len(height) - 2
        v_max = min(height[l], height[r]) * (r-l)
        while l_touch < r_touch:
            if height[l_touch] > height[l]:
                area_from_r = abs(l_touch - r) * \
                    min(height[r], height[l_touch])
                area_from_l = abs(l_touch - l) * \
                    min(height[l_touch], height[l])
                if area_from_r >= area_from_l:
                    l = l_touch
                else:
                    r = l_touch
                v_max = max(v_max, min(height[l], height[r]) * abs(r-l))
            if height[r_touch] > height[r]:
                area_from_r = abs(r_touch - r) * \
                    min(height[r], height[r_touch])
                area_from_l = abs(r_touch - l) * \
                    min(height[r_touch], height[l])
                if area_from_r >= area_from_l:
                    l = r_touch
                else:
                    r = r_touch
                v_max = max(v_max, min(height[l], height[r]) * abs(r-l))
            l_touch += 1
            r_touch -= 1
        return v_max


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
print('-----------------------------')
print(sol.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(sol.maxArea([8, 7, 2, 1]))
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
print('-----------------------------')
print(sol.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(sol.maxArea([8, 7, 2, 1]))
print(sol.maxArea([76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111, 115, 76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20, 185,
      171, 23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125, 143, 12, 76, 192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81, 163, 146, 75, 92, 198, 126, 191]))
