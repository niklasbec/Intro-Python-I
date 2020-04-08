# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if num == 0:
        return "0 is not even nor uneven"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Uneven"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

print(is_even(num))



