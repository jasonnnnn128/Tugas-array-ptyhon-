# array dalam python 

# array adalah Dalam Python, array adalah struktur data yang berfungsi menyimpan koleksi data dengan tipe yang sama dalam satu variabel, 
# disusun secara terstruktur dan terindeks. Array lebih efisien dalam hal penggunaan memori dan kecepatan operasi dibandingkan struktur seperti list, 
# terutama untuk koleksi data yang berskala besar

#codingan umum array 

from array import array #sebelum bikin array kiatr harus import arraynya dulu baru bisa, soalnya array bukan awaan (built-in) Python

from array import array

angka = array('i', [1, 2, 3, 4, 5, 6, 7, 8]) # angka = array('i', [...]) Baris ini membuat array asli Python, bukan list biasa.
print(angka) #Kenapa setelah 'i' harus ada koma? sintaks fungsi array() memerlukan dua argumen: Argumen pertama → 'i' → tipe data Argumen kedua → [1,2,3,...] → data yang disimpan
# Kenapa pakai kurung tutup ) setelah koma? Karena kamu sedang memanggil fungsi / constructor array().Semua fungsi di Python wajib pakai tanda kurung buka dan kurung tutup.
# ini kalau di print emang printoutnya array('i', [1, 2, 3, 4, 5, 6, 7, 8]) juga 
# kalau mau isinya ada pake .tolist 

# kalau mau print salah satu angkanya aja pake 
print (angka[0]) # ini outputnya 1 karena semua data itu mulainya dari angka 0 

angka[1] = 12 #angka[1] itu kita akses data angka di array yang kedua trus kita ubah jadi 12, nanti dia printoutnya 12 1,12 dst 
print(angka) 

number = array('i', [2, 3, 5, 7, 9])
print(number.tolist()) #kalau mau isinya aja tanpa i nya pake fungsi tolist 

# contoh penggunaan array 
# 1. extend 
#extend dipake kalau lu misalnya punya array lebih dari 1 dan mau digabungin bisa pake fungsi extend contoh 
angka.extend(number)
print(angka) #ini dia printoutnya array('i', [1, 12, 3, 4, 5, 6, 7, 8, 2, 3, 5, 7, 9]) karena dari 2 variabel itu kita gabungin pake extend

# 2. slice 
# slice itu dia ngambil beberapa datanya aja dalam array contoh 
print(angka[0:3]) # ini dai ambil data dari pertama yaitu 0 sampe 2 yaitu 1,12,3 karena angka data ke duanya udah diubah ke 12 

# 3. looping array itu dia buat ambil semua datanya tapi dia listnya ke bawah 
for x in angka: #for ... in ... adalah cara standar di Python untuk mengambil setiap item dari sebuah koleksi (list, array, string, tuple, dll.).
    print(x)   #Jadi maksudnya: buat setiap elemen (x) yang ada di dalam array angka, lakukan sesuatu.

# materi inti 
# 1. Dalam konteks Python, "key" itu kek kunci dalam struktur data dictionary (kamus), 
# fungsinya buat penanda unik untuk mengakses sebuah nilai (value) yang terkait dengannya, 
# mirip seperti indeks pada array yang berbasis angka. 

profil = {
    "nama" : "jason",
    "umur" :  18,       # ini kumpulan data yang kita bikin 
    "pekerjaan" : "mahasiswa",
}

print(profil["nama"]) #nama umur dan pekerjaan itu kunci buat akses nilai yang ada 

# 2. values 
#values itu dia elemen elemen data yang ada kek angka teks atau jenis data lainnya contoh 
binatang = ["kucing", "anjing", "ikan", "burung","naga"]
print(binatang[0]) # dia ambil data pertama dengan [0] itu dia data pertamanya dari value binatang itu yaitu kucing jadi printoutnya kucing 

# 3. Update array" dalam Python berarti memodifikasi elemen yang sudah ada atau menambahkan elemen baru ke dalam struktur data
#  seperti list atau array (menggunakan modul array). Ini bisa dilakukan dengan cara mengakses elemen berdasarkan indeksnya dan memberikan nilai baru untuk mengubah nilai yang ada, 
# atau menggunakan metode seperti .append() dan .insert() untuk menambahkan elemen baru. 

angka_ganjil = [1,5,7,9,11,13,14]
angka_ganjil[6] = 15 #dia ambil elemen ke 6 yaitu 14 buat diganti jadi 15
angka_ganjil.append(17) #ini dia nambahin angka lagi di angka_ganjil di paling akhirnya 
angka_ganjil.insert(1,3) # cara bacanya tambahin/insert urutan kedua dengan angka 3 
print(angka_ganjil)

# 4. del ya gampang buat delete sesuatu 
# A. ini delete sesuai index
buah = ["apel", "pisang", "mangga"]
del buah[1] # Menghapus elemen di indeks 1 (yaitu "pisang")
print(buah) # Output: ['apel', 'mangga']

# B. ini delete rentang elemen
bilangan= [0, 1, 2, 3, 4, 5]
del bilangan[1:3] # Menghapus elemen dari indeks 1 sampai sebelum indeks 3
print(bilangan) # Output: [0, 3, 4, 5]

# C. ini delete semua objeknya 
data = [10, 20, 30]
del data # Menghapus seluruh variabel 'data' dari memori
# Akan muncul error jika mencoba mencetak 'data' setelah ini
print(data) #gabisa ke print karena sebelumnya udah dihapus 




















