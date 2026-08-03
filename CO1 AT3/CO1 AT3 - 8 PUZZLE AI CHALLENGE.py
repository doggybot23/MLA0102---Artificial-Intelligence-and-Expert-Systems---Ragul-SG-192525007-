import heapq

def run_8_puzzle():
    print("\n" + "="*30)
    print("--- 8-Puzzle (A* Algorithm) ---")
    print("="*30)
    print("# 8-Puzzle:")
    print("# 1-8 = Numbered Tiles")
    print("# 0   = Empty Space")
    print("="*30 + "\n")
    
    initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
    goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    def manhattan(state):
        dist = 0
        for i in range(9):
            val = state[i]
            if val != 0:
                target_idx = goal_state.index(val)
                tr, tc = divmod(target_idx, 3)
                cr, cc = divmod(i, 3)
                dist += abs(tr - cr) + abs(tc - cc)
        return dist
        
    def print_state(state, prefix="  "):
        print(f"{prefix}{state[0]} {state[1]} {state[2]}")
        print(f"{prefix}{state[3]} {state[4]} {state[5]}")
        print(f"{prefix}{state[6]} {state[7]} {state[8]}\n")
        
    print("Solving with A* search... Please wait.\n")

    pq = []
    # Store path as a list of tuples: (move_description, state)
    heapq.heappush(pq, (manhattan(initial_state), 0, 0, initial_state, [("Initial State", initial_state)]))
    visited = set()
    counter = 1 
    
    move_names = {
        (-1, 0): "Moved Empty Space UP",
        (1, 0):  "Moved Empty Space DOWN",
        (0, -1): "Moved Empty Space LEFT",
        (0, 1):  "Moved Empty Space RIGHT"
    }
    
    while pq:
        f, _, g, current, path = heapq.heappop(pq)
        
        if current == goal_state:
            print(f"✨ Goal reached in {g} moves!\n")
            print("--- Step-by-Step Path ---")
            for idx, (move_str, s) in enumerate(path):
                if idx == 0:
                    print(f"Start -> {move_str}:")
                else:
                    print(f"Step {idx} -> {move_str}:")
                print_state(s)
            return
            
        if current in visited:
            continue
        visited.add(current)
        
        zero_idx = current.index(0)
        zr, zc = divmod(zero_idx, 3)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                new_state = list(current)
                new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
                new_state = tuple(new_state)
                
                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan(new_state)
                    move_str = move_names[(dr, dc)]
                    heapq.heappush(pq, (new_f, counter, new_g, new_state, path + [(move_str, new_state)]))
                    counter += 1
                    
    print("No solution found.")

if __name__ == "__main__":
    run_8_puzzle()
