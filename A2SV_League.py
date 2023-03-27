def possibleWinners(ratings, l, r, max_diff):
    if r == l:
        return [(ratings[l], l + 1)]
    mid = l + (r - l) // 2
    left = possibleWinners(ratings, l, mid, max_diff)
    right = possibleWinners(ratings, mid + 1, r, max_diff)
    left_min = min(left)
    right_min = min(right)
    next = []
    for player in left:
        if player[0] - right_min[0] >= max_diff or player[0] - right_min[0] >= -max_diff:
            next.append(player)
            
    for player in right:
        if player[0] - left_min[0] >= max_diff or player[0] - left_min[0] >= -max_diff:
            next.append(player)
    return next
 
n, max_diff = map(int, input().split())
ratings = list(map(int, input().split()))
possible_winners = possibleWinners(ratings, 0, len(ratings) - 1, max_diff)
indices = list(zip(*possible_winners))[1]
for indx in indices:
    print(indx, end=" ")