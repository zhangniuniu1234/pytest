import allure
import pytest
from testpy.cal import  Calc
import  yaml


#加载测试步骤yml文件
def load_step():
    with open("data/test_step.yml",'r') as f:
        f.seek(0)
        steps=yaml.safe_load(f)
        return steps



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


@allure.feature("测试用例类")
class TestCalc:


    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/add.yml")))
    @pytest.mark.add
    @allure.step("测试加法函数")
    def calc_add(self,fixture_setup, a, b, exp):
        steps=load_step()
        for step in  steps:
            if 'add' in step:
                if (isinstance(a, (int, float)) is not True) or isinstance(b, (int, float)) is not True :
                    # pytest.skip("不支持非整数的参数")
                    raise TypeError("传入的参数不是整数")

                result = fixture_setup.add(a, b)
                print(result)
                if compare_float(result, exp, 0.00001):
                    exp = result
                assert result == exp



    @pytest.mark.parametrize('a,b,exp',
                             yaml.safe_load(open("data/div.yml")))
    @pytest.mark.div
    @allure.step("测试除法函数")
    def calc_div(self,fixture_setup, a, b, exp):
        steps=load_step()
        for step in steps:
            if 'div' in step:
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
    # load_step()
    pytest.main(["-v","-s","-m add or div"])








