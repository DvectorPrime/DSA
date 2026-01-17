"""
Docstring for Skibidus and Amogu
Coding challenge from CodeForces

Challenge Link: https://codeforces.com/contest/2065/problem/A
Time Complexity: O(N)
Space Complexity: O(N)
"""

import sys

input = sys.stdin.readline

def solve():
    try:
        t_string = input()
        if not t_string: return
        t = int(t_string)
    except ValueError:
        return 
    
    try:
        for _ in range(t):
            singular_word = input().strip("\n")
            plural_word = singular_word[:-2] + "i"

            print(plural_word)
    except ValueError:
        print("An error Occured")
        return

if __name__ == "__main__":
    solve()    