def sudy_lichy(cislo):
    if cislo % 2 == 0:
        return "sudy"
    else:
        return "lichy"

def test_sudy_lichy():
    assert sudy_lichy(2) == "sudy", "Test case 1 failed"
    assert sudy_lichy(3) == "lichy", "Test case 2 failed"
    assert sudy_lichy(0) == "sudy", "Test case 3 failed"
    assert sudy_lichy(-1) == "lichy", "Test case 4 failed"
    assert sudy_lichy(-2) == "sudy", "Test case 5 failed"
    