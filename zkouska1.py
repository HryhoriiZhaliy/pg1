def process_numbers(numbers):
    result = []
    for number in numbers:
        if number == 10:
            break
        if number > 5:
            result.append(number * 2)
    return result

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]