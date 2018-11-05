from pyhonassign.assignment import Airplane
import unittest
class assignmenttest(unittest.TestCase):
    def test_test1(self):
        test1=Airplane.checkairplanemode(Airplane)
    @unittest.skip("no need")
    def test_test2(self):
        test2=Airplane.aiplane_toggle(Airplane)
        print(test2)
    def test_test3(self):
        test3=Airplane.sim_status(Airplane)

    def test_test4(self):
        test4 = Airplane.total(Airplane)


if __name__ == '__main__' :
    unittest.main()
    #suite=unittest.TestLoader().loadTestsFromTestCase(assignmenttest)
