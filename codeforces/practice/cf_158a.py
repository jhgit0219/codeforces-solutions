import sys

def solve(tokens):
    # --- PARSE INPUT HERE ---
    # Example: read an integer
    # n = int(next(tokens))
    
    # Example: read a list of integers
    # arr = [int(next(tokens)) for _ in range(n)]
    
    # --- LOGIC HERE ---
    n = int(next(tokens))
    k = int(next(tokens))-1
    scores = [int(next(tokens)) for _ in range(n)]
    l = len(scores)
    threshold = scores[k]
    count = k+1
    if threshold == 0:
        while scores[k] == 0 and k >= 0:
            k -= 1
            count -= 1
            if count == 0 or scores[k] != 0:
                break
    else:
        for i in range(k+1,l):
            if scores[i] == threshold:
                count+=1
            else:
                break
    
    print(count)
 

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        tokens = iter(input_data)

        t = 1                  # Use this line for 1 testcase
        # t = int(next(tokens))  # Uncomment this line for multiple testcases
        
        for _ in range(t):
            solve(tokens)

