import pytest
import common_math

class TestCommonMath(object):

    def test_add(self):
        result = common_math.add(1, 2)
        assert result == 3