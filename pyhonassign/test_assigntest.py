from pyhonassign.assignment import Airplane
import pytest
class Test:
    def test_test1(self):
        test1 = Airplane.checkairplanemode(Airplane)
    def test_test2(self):
        test2 = Airplane.sim_status(Airplane)
    @pytest.mark.skip
    def test_skip(self):
        test=Airplane.aiplane_toggle(Airplane)
    def test_test3(self):
        test3 = Airplane.sms(Airplane)
    def test_test4(self):
        test4 = Airplane.total(Airplane)


if __name__ == '__main__':
    pytest.main()