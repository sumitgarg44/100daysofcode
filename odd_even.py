num = int(input(f"\nEnter a whole number to check: "))
is_even = num % 2

if is_even == 0:
    print(f"\n{num} is an even number.")
else:
    print(f"\n{num} is an odd number.")
