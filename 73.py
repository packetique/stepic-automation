
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)
print('Expected: ')
x1 = input()
print('Actual: ')
x2 = input()
test_input_text(x1, x2)

