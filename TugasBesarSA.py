import time
import random
from itertools import combinations

class Flight:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def greedy_schedule(flights):
    flights.sort(key=lambda x: x.end)
    schedule = []
    current_end_time = 0

    for flight in flights:
        if flight.start >= current_end_time:
            schedule.append(flight)
            current_end_time = flight.end

    return schedule

def brute_force_schedule(flights):
    n = len(flights)
    max_schedule = []

    for i in range(1, n + 1):
        for combo in combinations(flights, i):
            if is_valid_schedule(combo):
                if len(combo) > len(max_schedule):
                    max_schedule = combo

    return max_schedule

def is_valid_schedule(flights):
    for i in range(len(flights)):
        for j in range(i + 1, len(flights)):
            if flights[i].end > flights[j].start and flights[i].start < flights[j].end:
                return False
    return True

def generate_flights(n):
    flights = []
    for _ in range(n):
        start = random.randint(0, 100)
        end = start + random.randint(1, 10)
        flights.append(Flight(start, end))
    return flights

def measure_time(algorithm, flights):
    start_time = time.time()
    algorithm(flights)
    end_time = time.time()
    return end_time - start_time

# Mengukur waktu eksekusi
input_sizes = [5, 10, 15, 20]
greedy_times = []
brute_force_times = []

for size in input_sizes:
    flights = generate_flights(size)
    greedy_times.append(measure_time(greedy_schedule, flights))
    if size <= 20:  # Brute force hanya untuk ukuran kecil karena eksponensial
        brute_force_times.append(measure_time(brute_force_schedule, flights))

print("Greedy Times:", greedy_times)
print("Brute Force Times:", brute_force_times)

# Contoh Penggunaan
print("Scheduled flights (Greedy) untuk input size 15:")
flights = generate_flights(15)
scheduled_flights = greedy_schedule(flights)
for flight in scheduled_flights:
    print(f"Flight from {flight.start} to {flight.end}")

print("\nScheduled flights (Brute Force) untuk input size 10:")
scheduled_flights = brute_force_schedule(flights)
for flight in scheduled_flights:
    print(f"Flight from {flight.start} to {flight.end}")
