# a. For Loop
for char in "Halo,Faishal!":
    if char.isalpha():
        print(f"{char} adalah huruf.")
    elif char.isdigit():
        print(f"{char} adalah angka.")
    else:
        print(f"{char} adalah karakter spesial.")

        
# b. While Loop
input_str = input("Masukkan string (ketik 'selesai' untuk Stop Running): ")
while input_str.lower() != 'selesai':
    if input_str.isalpha():
        print(f"{input_str} adalah sebuah kata.")
    elif input_str.isdigit():
        print(f"{input_str} adalah sebuah angka.")
    else:
        print(f"{input_str} adalah kombinasi karakter.")
    input_str = input("Masukkan string (ketik 'selesai' untuk Stop Running): ")
