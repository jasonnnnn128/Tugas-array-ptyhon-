# array('i', [...]) (dari modul array bawaan Python)
# Ini array versi standar library Python (from array import array).
#Sintaks: array(typecode, [data])
#ypecode = huruf yang menunjukkan tipe data.
#'i' → integer
#'f' → float
#'u' → Unicode character
#dll.

#np.array([...]) (dari NumPy)
#Ini array versi NumPy, yang lebih powerful.
#Bisa multidimensi (1D, 2D, 3D, dst).
#Bisa langsung operasi matematika (perkalian, penjumlahan, transpose, dll).
#Tipe data (dtype) akan otomatis ditentukan, tapi bisa juga dipaksa:

#fungsi fungsi array dalam numpy 
# 1. bikin array 
import numpy as np

np.array([1, 2, 3])       # dari list
np.zeros(5)               # array isi 0, panjang 5 → [0. 0. 0. 0. 0.]
np.ones((2, 3))           # matriks 2x3 isi 1
np.full((2, 2), 7)        # matriks 2x2 isi 7
np.arange(0, 10, 2)       # [0 2 4 6 8] (seperti range tapi jadi array)
np.linspace(0, 1, 5)      # 5 angka dari 0 sampai 1 → [0. 0.25 0.5 0.75 1.]
np.eye(3)                 # matriks identitas 3x3

# 2. informasi array
a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape      # ukuran array → (2, 3)
a.ndim       # jumlah dimensi → 2
a.size       # jumlah elemen → 6
a.dtype      # tipe data elemen → int32 / float64

# 3. Operasi MTK
b = np.array([1, 2, 3])
c = np.array([4, 5, 6])

b + c        # [5 7 9]
b - c        # [-3 -3 -3]
b * c        # [4 10 18] (perkalian elemen)
b / c        # [0.25 0.4 0.5]
b ** 2       # [1 4 9] (pangkat)

# 4. fungsi mtk 
np.sqrt(b)           # akar kuadrat
np.exp(b)            # e^x
np.log(b)            # log natural
np.sin(b)            # sinus
np.max(b)            # nilai terbesar
np.min(b)            # nilai terkecil
np.sum(b)            # jumlah semua elemen
np.mean(b)           # rata-rata
np.median(b)         # median
np.std(b)            # standar deviasi

# 5. Manipulasi array 
a = np.array([[1, 2, 3], [4, 5, 6]])

a.reshape(3, 2)   # ubah bentuk array jadi 3 baris 2 kolom
a.flatten()       # ubah jadi 1 dimensi
a.transpose()     # transpose matriks (tukar baris dan kolom)
np.concatenate([b, c])   # gabungkan array
np.vstack([b, c])        # gabungkan secara vertikal
np.hstack([b, c])        # gabungkan secara horizontal

# 6. Indexing dan Slicing 
a = np.array([10, 20, 30, 40, 50])

a[0]         # 10 (elemen pertama)
a[-1]        # 50 (elemen terakhir)
a[1:4]       # [20 30 40] (slice)
a[::2]       # [10 30 50] (loncat 2)

# 7. Random array acak 
np.random.rand(3)        # 3 angka random [0,1)
np.random.randint(0, 10, 5)  # 5 angka random dari 0–9
np.random.randn(2, 3)    # matriks normal distribusi 2x3

# 8. linear algebra 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)          # perkalian matriks
np.linalg.inv(A)      # inverse matriks
np.linalg.det(A)      # determinan matriks
np.linalg.eig(A)      # nilai eigen & vektor eigen
