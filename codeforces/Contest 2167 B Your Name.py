import sys

input = sys.stdin.readline

def solve():
    try:
        q_string = input().strip(" ")
        if not q_string: return
        q = int(q_string)
    except ValueError: return

    for _ in range(q):
        n = int(input())
        str_array = input().split()
        
        name1 = sorted(str_array[0])
        name2 = sorted(str_array[1])

        if name1 == name2:
            print("YES")
        else:
            print("NO")
    

if __name__ == "__main__":
    solve()