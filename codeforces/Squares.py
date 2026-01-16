import sys

input = sys.stdin.readline

def solve():
    try:
        t_string = input().strip()
        if not t_string: return
        t = int(t_string)
    except ValueError: return

    try:
        for _ in range(t):
            numArray = input().split()

            pivot = numArray[0]

            isSquare = "YES"

            for num in numArray:
                if num != pivot:
                    isSquare = "NO"
                    break
                else:
                    continue

            print(isSquare)
    except ValueError:
        return
    
if __name__ == "__main__":
    solve()