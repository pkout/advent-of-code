def read_frequencies():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return [int(freq) for freq in lines]

def sum_frequencies(frequencies):
    return sum(f for f in frequencies)

def find_repeating_frequency(frequencies):
    found_frequencies = {0}
    total_frequency = 0

    while True:
        for freq in frequencies:
            total_frequency += freq
            if total_frequency in found_frequencies:
                return total_frequency

            found_frequencies.add(total_frequency)

    return None

if __name__ == '__main__':
    frequencies = read_frequencies()
    total = sum_frequencies(frequencies)
    print("Total: {}".format(total))
    repeating_freq = find_repeating_frequency(frequencies)
    print("First repeating: {}".format(repeating_freq))
