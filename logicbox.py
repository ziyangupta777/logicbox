print("Menu")
print("1. Pattern")
print("2. Number Analyzer")
print("3. Exit")

choice = int(input("Enter choice: "))

# Pattern
if choice == 1:
    n = int(input("Enter rows: "))

    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

# Number Analyzer
elif choice == 2:
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    sum = 0

    for num in range(start, end+1):

        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")

        sum = sum + num

    print("Total Sum =", sum)

# Exit
elif choice == 3:
    print("Program Exit")

else:
    pass