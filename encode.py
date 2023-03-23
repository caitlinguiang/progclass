def encoder(password):      # caitlin guiang
    list(password)       # convert string into list
    new_password = ''        # create new string for encoded password
    for element in password:
        element = int(element)
        if element < 7:         # encodes by adding 3 to each element
            element += 3
        elif element >= 7:       # only uses 0-9
            element -= 7
        new_password += str(element)
    return new_password

def decoder(password):      # Joshua Barcenas
    encode_pass = []
    for i in range(len(password)):
        # reverses encode operation
        string = int(password[i]) - 3

        # removes instances where num out of range (0,9)
        if string == -3:
            string = 7
        elif string == -2:
            string = 8
        elif string == -1:
            string = 9
        string = f'{string}'
        encode_pass.append(string)

    # password is a string
    encode_pass = ''.join(encode_pass)
    return encode_pass
def print_menu():        # creates menu prompt
    print("Menu")
    print("-" * 13)
    print("1. Encode\n2. Decode\n3. Quit\n")

if __name__ == "__main__":
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:      # gets user input for password and encodes it
            password = input("Please enter your password to encode: ")
            new_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:        # displays encoded password and original password
            print(f"The encoded password is {new_password}, and the original password is {decoder(new_password)}.\n")
        elif option == 3:        # stops the program
            break
