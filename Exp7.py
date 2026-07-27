import math

# Minimax Function
def minimax(depth, nodeIndex, isMax, scores, height):

    # Terminal node
    if depth == height:
        return scores[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )

# Leaf node scores
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Height of the game tree
height = int(math.log2(len(scores)))

print("Optimal Value:", minimax(0, 0, True, scores, height))
