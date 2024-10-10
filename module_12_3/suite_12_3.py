import unittest
import module_12_3

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
