import itertools
import string
import random

def generate_word_list(length, characters, include_numbers=False, include_symbols=False, include_spaces=False, include_uppercase=False, filename='wordlist.txt'):
    charset = characters
    if include_numbers:
        charset += string.digits
    if include_symbols:
        charset += string.punctuation
    if include_spaces:
        charset += ' '
    if include_uppercase:
        charset += string.ascii_uppercase
    with open(filename, 'w') as file:
            charset = string.ascii_letters + string.digits
            for password in itertools.product(charset, repeat=length):
                file.write(''.join(password) + '\n')

def generate_router_password(length=8, algorithm='default', filename='wordlist.txt'):
    with open(filename, 'w') as file:
        if algorithm == 'default':
            charset = string.ascii_letters + string.digits
            for password in itertools.product(charset, repeat=length):
                file.write(''.join(password) + '\n')
        elif algorithm == 'random':
            charset = string.ascii_letters + string.digits + string.punctuation
            for password in itertools.product(charset, repeat=length):
                file.write(''.join(password) + '\n')
        elif algorithm == 'common':
            common_passwords = ['admin', '123456', 'password', '123456789', 'qwerty', 'abc123', 'letmein', 'monkey', 'password1', 'dragon']
            for password in common_passwords:
                file.write(password + '\n')
        elif algorithm == 'pattern':
            charset = string.ascii_lowercase + string.digits
            for password in itertools.product(charset, repeat=length):
                file.write(''.join(password) + '\n')
        elif algorithm == 'HEX':
            for i in range(16**length):  # Desde 00 hasta FF (0x00 - 0xFF)
                password = format(i,'0' + str(length)+'X')  # Convierte el número a hexadecimal de 2 dígitos
                file.write(password + '\n')
        elif algorithm == 'OCT':
            for i in range(8 ** length):  # Desde 00 hasta 77 (0-7 en octal)
                password = format(i, '0' + str(length) + 'o')  # Convierte el número a octal de longitud 'length'
                file.write(password + '\n')
        elif algorithm == 'BIN':
            for i in range(2 ** length):  # Desde 00 hasta 11 (0-1 en bin)
                password = format(i, '0' + str(length) + 'b')  # Convierte el número a binario de longitud 'length'
                file.write(password + '\n')
        else:
            raise ValueError("Algoritmo no válido")

    print(f"Word-list guardada en '{filename}'")

def generate_word_list_from_phrase(phrase, length,filename='wordlist.txt'):
    with open(filename, 'w') as file:
        words = phrase.split()
        for password in itertools.product(words, repeat=length):
                file.write(''.join(password) + '\n')

def generate_word_list_from_dictionary(dictionary_file,filename='wordlist.txt'):
    with open(dictionary_file, 'r') as input_file:
        with open(filename, 'w') as output_file:
            for line in input_file:
                output_file.write(line.strip() + '\n')


def save_word_list(wordlist, filename):
    with open(filename, 'w') as file:
        file.writelines(word + '\n' for word in wordlist)
    print(f"Word-list guardada en '{filename}'")

def main():
    print("Bienvenido al generador de Word-list")
    print("====================================")

    print("Seleccione el propósito de la word-list:")
    print("1. Contraseñas de routers")
    print("2. Basada en una frase o conjunto de palabras")
    print("3. Personalizada")
    print("4. Desde un archivo de diccionario")
    choice = input("Ingrese el número correspondiente a su elección: ")

    if choice == '1':
        length = int(input("Longitud de las contraseñas: "))
        algorithm = input("Seleccione el algoritmo para generar las contraseñas (default/random/common/pattern/HEX/OCT/BIN): ")
        filename = input("Ingrese el nombre del archivo para guardar la Word-list: ")
        generate_router_password(length, algorithm, filename)
    elif choice == '2':
        phrase = input("Ingrese la frase o conjunto de palabras: ")
        length = int(input("Longitud de las palabras: "))
        filename = input("Ingrese el nombre del archivo para guardar la Word-list: ")

        generate_word_list_from_phrase(phrase, length,filename)
    

    elif choice == '3':
        characters = input("Ingrese los caracteres a incluir (sin espacios): ")
        length = int(input("Longitud de las palabras: "))
        filename = input("Ingrese el nombre del archivo para guardar la Word-list: ")

        include_numbers = input("¿Incluir números? (s/n): ").lower() == 's'
        include_symbols = input("¿Incluir símbolos? (s/n): ").lower() == 's'
        include_spaces = input("¿Incluir espacios? (s/n): ").lower() == 's'
        include_uppercase = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'

        wordlist = generate_word_list(length, characters, include_numbers, include_symbols, include_spaces, include_uppercase,filename)

    elif choice == '4':
        dictionary_file = input("Ingrese el nombre del archivo de diccionario: ")
        filename = input("Ingrese el nombre del archivo para guardar la Word-list: ")

        generate_word_list_from_dictionary(dictionary_file,filename)


    else:
        print("Selección no válida. Por favor, ingrese 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
