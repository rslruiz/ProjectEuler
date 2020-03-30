class Test(object):
    @classmethod
    def assert_equals(self,actual,expected, text=''):
#        print(actual, expected)
        if actual == expected:
            return print(f'pass')
        else:
            return print(f'fail {text}')

def multiplesOf3and5(number):
    return sum(i for i in range(number) if not i%3 or not i%5)

Test.assert_equals(multiplesOf3and5(10), 23)
Test.assert_equals(multiplesOf3and5(49), 543)
Test.assert_equals(multiplesOf3and5(1000), 233168)
Test.assert_equals(multiplesOf3and5(8456), 16687353)
Test.assert_equals(multiplesOf3and5(19564), 89301183)