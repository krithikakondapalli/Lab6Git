# Krithika Kondapalli: encode function


def main():
    while True:
        print("""
Menu
-------------
1. Encode 
2. Decode 
3. Quit
           """)
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            original_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(original_pass)
            print("Your password has been encoded and stored!")
        elif user_option == 2:
            original_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {original_pass}.")
            print()
        elif user_option == 3:
            break
        else:
            break

def encode(password):
    encoded_pass = ""
    for digit in password:
        if int(digit) >= 7:
            number = str(int(digit) + 3)
            encoded_pass += number[1]
        else:
            encoded_pass += str(int(digit) + 3)

    return encoded_pass



if __name__ == "__main__":
    encoded_pass = ""
    original_pass = ""
    main()