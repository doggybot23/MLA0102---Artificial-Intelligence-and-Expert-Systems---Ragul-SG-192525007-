import math

tree = [
    [[3,5,6],[9,1,2],[0,-1,4]],
    [[7,5,8],[6,2,3],[4,0,-2]],
    [[1,2,3],[5,-1,2],[6,4,7]]
]

def minimax(node, depth, alpha, beta, maximizing):

    if depth == 3:
        return node

    if maximizing:
        value = -math.inf
        for child in node:
            value = max(value, minimax(child, depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    else:
        value = math.inf
        for child in node:
            value = min(value, minimax(child, depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

result = minimax(tree, 0, -math.inf, math.inf, True)

print("Best Move Value:", result)
