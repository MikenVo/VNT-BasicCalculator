def main():
    x = int(input("Type the first number: ").strip())
    op = input("Choose an operation (+, -, /, *): ").strip()
    y = int(input("Type the second number: ").strip())

    if op == "+":
        print(f"The result is {x + y}")
    elif op == "-":
        print(f"The result is {x - y}")
    elif op == "*":
        print(f"The result is {x * y}")
    elif op == "/" and y != 0:
        print(f"The result is {x / y}")
    else:
        print("Error!!!")
    
    print("Wanna calculate again? Press 'R' to restart or 'X' to stop")
    while True:
        ip = input("Input: ").strip().lower()
        if ip == "r":
            main()
            break
        elif ip == "x":
            print("See you later! Basic Calculator made by Curious Dude")
            break
        else:
            print("Error!!!")
            continue


        

print("Welcome to the calculator!")
print("Press 'S' to start calculating")

while True:
    i = input().strip().lower()

    if i == "s":
        main()
        break
    else:
        continue
