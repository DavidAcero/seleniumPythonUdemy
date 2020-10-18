import pytest

@pytest.fixture()
def setUp():
    print("Running demo2 setUp")
    yield # After Yield will run when test finish
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")