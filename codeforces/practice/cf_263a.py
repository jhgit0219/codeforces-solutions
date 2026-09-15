import sys

def solve(tokens):
    # --- PARSE INPUT HERE ---
    # Example: read an integer
    # n = int(next(tokens))
    
    # Example: read a list of integers
    # arr = [int(val) for val in tokens]
    
    # --- LOGIC HERE ---
    for i, val in enumerate(tokens):
        if val == '1':
            c = (i % 5) + 1
            r = (i // 5) + 1
            print(abs(3 - c) + abs(3 - r))
            break

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        tokens = iter(input_data)

        t = 1                  # Use this line for 1 testcase
        # t = int(next(tokens))  # Uncomment this line for multiple testcases
        
        for _ in range(t):
            solve(tokens)

