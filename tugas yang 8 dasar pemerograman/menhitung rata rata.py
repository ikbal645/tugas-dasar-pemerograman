def mean(n):
    sum = 0
    for i in range(n):
        bil = int(input('Masukkan bilangan: '))
        sum = sum + bil
    result = sum / n
    print('Rata-rata:', result)

# Minta pengguna untuk mengetahui jumlah input dan kemudian panggil fungsi mean
print('Masukkan jumlah bilangan:')
mean(int(input()))  # Ini akan memanggil fungsi mean dengan jumlah input yang ditentukan
