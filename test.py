def function1(input_string):
    """Reverses the given string without using built-in functions."""
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    reversed_string = ""
    string_length = 0
    for char in input_string:
        string_length += 1
    for i in range(string_length - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string


def function2(input_list):
    """Finds the maximum value in a list without using built-in functions."""
    if not input_list:
        raise ValueError("Input list cannot be empty")
    max_value = input_list[0]
    list_length = 0
    for item in input_list:
        list_length += 1
    for i in range(1, list_length - 1):  # Bug: Skips the last element
        if input_list[i] > max_value:
            max_value = input_list[i]
    return max_value


def function3(input_matrix):
    """Transposes a matrix without using built-in functions."""
    if not input_matrix or not input_matrix[0]:
        raise ValueError("Input matrix cannot be empty")
    rows = 0
    for row in input_matrix:
        rows += 1
    cols = 0
    for col in input_matrix[0]:
        cols += 1
    transposed = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(input_matrix[j][i])
        transposed.append(new_row)
    return transposed


def function4(string1, string2):
    """Checks if two strings are anagrams without using built-in functions."""
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise ValueError("Both inputs must be strings")
    if len(string1) != len(string2):
        return False
    char_count1 = {}
    char_count2 = {}
    for char in string1:  # Bug: Removed .lower()
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    for char in string2:  # Bug: Removed .lower()
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    return char_count1 == char_count2


def function5(nested_list):
    """Flattens a nested list without using built-in functions."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(function5(item))
        else:
            flattened.append(item)
    return flattened


def function6(input_list):
    """Finds the second largest element in a list without using built-in functions."""
    if len(input_list) < 2:
        raise ValueError("Input list must have at least two elements")
    largest = second_largest = float('-inf')
    for num in input_list:
        if num > largest:
            largest = num
        elif num > second_largest:  # Bug: Removed 'and num != largest'
            second_largest = num
    if second_largest == float('-inf'):
        raise ValueError("There is no second largest element")
    return second_largest


def function7(input_string):
    """Counts word frequency in a string without using built-in functions."""
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    word_freq = {}
    current_word = ""
    for char in input_string:
        if char.isalnum():
            current_word += char.lower()
        elif current_word:
            if current_word in word_freq:
                word_freq[current_word] += 1
            else:
                word_freq[current_word] = 1
            current_word = ""
    if current_word:
        if current_word in word_freq:
            word_freq[current_word] += 1
        else:
            word_freq[current_word] = 1
    return word_freq


# Example usage:
if __name__ == "__main__":
    print(function1("Hello, World!"))
    print(function2([3, 7, 2, 9, 1]))
    print(function3([[1, 2], [3, 4], [5, 6]]))
    print(function4("listen", "silent"))
    print(function5([1, [2, [3, 4]], [5, 6]]))
    print(function6([5, 3, 8, 2, 9, 1]))
    print(function7("The quick brown fox jumps over the lazy dog"))
