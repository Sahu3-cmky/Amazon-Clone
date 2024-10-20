def take_n_natural_numbers(n):
    natural_numbers = list(range(1, n + 1))
    return natural_numbers
n = int(input("Enter the number of natural numbers: "))
numbers = take_n_natural_numbers(n)

print("The first", n, "natural numbers are:", numbers)
