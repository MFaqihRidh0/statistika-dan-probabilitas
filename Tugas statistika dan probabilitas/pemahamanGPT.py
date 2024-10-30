# Mengonversi kolom menjadi tipe numerik
penjualan_A = pd.to_numeric(dataset['Penjualan A (pcs)'], errors='coerce')  # Mengubah data kolom 'Penjualan A (pcs)' menjadi numerik, jika ada nilai non-numerik, akan diubah menjadi NaN
penjualan_B = pd.to_numeric(dataset['Penjualan B (pcs)'], errors='coerce')  # Mengubah data kolom 'Penjualan B (pcs)' menjadi numerik, jika ada nilai non-numerik, akan diubah menjadi NaN

# Menghitung jangkauan interkuartil (IQR) untuk setiap kolom
def hitung_iqr(data):
    Q1 = data.quantile(0.25)  # Menghitung kuartil pertama (25% data berada di bawah nilai ini)
    Q3 = data.quantile(0.75)  # Menghitung kuartil ketiga (75% data berada di bawah nilai ini)
    IQR = Q3 - Q1  # Menghitung jangkauan interkuartil dengan mengurangi Q1 dari Q3
    return IQR  # Mengembalikan nilai IQR yang sudah dihitung

# Menghitung IQR untuk masing-masing kolom penjualan
iqr_A = hitung_iqr(penjualan_A)  # Memanggil fungsi hitung_iqr untuk data penjualan_A dan menyimpan hasilnya pada variabel iqr_A
iqr_B = hitung_iqr(penjualan_B)  # Memanggil fungsi hitung_iqr untuk data penjualan_B dan menyimpan hasilnya pada variabel iqr_B

# Menampilkan hasil IQR untuk Penjualan A dan Penjualan B
print(f'Jangkauan Interkuartil (IQR) untuk Penjualan A: {iqr_A}')  # Menampilkan nilai IQR untuk data Penjualan A
print(f'Jangkauan Interkuartil (IQR) untuk Penjualan B: {iqr_B}')  # Menampilkan nilai IQR untuk data Penjualan B

#Visualisasi IQR

import matplotlib.pyplot as plt  # Mengimpor pustaka matplotlib untuk membuat visualisasi grafik
import numpy as np  # Mengimpor pustaka numpy untuk operasi numerik

# Membuat Tabel Distribusi Frekuensi
def buat_tabel_frekuensi(data, bins):
    # Menghitung frekuensi untuk setiap interval (bin)
    frekuensi, batas = np.histogram(data, bins=bins)  # Menggunakan fungsi histogram dari numpy untuk menghitung frekuensi dan batas interval
    tabel = pd.DataFrame({
        'Interval': [f'{batas[i]:.2f} - {batas[i+1]:.2f}' for i in range(len(batas)-1)],  # Membuat kolom 'Interval' dengan rentang tiap bin
        'Frekuensi': frekuensi  # Menyimpan frekuensi pada kolom 'Frekuensi'
    })
    return tabel, batas  # Mengembalikan tabel distribusi frekuensi dan batas interval

# Menentukan jumlah kelas (bins) untuk histogram
bins = 10  # Mengatur jumlah interval menjadi 10 untuk visualisasi histogram

# Membuat tabel distribusi frekuensi untuk Penjualan A dan B
tabel_frekuensi_A, batas_A = buat_tabel_frekuensi(penjualan_A, bins)  # Menghitung distribusi frekuensi untuk Penjualan A
tabel_frekuensi_B, batas_B = buat_tabel_frekuensi(penjualan_B, bins)  # Menghitung distribusi frekuensi untuk Penjualan B

# Menampilkan tabel distribusi frekuensi
print("Tabel Distribusi Frekuensi Penjualan A:")
print(tabel_frekuensi_A)  # Menampilkan tabel distribusi frekuensi untuk Penjualan A
print("\nTabel Distribusi Frekuensi Penjualan B:")
print(tabel_frekuensi_B)  # Menampilkan tabel distribusi frekuensi untuk Penjualan B

# Visualisasi Histogram dan Poligon Frekuensi
plt.figure(figsize=(14, 7))  # Membuat figure untuk visualisasi dengan ukuran 14x7 inci

# Histogram untuk Penjualan A
plt.subplot(1, 2, 1)  # Menentukan subplot pertama (1 baris, 2 kolom, posisi 1)
plt.hist(penjualan_A, bins=bins, alpha=0.7, color='blue', edgecolor='black')  # Membuat histogram untuk Penjualan A
plt.title('Histogram Penjualan A')  # Memberikan judul pada histogram
plt.xlabel('Jumlah Penjualan (pcs)')  # Menambahkan label sumbu-x
plt.ylabel('Frekuensi')  # Menambahkan label sumbu-y

# Poligon Frekuensi untuk Penjualan A
titik_tengah_A = [(batas_A[i] + batas_A[i+1]) / 2 for i in range(len(batas_A)-1)]  # Menghitung titik tengah untuk setiap interval
plt.plot(titik_tengah_A, tabel_frekuensi_A['Frekuensi'], marker='o', color='blue', label='Poligon Frekuensi A')  # Membuat grafik poligon frekuensi untuk Penjualan A
plt.legend()  # Menambahkan legenda untuk grafik

# Histogram untuk Penjualan B
plt.subplot(1, 2, 2)  # Menentukan subplot kedua (1 baris, 2 kolom, posisi 2)
plt.hist(penjualan_B, bins=bins, alpha=0.7, color='green', edgecolor='black')  # Membuat histogram untuk Penjualan B
plt.title('Histogram Penjualan B')  # Memberikan judul pada histogram
plt.xlabel('Jumlah Penjualan (pcs)')  # Menambahkan label sumbu-x
plt.ylabel('Frekuensi')  # Menambahkan label sumbu-y

# Poligon Frekuensi untuk Penjualan B
titik_tengah_B = [(batas_B[i] + batas_B[i+1]) / 2 for i in range(len(batas_B)-1)]  # Menghitung titik tengah untuk setiap interval
plt.plot(titik_tengah_B, tabel_frekuensi_B['Frekuensi'], marker='o', color='green', label='Poligon Frekuensi B')  # Membuat grafik poligon frekuensi untuk Penjualan B
plt.legend()  # Menambahkan legenda untuk grafik

plt.tight_layout()  # Menyesuaikan tata letak subplot agar tidak saling tumpang tindih
plt.show()  # Menampilkan visualisasi

#perhitungan skewness

import pandas as pd  # Mengimpor pustaka pandas untuk manipulasi data
from scipy.stats import skew, mode  # Mengimpor fungsi skew untuk menghitung skewness dan mode untuk menghitung modus
import numpy as np  # Mengimpor pustaka numpy untuk operasi numerik

# Contoh data (gunakan dataset yang sesuai)
penjualan_A = pd.to_numeric(dataset['Penjualan A (pcs)'], errors='coerce')  # Mengonversi kolom 'Penjualan A (pcs)' menjadi numerik, mengubah nilai yang tidak valid menjadi NaN
penjualan_B = pd.to_numeric(dataset['Penjualan B (pcs)'], errors='coerce')  # Mengonversi kolom 'Penjualan B (pcs)' menjadi numerik, mengubah nilai yang tidak valid menjadi NaN

# Menghitung mean, median, dan modus untuk Penjualan A
mean_A = penjualan_A.mean()  # Menghitung nilai rata-rata (mean) dari data Penjualan A
median_A = penjualan_A.median()  # Menghitung nilai tengah (median) dari data Penjualan A
# Memastikan hasil mode diakses dengan benar
modus_A_result = mode(penjualan_A.dropna(), nan_policy='omit')  # Menghitung nilai yang paling sering muncul (modus), mengabaikan nilai NaN
modus_A = modus_A_result.mode[0] if isinstance(modus_A_result.mode, np.ndarray) and len(modus_A_result.mode) > 0 else modus_A_result.mode  # Mengambil nilai modus jika hasilnya adalah array, jika tidak, menggunakan nilai asli

# Menghitung mean, median, dan modus untuk Penjualan B
mean_B = penjualan_B.mean()  # Menghitung nilai rata-rata (mean) dari data Penjualan B
median_B = penjualan_B.median()  # Menghitung nilai tengah (median) dari data Penjualan B
modus_B_result = mode(penjualan_B.dropna(), nan_policy='omit')  # Menghitung nilai yang paling sering muncul (modus), mengabaikan nilai NaN
modus_B = modus_B_result.mode[0] if isinstance(modus_B_result.mode, np.ndarray) and len(modus_B_result.mode) > 0 else modus_B_result.mode  # Mengambil nilai modus jika hasilnya adalah array, jika tidak, menggunakan nilai asli

# Menghitung skewness untuk Penjualan A dan B
skewness_A = skew(penjualan_A.dropna())  # Menghitung nilai skewness (kemencengan) dari data Penjualan A, mengabaikan nilai NaN
skewness_B = skew(penjualan_B.dropna())  # Menghitung nilai skewness (kemencengan) dari data Penjualan B, mengabaikan nilai NaN

# Menampilkan hasil
print(f"Penjualan A - Mean: {mean_A:.2f}, Median: {median_A:.2f}, Modus: {modus_A}")  # Menampilkan mean, median, dan modus dari Penjualan A
print(f"Penjualan A - Skewness: {skewness_A:.2f}")  # Menampilkan nilai skewness dari Penjualan A
print(f"Penjualan B - Mean: {mean_B:.2f}, Median: {median_B:.2f}, Modus: {modus_B}")  # Menampilkan mean, median, dan modus dari Penjualan B
print(f"Penjualan B - Skewness: {skewness_B:.2f}")  # Menampilkan nilai skewness dari Penjualan B

#visualisasi skewness

import matplotlib.pyplot as plt  # Mengimpor pustaka matplotlib untuk visualisasi grafik
import seaborn as sns  # Mengimpor pustaka seaborn untuk visualisasi data yang lebih estetik

# Visualisasi histogram dengan informasi skewness, mean, median, dan modus untuk Penjualan A dan B
plt.figure(figsize=(12, 6))  # Membuat figure baru untuk visualisasi dengan ukuran 12x6 inci

# Histogram untuk Penjualan A
plt.subplot(1, 2, 1)  # Membuat subplot pertama (1 baris, 2 kolom, posisi 1)
sns.histplot(penjualan_A.dropna(), bins=30, kde=True, color='blue')  # Membuat histogram dengan 30 bins dan menampilkan garis kepadatan kernel (KDE) untuk Penjualan A, mengabaikan nilai NaN
plt.axvline(mean_A, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_A:.2f}')  # Menambahkan garis vertikal untuk mean, berwarna merah dan putus-putus
plt.axvline(median_A, color='green', linestyle='dotted', linewidth=2, label=f'Median: {median_A:.2f}')  # Menambahkan garis vertikal untuk median, berwarna hijau dan berbentuk titik-titik
if modus_A is not None:  # Memeriksa apakah modus_A memiliki nilai yang valid
    plt.axvline(modus_A, color='purple', linestyle='dashdot', linewidth=2, label=f'Modus: {modus_A}')  # Menambahkan garis vertikal untuk modus, berwarna ungu dan berbentuk garis-dan-titik
plt.title(f'Skewness Penjualan A: {skewness_A:.2f}')  # Menambahkan judul pada histogram yang menunjukkan nilai skewness untuk Penjualan A
plt.xlabel('Penjualan A (pcs)')  # Menambahkan label pada sumbu-x
plt.ylabel('Frekuensi')  # Menambahkan label pada sumbu-y
plt.legend()  # Menampilkan legenda untuk garis mean, median, dan modus

# Histogram untuk Penjualan B
plt.subplot(1, 2, 2)  # Membuat subplot kedua (1 baris, 2 kolom, posisi 2)
sns.histplot(penjualan_B.dropna(), bins=30, kde=True, color='green')  # Membuat histogram dengan 30 bins dan menampilkan garis kepadatan kernel (KDE) untuk Penjualan B, mengabaikan nilai NaN
plt.axvline(mean_B, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_B:.2f}')  # Menambahkan garis vertikal untuk mean, berwarna merah dan putus-putus
plt.axvline(median_B, color='green', linestyle='dotted', linewidth=2, label=f'Median: {median_B:.2f}')  # Menambahkan garis vertikal untuk median, berwarna hijau dan berbentuk titik-titik
if modus_B is not None:  # Memeriksa apakah modus_B memiliki nilai yang valid
    plt.axvline(modus_B, color='purple', linestyle='dashdot', linewidth=2, label=f'Modus: {modus_B}')  # Menambahkan garis vertikal untuk modus, berwarna ungu dan berbentuk garis-dan-titik
plt.title(f'Skewness Penjualan B: {skewness_B:.2f}')  # Menambahkan judul pada histogram yang menunjukkan nilai skewness untuk Penjualan B
plt.xlabel('Penjualan B (pcs)')  # Menambahkan label pada sumbu-x
plt.ylabel('Frekuensi')  # Menambahkan label pada sumbu-y
plt.legend()  # Menampilkan legenda untuk garis mean, median, dan modus

plt.tight_layout()  # Menyesuaikan tata letak subplot agar tidak saling tumpang tindih
plt.show()  # Menampilkan visualisasi


#perhitungan kurtosis

import pandas as pd  # Mengimpor pustaka pandas untuk manipulasi data
from scipy.stats import kurtosis  # Mengimpor fungsi kurtosis dari pustaka scipy untuk menghitung kurtosis

# Membaca file Excel
dataset = pd.read_excel("Dataset.xlsx")  # Membaca data dari file Excel bernama "Dataset.xlsx" dan menyimpannya dalam variabel dataset

# Mengonversi kolom Penjualan A dan Penjualan B menjadi numerik
penjualan_A = pd.to_numeric(dataset['Penjualan A (pcs)'], errors='coerce')  # Mengonversi data pada kolom "Penjualan A (pcs)" menjadi tipe numerik, mengubah nilai yang tidak bisa dikonversi menjadi NaN
penjualan_B = pd.to_numeric(dataset['Penjualan B (pcs)'], errors='coerce')  # Mengonversi data pada kolom "Penjualan B (pcs)" menjadi tipe numerik, mengubah nilai yang tidak bisa dikonversi menjadi NaN

# Menghitung kurtosis untuk Penjualan A dan Penjualan B
kurtosis_A = kurtosis(penjualan_A, nan_policy='omit')  # Menghitung kurtosis untuk Penjualan A, dengan mengabaikan nilai NaN
kurtosis_B = kurtosis(penjualan_B, nan_policy='omit')  # Menghitung kurtosis untuk Penjualan B, dengan mengabaikan nilai NaN

# Menampilkan hasil
print(f'Kurtosis Penjualan A: {kurtosis_A}')  # Menampilkan hasil perhitungan kurtosis untuk Penjualan A
print(f'Kurtosis Penjualan B: {kurtosis_B}')  # Menampilkan hasil perhitungan kurtosis untuk Penjualan B

#visualisasi kirtosis

import pandas as pd  # Mengimpor pustaka pandas untuk manipulasi data
import numpy as np  # Mengimpor pustaka numpy untuk komputasi numerik
import matplotlib.pyplot as plt  # Mengimpor pustaka matplotlib untuk visualisasi data
import seaborn as sns  # Mengimpor pustaka seaborn untuk membuat grafik yang lebih menarik
from scipy.stats import norm, kurtosis  # Mengimpor fungsi norm dan kurtosis dari pustaka scipy untuk perhitungan statistik

# Membaca file Excel
dataset = pd.read_excel("Dataset.xlsx")  # Membaca data dari file Excel bernama "Dataset.xlsx" dan menyimpannya dalam variabel dataset

# Mengonversi kolom Penjualan A dan Penjualan B menjadi numerik
penjualan_A = pd.to_numeric(dataset['Penjualan A (pcs)'], errors='coerce')  # Mengonversi data pada kolom "Penjualan A (pcs)" menjadi tipe numerik, mengubah nilai yang tidak bisa dikonversi menjadi NaN
penjualan_B = pd.to_numeric(dataset['Penjualan B (pcs)'], errors='coerce')  # Mengonversi data pada kolom "Penjualan B (pcs)" menjadi tipe numerik, mengubah nilai yang tidak bisa dikonversi menjadi NaN

# Menghitung kurtosis untuk Penjualan A dan Penjualan B
kurtosis_A = kurtosis(penjualan_A, nan_policy='omit')  # Menghitung kurtosis untuk Penjualan A, dengan mengabaikan nilai NaN
kurtosis_B = kurtosis(penjualan_B, nan_policy='omit')  # Menghitung kurtosis untuk Penjualan B, dengan mengabaikan nilai NaN

# Visualisasi Penjualan A
plt.figure(figsize=(12, 6))  # Mengatur ukuran figure untuk visualisasi

# Plot histogram dan fit kurva normal untuk Penjualan A
plt.subplot(1, 2, 1)  # Membuat subplot pertama dari dua subplot (1 baris, 2 kolom, subplot ke-1)
sns.histplot(penjualan_A, kde=False, color='blue', stat='density')  # Membuat histogram untuk data Penjualan A, dengan warna biru dan plot densitas
mu_A, std_A = penjualan_A.mean(), penjualan_A.std()  # Menghitung rata-rata dan standar deviasi untuk Penjualan A
xmin, xmax = plt.xlim()  # Mendapatkan batas minimum dan maksimum dari sumbu x
x = np.linspace(xmin, xmax, 100)  # Membuat array nilai x yang berjarak sama antara xmin dan xmax
p = norm.pdf(x, mu_A, std_A)  # Menghitung nilai fungsi distribusi probabilitas normal (kurva normal) berdasarkan mean dan standar deviasi
plt.plot(x, p, 'k', linewidth=2)  # Memplot kurva normal di atas histogram
title_A = f'Penjualan A\nKurtosis: {kurtosis_A:.2f}'  # Menyusun judul plot yang mencakup nilai kurtosis
plt.title(title_A)  # Menampilkan judul untuk plot Penjualan A
plt.xlabel('Penjualan A (pcs)')  # Memberi label sumbu x
plt.ylabel('Density')  # Memberi label sumbu y

# Visualisasi Penjualan B
# Plot histogram dan fit kurva normal untuk Penjualan B
plt.subplot(1, 2, 2)  # Membuat subplot kedua (1 baris, 2 kolom, subplot ke-2)
sns.histplot(penjualan_B, kde=False, color='green', stat='density')  # Membuat histogram untuk data Penjualan B, dengan warna hijau dan plot densitas
mu_B, std_B = penjualan_B.mean(), penjualan_B.std()  # Menghitung rata-rata dan standar deviasi untuk Penjualan B
xmin, xmax = plt.xlim()  # Mendapatkan batas minimum dan maksimum dari sumbu x
x = np.linspace(xmin, xmax, 100)  # Membuat array nilai x yang berjarak sama antara xmin dan xmax
p = norm.pdf(x, mu_B, std_B)  # Menghitung nilai fungsi distribusi probabilitas normal (kurva normal) berdasarkan mean dan standar deviasi
plt.plot(x, p, 'k', linewidth=2)  # Memplot kurva normal di atas histogram
title_B = f'Penjualan B\nKurtosis: {kurtosis_B:.2f}'  # Menyusun judul plot yang mencakup nilai kurtosis
plt.title(title_B)  # Menampilkan judul untuk plot Penjualan B
plt.xlabel('Penjualan B (pcs)')  # Memberi label sumbu x
plt.ylabel('Density')  # Memberi label sumbu y

# Menampilkan plot
plt.tight_layout()  # Mengatur layout agar tidak tumpang tindih
plt.show()  # Menampilkan plot

