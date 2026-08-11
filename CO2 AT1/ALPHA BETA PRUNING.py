import math

# Minimax with Alpha-Beta Pruning
def minimax(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            val = minimax(depth + 1,
                          node_index * 2 + i,
                          False,
                          values,
                          alpha,
                          beta,
                          max_depth)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Pruned at MAX node")
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = minimax(depth + 1,
                          node_index * 2 + i,
                          True,
                          values,
                          alpha,
                          beta,
                          max_depth)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print("Pruned at MIN node")
                break

        return best


# Terminal node values (example game tree)
values = [3, 5, 6, 9, 1, 2, 0, -1]

tree_depth = 3

result = minimax(0, 0, True, values, -math.inf, math.inf, tree_depth)

print("\nBest value for MAX player:", result)