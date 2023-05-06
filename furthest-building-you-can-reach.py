class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        by_ladder = []
        by_bricks = []
        by_bricks_sum = 0

        prev_BLDG = 0
        BLDG = 1
        while BLDG < len(heights) and len(by_ladder) <= ladders and by_bricks_sum <= bricks:
            if heights[prev_BLDG] < heights[BLDG]:
                heappush(by_ladder, heights[BLDG] - heights[prev_BLDG])
                if len(by_ladder) > ladders:
                    h = heappop(by_ladder)

                    if by_bricks_sum + h <= bricks:
                        by_bricks.append(h)
                        by_bricks_sum += h
                    else:
                        return prev_BLDG
            prev_BLDG += 1
            BLDG += 1

        return prev_BLDG