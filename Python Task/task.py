def pattern(rows, cols):
    top = "  __" 
    middle = " /  \\"
    bottom = "/    \\"
    base = "\\__  /"
    bottom_base = " \\__/"

    for r in range(rows):

        for c in range(cols):
            print(top, end="")
        print()

        for c in range(cols):
            print(middle, end="")
        print()

        for c in range(cols):
            print(bottom, end="")
        print()

        for c in range(cols):
            print(base, end="")
        print()
    for c in range(cols):
        print(bottom_base, end="")
    print()
print("Sample-1")
pattern(4, 7)
print("\nSample-2")
pattern(3, 5)