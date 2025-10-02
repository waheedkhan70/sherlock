def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong Number!!!")
    else:
        print(f"{num} is not an Armstrong Number!!!")
