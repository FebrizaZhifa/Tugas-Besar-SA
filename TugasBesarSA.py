import random
import time
from itertools import combinations

# Fungsi untuk menghasilkan data penerbangan acak
def generate_random_flights(num_flights):
    flights = []
    for _ in range(num_flights):
        start_time = random.randint(0, 100)  # Waktu mulai acak antara 0 dan 100
        end_time = start_time + random.randint(1, 10)  # Waktu berakhir acak antara 1 dan 10 setelah waktu mulai
        flights.append((start_time, end_time))  # Tambahkan tuple (start_time, end_time) ke daftar
    return flights  # Kembalikan daftar penerbangan

# Algoritma Greedy untuk penjadwalan penerbangan
def greedy_schedule(flights):
    flights.sort(key=lambda x: x[1])  # Urutkan penerbangan berdasarkan waktu berakhir
    last_end_time = -1  # Inisialisasi waktu berakhir terakhir
    selected_flights = []  # Daftar untuk menyimpan penerbangan yang dipilih
    for flight in flights:
        if flight[0] >= last_end_time:  # Jika waktu mulai penerbangan lebih besar atau sama dengan waktu berakhir terakhir
            selected_flights.append(flight)  # Tambahkan penerbangan ke daftar penerbangan yang dipilih
            last_end_time = flight[1]  # Perbarui waktu berakhir terakhir
    return selected_flights  # Kembalikan daftar penerbangan yang dipilih

# Algoritma Brute Force untuk penjadwalan penerbangan
def brute_force_schedule(flights):
    n = len(flights)  # Jumlah penerbangan
    max_flights = []  # Daftar untuk menyimpan penerbangan maksimal yang tidak bertabrakan
    max_count = 0  # Inisialisasi jumlah maksimal penerbangan
    # Evaluasi semua subset penerbangan
    for i in range(1, 2**n):
        subset = [flights[j] for j in range(n) if (i & (1 << j))]  # Buat subset penerbangan
        if is_valid_subset(subset) and len(subset) > max_count:  # Jika subset valid dan lebih besar dari jumlah maksimal saat ini
            max_count = len(subset)  # Perbarui jumlah maksimal
            max_flights = subset  # Perbarui penerbangan maksimal
    return max_flights  # Kembalikan penerbangan maksimal

# Fungsi untuk memeriksa apakah subset penerbangan valid (tidak ada penerbangan yang bertabrakan)
def is_valid_subset(subset):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if subset[i][1] > subset[j][0] and subset[i][0] < subset[j][1]:  # Jika waktu berakhir penerbangan i lebih besar dari waktu mulai penerbangan j dan waktu mulai penerbangan i kurang dari waktu berakhir penerbangan j
                return False  # Subset tidak valid
    return True  # Subset valid

# Fungsi utama untuk membandingkan kedua algoritma
def compare_algorithms(num_flights):
    flights = generate_random_flights(num_flights)  # Hasilkan data penerbangan acak
    print("Random Flights:")
    for i, (start, end) in enumerate(flights, 1):
        print(f"Flight {i}: Start = {start}, End = {end}")  # Cetak data penerbangan acak

    start_time = time.time()  # Catat waktu mulai
    greedy_result = greedy_schedule(flights)  # Jalankan algoritma Greedy
    greedy_time = time.time() - start_time  # Hitung waktu eksekusi Greedy

    start_time = time.time()  # Catat waktu mulai
    brute_force_result = brute_force_schedule(flights)  # Jalankan algoritma Brute Force
    brute_force_time = time.time() - start_time  # Hitung waktu eksekusi Brute Force

    print("\nGreedy Result:")
    for i, (start, end) in enumerate(greedy_result, 1):
        print(f"Flight {i}: Start = {start}, End = {end}")  # Cetak hasil algoritma Greedy
    print(f"Greedy Time: {greedy_time:.6f} seconds")  # Cetak waktu eksekusi Greedy

    print("\nBrute Force Result:")
    for i, (start, end) in enumerate(brute_force_result, 1):
        print(f"Flight {i}: Start = {start}, End = {end}")  # Cetak hasil algoritma Brute Force
    print(f"Brute Force Time: {brute_force_time:.6f} seconds")  # Cetak waktu eksekusi Brute Force

    print(f"\nNumber of flights scheduled by Greedy: {len(greedy_result)}")  # Cetak jumlah penerbangan yang dijadwalkan oleh Greedy
    print(f"Number of flights scheduled by Brute Force: {len(brute_force_result)}")  # Cetak jumlah penerbangan yang dijadwalkan oleh Brute Force

# Jalankan perbandingan dengan 20 penerbangan acak
compare_algorithms(20)