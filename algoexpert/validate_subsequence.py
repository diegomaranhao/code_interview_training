def is_valid_subsequence(array, sequence):
    sequence_initial_index = 0
    sequence_final_index = len(sequence) - 1
    array_size = len(array)

    for number in range(array_size):
        if sequence[sequence_initial_index] == array[number]:
            if sequence_initial_index < sequence_final_index:
                sequence_initial_index += 1
            else:
                return True
    return False


def is_valid_subsequence_2(array, sequence):
    array_index = 0
    sequence_index = 0

    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)

if __name__ == '__main__':
    print(is_valid_subsequence_2([1, 2, 3], [1, 2, 8]))
    print(is_valid_subsequence_2([1, 2, 3], [1, 2]))
