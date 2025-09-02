# Your task for today is to build a multiplication table grid using nested for loops. This project will strengthen your understanding of nested iteration and help you practice basic formatting in printed output.

# 📝 Project Task

# The program should:

# Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
# Upgrade to paid

#     Ask the user for a table size (e.g., 5 means a 5x5 table).

#     Use nested for loops to generate and display the multiplication table.

#     Format the table for aligned columns using str.ljust() or f-strings.

# Bonus (optional):

#     Highlight the diagonal (e.g., square numbers).

#     Allow the user to choose between rows × columns or columns × rows.

# This project helps you visualize how outer and inner loops interact — a key concept for working with grids, 2D arrays, or drawing shapes.
# 📌 Expected Output

# Example for size = 5:

	
#     1   2   3   4   5
#     2   4   6   8  10
#     3   6   9  12  15
#     4   8  12  16  20
#     5  10  15  20  25

# Multiplication Table with Colored Diagonal



# ---------------------------------------------------------------------- Answer -----------------------------------------------------------------------------------

# ------------------------------------------------------------------- BEGINNER LEVEL ------------------------------------------------------------------------------

# Let's ask the table size from the user

# tab_size = int(input("Input The Table Size :- "))

# for i in range(1, tab_size + 1):
#     for j in range(1, tab_size + 1):
#         if i == j:

#             # Highlighting the diagonal elements (square numbers)

#             print(f"\033[1;32m{i * j:4}\033[0m", end="")
#         else:
#             print(f"{i * j:4}", end="")
#     print()

# ------------------------------------------------------------- ADVANCED LEVEL (Bonus Questions )--------------------------------------------------------------------

# Let's ask the table size from the user e.g. row and column

row = int(input("Input The Number of Rows :- "))
col = int(input("Input The Number of Columns :- "))

orient = int(input("Choose Orientation - 1 for Rows x Columns, 2 for Columns x Rows: "))

if orient == 1:
    print(f"\nMultiplication Table of {row} rows x {col} columns:\n")
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if i == j:
                # Highlighting the diagonal elements (square numbers)
                print(f"\033[1;32m{i * j:4}\033[0m", end="")
            else:
                print(f"{i * j:4}", end="")
        print()

elif orient == 2:
    print(f"\nMultiplication Table of {col} columns x {row} rows:\n")
    for i in range(1, col + 1):
        for j in range(1, row + 1):
            if i == j:
                # Highlighting the diagonal elements (square numbers)
                print(f"\033[1;32m{i * j:4}\033[0m", end="")
            else:
                print(f"{i * j:4}", end="")
        print()

else:
    print("Invalid Orientation Choice. Please choose 1 or 2.")