"""

test for calc app

"""

import calc 

class TestCalcApp:
    def testAdd(self):
        assert 5 == calc.addition(3,2)

    def testSubtraction(self):
        assert 10 == calc.subtraction(20,10)

    def testMultiplication(self):
        assert 50 == calc.multiplication(25, 2)

    def testDivision(self):
        assert 5 == calc.division(125, 5)