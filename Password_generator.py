import random
import string

"""

PASSWORD GENERATOR made by Otto Heldt

"""

letters = string.ascii_letters

numbers = string.digits

special_char = string.punctuation


def get_length():

    """
    Asks the user to define the length of the password, requires it to be at least 8 characters long.
    """
    length = int(input("How long do you want your password to be? (Minimum 8): "))

    while length < 8:
        print("The minimum length for a password should be 8 characters\n")
        length = int(input("How long do you want your password to be? (Minimum 8): "))

    return length


def get_password_requirements():
    """
    Asks the user about the requirements of the password, like if it needs to have numbers or special characters.
    Stores and returns a boolean variable based on the users input yes = True, no = False

    """
    want_num = input("Do you want the password to have numbers?(yes or no): ")
    while want_num.lower() not in ("yes", "no"):
        want_num = input("Please type yes or no: ")
    if want_num.lower() == "yes":
        num_value = True
    else:
        num_value = False

    want_special = input("Do you want the password to have special characters?(yes or no): ")
    while want_special.lower() not in ("yes", "no"):
        want_special = input("Please type yes or no: ")
    if want_special.lower() == "yes":
        special_value = True
    else:
        special_value = False

    want_letters = input("Do you want the password to have letters?(yes or no): ")
    while want_letters.lower() not in ("yes", "no"):
        want_letters = input("Please type yes or no: ")
    if want_letters.lower() == "yes":
        letters_value = True
    else:
        letters_value = False

    return num_value, special_value, letters_value


def password_info(num_value, special_value, letters_value):

    """
    Stores string data on pass_info variable based on the value of num_value, special_value and letters_value,
    which it gets from the get_passwords_requirements function.

    """
    pass_info = ''
    
    if letters_value:
        pass_info += letters

    if special_value:
        pass_info += special_char

    if num_value:
        pass_info += numbers

    return pass_info


def pass_generator(pass_info,length):
    """
    Generates a random password based on the variable pass_info which it gets from the password_info function
    """
    char_list = pass_info

    char_list = list(char_list)

    random.shuffle(char_list)

    generated_password = random.choices(char_list, k=length)

    generated_password = ''.join(generated_password)

    return generated_password


def start():
    length = get_length()

    num_value, special_value, letters_value = get_password_requirements()

    pass_info = password_info(num_value, special_value, letters_value)

    password = pass_generator(pass_info, length)

    print("Your randomly generated password is:", password)

    question = input("Do you want to create a new password (yes or no)?: ")

    while question.lower() not in ("yes", "no"):
        question = input("Please type yes or no: ")
    if question == "yes":
        start()
    else:
        exit()


if __name__ == '__main__':
    start()







