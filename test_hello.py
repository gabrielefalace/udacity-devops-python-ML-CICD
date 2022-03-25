from hello import to_you, add, sub

def setup_function(test_func):
    print("Running Setup %s" % test_func.__name__)
    test_func.x = 10

def teardown_function(test_func):
    print("Running Teardown %s" % test_func.__name__)
    del test_func.x

def test_hello_subtract():
    assert sub(test_hello_subtract.x) == 9