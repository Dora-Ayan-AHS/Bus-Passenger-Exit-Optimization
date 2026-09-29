import random
import matplotlib.pyplot as plt

ROWS = 10
SEATS_PER_ROW = 4

def front_to_back():
    total_time = 0

    for row in range(ROWS):
        passengers = [random.randint(1, 3)
                      for _ in range(SEATS_PER_ROW)]

        total_time += max(passengers)

    return total_time


def alternating_rows():
    total_time = 0

    order = list(range(0, ROWS, 2)) + \
            list(range(1, ROWS, 2))

    for row in order:
        passengers = [random.randint(1, 3)
                      for _ in range(SEATS_PER_ROW)]

        total_time += max(passengers)

    return total_time * 0.9  # small efficiency gain


def everyone_rushes():
    total_time = 0

    for row in range(ROWS):
        passengers = [random.randint(1, 3)
                      for _ in range(SEATS_PER_ROW)]

        total_time += max(passengers)

    congestion_penalty = 5

    return total_time + congestion_penalty


results = {
    "Front-to-Back": front_to_back(),
    "Alternating Rows": alternating_rows(),
    "Everyone Rushes": everyone_rushes()
}

print("Bus Exit Times")
print("-" * 30)

for method, time in results.items():
    print(f"{method}: {time:.1f} seconds")

plt.bar(results.keys(),
        results.values(),
        color=["steelblue", "green", "red"])

plt.ylabel("Time (seconds)")
plt.title("Bus Exit Optimization")
plt.tight_layout()
plt.savefig("results.png")
plt.show()
