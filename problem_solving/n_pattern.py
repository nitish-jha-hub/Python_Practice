# n = int(input("Enter the number of asterisks: "))
# for i in range(n):
#     print("*", end="")


# for i in range(7):
#     for j in range(7):
#         if j == 3 or i == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
def print_N(number_of_lines):
    for i in range(number_of_lines):
        for j in range(number_of_lines):
            if j == 0 or j == number_of_lines-1 or i == j:
              print("*", end="")
            else:
                print(" ", end="")
        print()

print_N(11)