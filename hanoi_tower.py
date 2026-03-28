def hanoi(n, source, auxiliary, destination):
    global move_count
    
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        move_count += 1
        return
    hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    move_count += 1
    hanoi(n-1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))

if n <= 0:
    print("Invalid input! Number must be positive.")
else:
    move_count = 0
    print("Move Sequence:\n")
    hanoi(n, "A", "B", "C")
    
    print("Total Moves:", move_count)
    print("Formula: 2^n - 1")
    print("Time Complexity: O(2^n)")