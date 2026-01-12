def findMinStep(coordinate_distance):
    if coordinate_distance % 5 == 0:
        return coordinate_distance // 5 
    else:
        return (coordinate_distance // 5) + 1
    
if __name__ == "__main__":
    print(findMinStep(int(input("Enter distance from x = 0: "))))