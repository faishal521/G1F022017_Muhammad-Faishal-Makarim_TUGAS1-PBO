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
#### 1.1. Apa itu Looping?
Perulangan atau disebut Looping adalah bahasa pemrograman dan algoritma yang kegunaannya untuk mengulang sebuah perintah/intruksi yang dibuat dalam script sesuai dengan jumlah yang telah ditentukan. Perulangan bertujuan untuk mempersingkat waktu pernyataan program yang harus ditulis dalam jumlah yang banyak.
#### 1.2. Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/looping1.png?raw=true)

Pada Kode Diatas adalah sebuah program Python yang menggunakan perulangan for untuk mencetak angka dari 1 hingga 20. Jika suatu angka habis dibagi 10, maka program akan mencetak "Faishal" sebanyak tiga kali. Jika tidak, program akan mencetak angka tersebut.
#### 1.3. Penjelasan Setiap Kode
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

#### 1.4. Contoh Luaran Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/looping1%20Luaran.png?raw=true)
Pada Gambar diatas merupakan sebuah tampilan dari output yang telah dijalankan pada sebuah kode program Perulangan tersebut, Bisa Dilihat bahwa Pada nilai i sama dengan 10 dan 20, "Faishal" dicetak sebanyak tiga kali. 

### 2. Buatlah program bebas, dengan menerapkan if else pada:
   a. For Loops
   
   b. While Loops
# Contoh Penggunaan For Loops
#### 2.1. Apa Itu if Else?
else if adalah pilihan alternative dari penyeleksian untuk mencari kondisi yang diinginkan, else if memiliki fungsi yang sama seperti pernyataan if dan diletakan setelah pernyataan if. else adalah pilihan terakhir yang akan dijalankan jika semua pilihan tidak memiliki nilai benar (true) pada kondisi yang ada. else merupakan pernyataan opsional untuk digunakan berdasarkan kebutuhan, jika tidak menggunakan pernyataan else maka keseluruhan dari pernyataan if akan diabaikan. Statement if-else digunakan untuk menentukan pilihan dari suatu kondisi yang diberikan, cara kerjanya adalah melakukan perbandingan menggunakan Relational operator dan atau Logical operator. Ada juga Statement if-else bersarang merupakan kombinasi dari beberapa If-else dimana ada beberapa kondisi yang diuji kebenarannya ( if didalam if). Statement else-if untuk menentukan satu kondisi benar dari beberapa kondisi yang tersedia, dan untuk switch-case adalah bentuk lain dari else-if dengan mendaftar kondisi secara vertikal dalam satu kolom sehingga memudahkan dalam hal evaluasi program.

#### 2.2. Definisi For Loops
For Loops membaca data dari suatu array atau himpunan data. Proses perulangan pada for loops, dilakukan berdasarkan array/himpunan data yang telah didefinisikan pada suatu variabel.

#### 2.3. Kode Program (Penggunaan For Loops)
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/ifels1.png?raw=true)

Pada Kode Program Diatas merupakan sebuah program Python yang menggunakan perulangan for untuk mengiterasi setiap karakter dalam string "Halo,Faishal!". Selanjutnya, program memeriksa apakah setiap karakter adalah huruf, angka, atau karakter spesial, dan mencetak hasilnya. 
#### 2.4. Penjelasan Setiap Kode
```sh
for char in "Halo,Faishal!"
```
Pada kode program diatas merupakan Perulangan, Perulangan ini akan mengiterasi melalui setiap karakter dalam string "Halo,Faishal!"
##### 2.4.1. Mencetak Karakter Berupa Huruf
```sh
if char.isalpha():
```
Pada kode program diatas berfungsi untuk memeriksa apakah karakter tersebut adalah huruf.
##### _Jika Iya Maka :_
```sh
print(f"{char} adalah huruf.")
```
Mencetak bahwa karakter tersebut adalah huruf.
##### 2.4.2. Mencetak Karakter Berupa Angka
```sh
elif char.isdigit():
```
Pada kode program diatas berfungsi memeriksa apakah karakter tersebut adalah angka.
##### _Jika Iya Maka :_
```sh
print(f"{char} adalah angka.")
```
Mencetak bahwa karakter tersebut adalah angka.
##### 2.4.3. Mencetak Karakter Kondisi yang tidak memenuhi
```sh
print(f"{char} adalah karakter spesial.")
```
Pada Kode Program Diatas berfungsi untuk Mencetak bahwa karakter tersebut adalah karakter spesial.

#### 2.5. Contoh Luaran Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/ifels1%20Luaran.png?raw=true)

Pada Kode tersebut memberikan output yang menjelaskan setiap karakter dalam string apakah huruf, angka, atau karakter spesial. 

# Contoh Penggunaan While Loops
#### 2.6. Apa Itu While Loops
While Loop adalah metode perulangan dimana ada kondisi yang harus dipenuhi supaya looping bisa berjalan terus. While Loop mengulangi eksekusi sub diagram didalamnya sampai terminal kondisi menerima nilai Boolean tertentu. Nilai Boolean tergantung dari sifat dari While Loop. While loops akan mengeksekusi if condition secara terus menerus asalkan condition statement itu menghasilkan pernyataan “True” dan while loops statement dilakukan secara uncountable (secara terus menerus, jika jumlah perulangan tidak ditemukan atau ditentukan).

#### 2.7. Kode Program (Penggunaan While Loops
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/ifels2%20.png?raw=true)


Kode di atas adalah program Python yang meminta pengguna untuk memasukkan sebuah string. Program akan terus meminta input string sampai pengguna memasukkan string "selesai". Setiap kali pengguna memasukkan string, program akan memeriksa apakah string tersebut terdiri dari huruf, angka, atau kombinasi karakter, dan mencetak hasilnya. 
#### 2.8. Penjelasan Setiap Kode
```sh
input_str = input("Masukkan string (ketik 'selesai' untuk Stop Running): ")
```
Pada Kode Program Diatas berfungsi untuk Mengambil input string dari pengguna.
```sh
while input_str.lower() != 'selesai':
```
Pada Kode Program Diatas berfungsi untuk Memulai sebuah loop while yang akan terus berjalan selama input string bukan "selesai" (tanpa memperhatikan huruf besar atau kecil).
### Didalam Perkondisian While Loops
```sh
if input_str.isalpha():
```
Pada Kode Program Diatas berfungsi untuk memeriksa apakah string tersebut hanya terdiri dari huruf.
```sh
print(f"{input_str} adalah sebuah kata.")
```
Pada Kode Program Diatas berfungsi untuk Mencetak bahwa string tersebut adalah sebuah kata.
```sh
elif input_str.isdigit():
```
Pada Kode Program Diatas berfungsi untuk memeriksa apakah string tersebut hanya terdiri dari angka.
```sh
print(f"{input_str} adalah sebuah angka.")
```
Mencetak bahwa string tersebut adalah sebuah angka.
```sh
print(f"{input_str} adalah kombinasi karakter.")
```
Kondisi terakhir adalah untuk Mencetak bahwa string tersebut adalah kombinasi karakter.
```sh
input_str = input("Masukkan string (ketik 'selesai' untuk Stop Running): ")
```
Dan terakhir merupakan Sebuah kode program untuk Mengambil input string lagi untuk iterasi selanjutnya.

#### 2.9. Contoh Luaran Kode Program
![alt text](https://github.com/faishal521/G1F022017_Muhammad-Faishal-Makarim_TUGAS1-PBO/blob/main/public/ifels2%20Luaran.png?raw=true)

Setiap kali pengguna memasukkan string, program akan memberikan respons sesuai dengan jenis string yang dimasukkan. Ketika pengguna memasukkan "selesai", program akan berhenti. 

