def add(a, b):
    return a + b


def test_add():
    expected = 15
    actual = add(10, 5)

    if actual == expected:
        print("Test Passed")
    else:
        print("Test Failed")


test_add()