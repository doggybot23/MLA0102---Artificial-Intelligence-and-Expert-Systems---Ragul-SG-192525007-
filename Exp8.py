import math

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):

    # Terminal node
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            False,
                            values,
                            alpha,
                            beta,
                            height)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break  # Beta Cutoff

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            True,
                            values,
                            alpha,
                            beta,
                            height)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break  # Alpha Cutoff

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Height of the game tree
height = int(math.log2(len(values)))

result = alphabeta(
    0,          # depth
    0,          # root index
    True,       # Maximizing player
    values,
    -math.inf,  # Alpha
    math.inf,   # Beta
    height
)

print("Optimal Value:", result)
