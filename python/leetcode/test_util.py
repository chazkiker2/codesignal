import unittest


class AbstractSuite:
    def __init__(self, base_case, functions) -> None:
        self.suite = unittest.TestSuite()
        self.base_case = base_case

        for fn in functions:
            self.suite.addTest(unittest.makeSuite(self.make_base_instance(fn)))

    def make_base_instance(self, fn):
        class AbstractTestCase(self.base_case):
            def setUp(self) -> None:
                super().setUp()
                self.fn = fn
        return AbstractTestCase

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
