###### G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO

## Soal
1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut:
 (https://github.com/randiijulian/randiijulian/assets/81604461/e32b6d92-7e3a-4323-a0e3-711009112c8e)

2. Buatlah program bebas, dengan menerapkan if else pada:
   a. For Loops
   b. While Loops

3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for

## Pembahasan

### 1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut: (https://github.com/randiijulian/randiijulian/assets/81604461/e32b6d92-7e3a-4323-a0e3-711009112c8e)
#### 1.1 Apa itu Looping?
Perulangan atau disebut Looping adalah bahasa pemrograman dan algoritma yang kegunaannya untuk mengulang sebuah perintah/intruksi yang dibuat dalam script sesuai dengan jumlah yang telah ditentukan. Perulangan bertujuan untuk mempersingkat waktu pernyataan program yang harus ditulis dalam jumlah yang banyak.
#### 1.2 Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/looping1.png?raw=true)

Pada Kode Diatas adalah sebuah program Python yang menggunakan perulangan for untuk mencetak angka dari 1 hingga 20. Jika suatu angka habis dibagi 10, maka program akan mencetak "Faishal" sebanyak tiga kali. Jika tidak, program akan mencetak angka tersebut.
#### 1.3 Penjelasan Setiap Kode
```sh
for i in range(1, 21):
```
Pada Kode Program Diatas berfungsi agar Perulangan ini akan berjalan dari 1 hingga 20
```sh
if i % 10 == 0:
```
Pada Kode Program Diatas berfungsi untuk memeriksa apakah nilai i habis dibagi 10
Jika i habis dibagi 10, masuk ke dalam blok if:
```sh
for _ in range(3):
```
Pada Kode Program Diatas berfungsi agar perulangan berjalan sebanyak 3 kali
```sh
print("Faishal")
```
Dan terakhir pada kode program diatas berfungsi untuk mencetak suatu nama untuk dijadikan sebuah perulangan

#### Contoh Luaran Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/looping1%20Luaran.png?raw=true)
Pada Gambar diatas merupakan sebuah tampilan dari output yang telah dijalankan pada sebuah kode program Perulangan tersebut, Bisa Dilihat bahwa Pada nilai i sama dengan 10 dan 20, "Faishal" dicetak sebanyak tiga kali. 
