def find_max_min_median_mean(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # 1. Максимальне число
    maximum = max(numbers)

    # 2. Мінімальне число
    minimum = min(numbers)

    # 3. Медіана
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]

    # 4. Середнє арифметичне
    mean = sum(numbers) / n

    return maximum, minimum, median, mean

def find_longest_increasing_decreasing_sequence(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # 5*. Найбільша зростаюча послідовність
    longest_increasing = []
    current_sequence = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            current_sequence.append(numbers[i])
        else:
            current_sequence.append(numbers[i])
            if len(current_sequence) > len(longest_increasing):
                longest_increasing = current_sequence.copy()
            current_sequence = []

    # 6*. Найбільша спадна послідовність
    longest_decreasing = []
    current_sequence = []
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            current_sequence.append(numbers[i])
        else:
            current_sequence.append(numbers[i])
            if len(current_sequence) > len(longest_decreasing):
                longest_decreasing = current_sequence.copy()
            current_sequence = []

    return longest_increasing, longest_decreasing

filename = '10m.txt'
maximum, minimum, median, mean = find_max_min_median_mean(filename)
longest_increasing, longest_decreasing = find_longest_increasing_decreasing_sequence(filename)

print("1. Максимальне число:", maximum)
print("2. Мінімальне число:", minimum)
print("3. Медіана:", median)
print("4. Середнє арифметичне:", mean)
print("5*. Найбільша зростаюча послідовність:", longest_increasing)
print("6*. Найбільша спадна послідовність:", longest_decreasing)