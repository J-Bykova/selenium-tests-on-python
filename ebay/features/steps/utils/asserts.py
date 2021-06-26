def assert_equal(expected, actual):
    if expected != actual:
        raise AssertionError(f'\n\tExpected: "{expected}"\n\tActual: "{actual}"')