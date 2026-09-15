import sys

def solve(tokens):
    # --- PARSE INPUT HERE ---
    # Example: read an integer
    # n = int(next(tokens))
    
    # Example: read a list of integers
    # arr = [int(next(tokens)) for _ in range(n)]
    
    # --- LOGIC HERE ---
    n = int(next(tokens)) * int(next(tokens))
    print(n//2)

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        tokens = iter(input_data)

        t = 1                  # Use this line for 1 testcase
        # t = int(next(tokens))  # Uncomment this line for multiple testcases
        
        for _ in range(t):
            solve(tokens)

