
def average(li):
    if not li:
        return None
    else:
        return sum(li) / len(li)


def test_average():
    test_cases = [
        {
            "name": "Test Case 1",
            "input": [1, 2, 3, 4],
            "expected": 2.5
        },
        {
            "name": "Test Case 2",
            "input": [1, 2, 3],
            "expected": 2
        },
        {
            "name": "Test Case 3",
            "input": [1, 2, 3, 4, 5],
            "expected": 3
        },
        {
            "name": "Test Case 4",
            "input": [1, 2, 3, 4, 5, 6],
            "expected": 3.5
        }
    ] # This is called table driven test. This test is done by making a test case table.
    
    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"]), test_case["name"]
