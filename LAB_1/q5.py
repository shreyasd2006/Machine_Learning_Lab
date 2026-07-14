import random
import statistics

numbers = []

for i in range(100):
    numbers.append(random.randint(100, 150))

print("Numbers:")
print(numbers)

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))