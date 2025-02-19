print('menghitung luas dan keliling segitiga silu siku')
print('-----------------------------------------------')

A = int(input('masukan nilai alas'))
T = int(input('masukan nilai tinggi'))
C = int(input('masukan nilai C: '))

def menu():
    print('1. keliling')
    print('2. luas')
    print('3. keluar')

menu()
option = int(input('Masukan menu yang dituju: '))

while option != 3:
    if option == 1:
        keliling = T + A + C
        print('Dengan rumus a+b+c. Keliling segitiga siku-siku ini adalah', keliling)
        menu()
        option = int(input('Masukan menu yang dituju: '))

    elif option == 2:
        luas = 0.5 * A * T
        print('Dengan rumus  Â½ x a x t Luas dari Segitiga siku-siku ini adalah', luas)
        menu()
        option = int(input('Masukan menu yang dituju: '))