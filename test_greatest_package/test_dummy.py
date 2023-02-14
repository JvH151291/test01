import unittest
from unittest import skip


class ExampleTestCase(unittest.TestCase):
    def test_something_that_is_true(self) -> None:
        self.assertEqual(True, True)

    @skip
    def skip_me(self) -> None:
        self.assertEqual(False, True)

    def test_some_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            a = 1 / 0


if __name__ == "__main__":
    unittest.main()
