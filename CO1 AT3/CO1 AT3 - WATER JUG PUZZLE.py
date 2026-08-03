from collections import deque

def run_water_jug():
    print("\n" + "="*45)
    print("--- Water Jug (11L & 9L to 8L) ---")
    print("="*45)
    print("# Water Jug:")
    print("# (x, y) = (Amount in 11L jug, Amount in 9L jug)")
    print("# Target = 8L in either jug")
    print("="*45 + "\n")
    
    capA, capB, target = 11, 9, 8
    queue = deque([((0, 0), [])])
    visited = {(0, 0)}
    
    print(f"Jugs: {capA}L and {capB}L. Target: {target}L in either jug.\n")
    
    while queue:
        (a, b), steps = queue.popleft()
        
        if a == target or b == target:
            print(f"Solution found in {len(steps)} steps!\n")
            print(f"{'Step':<6} | {'Action':<22} | {'11L Jug':<8} | {'9L Jug':<7}")
            print("-" * 53)
            print(f"{'0':<6} | {'Initial State':<22} | {'0L':<8} | {'0L':<7}")
            for i, (action, (st_a, st_b)) in enumerate(steps, 1):
                print(f"{i:<6} | {action:<22} | {str(st_a)+'L':<8} | {str(st_b)+'L':<7}")
            print("-" * 53)
            return
            
        transitions = [
            (capA, b, f"Fill 11L jug"),
            (a, capB, f"Fill 9L jug"),
            (0, b, f"Empty 11L jug"),
            (a, 0, f"Empty 9L jug"),
            (a - min(a, capB - b), b + min(a, capB - b), f"Pour 11L to 9L"),
            (a + min(b, capA - a), b - min(b, capA - a), f"Pour 9L to 11L")
        ]
        
        for na, nb, action in transitions:
            if (na, nb) not in visited:
                visited.add((na, nb))
                queue.append(((na, nb), steps + [(action, (na, nb))]))
                
    print("No solution possible.")

if __name__ == "__main__":
    run_water_jug()
