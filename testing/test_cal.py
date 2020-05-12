import pytest
from testpy.cal import  Calc
import  yaml


#判断两个浮点数是否相等
def compare_float(a, b, precision):
    if precision == 0:
        return a == b
    elif precision < 0:
        raise Exception('precision 不能小于0')
    elif precision >= 1:
        if abs(a - b) <= precision:
            return True
    else:
        if (1 / precision) * abs(a - b) <= 1:
            return True
    return False


class TestCalc:


    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/add.yml")))
    @pytest.mark.add
    def calc_add(self,fixture_setup, a, b, exp):
        if isinstance(a,(int,float) ) is not True:
            raise TypeError("传入的参数不是整数")

        result=fixture_setup.add(a,b)
        print(result)
        if compare_float(result,exp,0.00001):
            exp = result
        assert result == exp


    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/div.yml")))
    @pytest.mark.div
    def calc_div(self,fixture_setup, a, b, exp):
        try:
            result = fixture_setup.div(a, b)
            if compare_float(result, exp, 0.00001):
                exp = result
        except ZeroDivisionError:
            print("0不能做除数")
        else:
            assert result == exp


    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/mul.yml")))
    @pytest.mark.mul
    def calc_mul(self, fixture_setup, a, b, exp):
        result = fixture_setup.mul(a, b)
        assert result==exp


    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/sub.yml")))
    @pytest.mark.sub
    def calc_sub(self, fixture_setup, a, b, exp):
        result = fixture_setup.sub(a, b)
        if compare_float(result, exp, 0.00001):
            exp = result
        assert result == exp






if __name__=="__main__":
    pytest.main(["-v","-s","-m add or div"])







