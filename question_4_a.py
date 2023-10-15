from question_3 import filterData


def test_low_coverage_mult():
    # This tests the multiplcation functaionality (item > limit)
    data = [10, 20, 30, 40]
    limit = 5
    exceptions = []
    output = filterData(data, limit, exceptions)
    ground_truth = [10 * 2, 20 * 2, 30 * 2, 40 * 2]
    assert output == ground_truth


def test_low_coverage_div():
    # This tests the division funcationality (else statement)
    data = [10, 20, 30, 40]
    limit = 100
    exception = []
    output = filterData(data, limit, exception)
    ground_truth = [10 / 100, 20 / 100, 30 / 100, 40 / 100]
    assert output == ground_truth


def test_mid_coverage():
    # This tests the multiplication and division funcationality together
    data = [10, 20, 30, 40]
    limit = 20
    exception = []
    output = filterData(data, limit, exception)
    ground_truth = [10 / 20, 20 / 20, 30 * 2, 40 * 2]
    assert output == ground_truth


def test_all_coverage():
    data = [10, 20, 30, 40]
    limit = 20
    exception = [30]
    output = filterData(data, limit, exception)
    ground_truth = [10 / 20, 20 / 20, "30_EXCEPTION", 40 * 2]
    assert output == ground_truth