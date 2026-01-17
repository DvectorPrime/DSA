"""
Docstring for Skibidus and Ohio
Coding challenge from CodeForces

Challenge Link: https://codeforces.com/contest/2065/problem/B
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
    
    for _ in range(t):
        word = input().strip("\n")

        currentLetter = ""
        duplicateFound = False
        for letter in word:
            if letter == currentLetter:
                duplicateFound = True
                print(1)
                break
            else:
                currentLetter = letter
                continue
        
        if not duplicateFound: print(len(word))


if __name__ == "__main__":
    solve()