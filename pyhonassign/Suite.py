from pyhonassign.test import *
import unittest
def suite():
    Suite=unittest.TestSuite()
    Suite.addTest(assignmenttest('test_test1'))
    Suite.addTest(assignmenttest('test_test2'))
    Suite.addTest(assignmenttest('test_test4'))
    return Suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    print(result)

    print("result::errors")

    print(result.errors)


    print("result::failures")

    print(result.failures)

    print( "result::skipped")

    print(result.skipped)


    print("result::successful")

    print(result.wasSuccessful())


    print("result::test-run")

    print(result.testsRun)

    print( "---- END OF TEST RESULTS")


