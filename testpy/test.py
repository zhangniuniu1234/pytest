import pytest


class TestCase():
    def testOne(self):
        assert 'h' in "hello"

    def testTwo(self):
        assert 2==2

if __name__=="__main__":
    # pytest.main()
    pytest.main('-v -x TestCase::testOne')
    pytest.main(['-v','-s','TestCase::testOne'])

