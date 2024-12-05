def nejvetsi(seznam_cisel):
    return max(seznam_cisel)

def test_nejvetsi():
    assert nejvetsi([1, 2, 3, 4, 5]) == 5, "Test case 1 failed"
    assert nejvetsi([10, 20, 30, 40, 50]) == 50, "Test case 2 failed"
    assert nejvetsi([-1, -2, -3, -4, -5]) == -1, "Test case 3 failed"
    assert nejvetsi([0, 0, 0]) == 0, "Test case 4 failed"
    assert nejvetsi([100, 200, 300, 400, 500]) == 500, "Test case 5 failed"
    assert nejvetsi([7]) == 7, "Test case 6 failed"