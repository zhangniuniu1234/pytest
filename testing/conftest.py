from testpy.cal import Calc
import  pytest

@pytest.fixture(scope="module")
def fixture_setup():
    print("\n**********测试初始化，创建calc对象***********\n")
    calc = Calc()
    yield calc
    print("\n***********测试完成***********\n")