def odd_numbers(n):
    pass



def even_numbers(n):
    pass



def fibonacci_sequence(n):
    pass



def prime_numbers(n):
    pass


def print_menu():
    print("1. Odd numbers")
    print("2. Even numbers")
    print("3. Fibonacci sequence")
    print("4. Prime numbers")


def main():
    print_menu()
    function = int(input("Your choice: "))
    maxNum = int(input("Enter max number: "))
    if function == 1:
        odd_numbers(maxNum)
    elif function == 2:
        even_numbers(maxNum)
    elif function == 3:
        fibonacci_sequence(maxNum)
    elif function == 4:
        prime_numbers(maxNum)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
