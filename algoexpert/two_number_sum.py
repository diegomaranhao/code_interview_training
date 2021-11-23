# O(n^2) time | O(1) space
def two_number_sum_1(array, targetSum):
    for first_number in array:
        for second_number in array:
            if first_number != second_number:
                if first_number + second_number == targetSum:
                    return [first_number, second_number]
    return []

# O(nlog(n)) time | O(1) space
def two_number_sum_2(array, targetSum):
    array = sorted(array)
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        current_sum = array[left_pointer] + array[right_pointer]
        if current_sum == targetSum:
            return [array[left_pointer], array[right_pointer]]
        elif array[left_pointer] + array[right_pointer] < targetSum:
            left_pointer += 1
        elif array[left_pointer] + array[right_pointer] > targetSum:
            right_pointer -= 1
    return []

# o(n) time | o(n) space
def two_number_sum_3(array, targetSum):
    hash_table = {}
    for number in array:
        potentialMatch = targetSum - number
        if potentialMatch in hash_table:
            return [number, potentialMatch]
        else:
            hash_table[number] = True
    return []


if __name__ == '__main__':
    print(two_number_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum_2([6], 10))
