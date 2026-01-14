import sys
import math

input = sys.stdin.readline

def solve():
    try:
        t_str = input().strip()
        if not t_str: return 
        t = int(t_str)
    except ValueError: return

    for _ in range(t):
        try:
            n = int(input())
            
            a = list(map(int, input().split()))

            overall_gcd = a[0]
            for i in range(1, n):
                overall_gcd = math.gcd(overall_gcd, a[i])
            
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            
            found = False
            for p in primes:
                if overall_gcd % p != 0:
                    print(p)
                    found = True
                    break
            
            if not found:
                print(-1)
                
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    solve()