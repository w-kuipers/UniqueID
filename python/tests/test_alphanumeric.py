from simpleuid import alphanumeric

def test_alphanumeric():
    assert alphanumeric().isalnum() == True

def test_alphanumeric_length():
    assert len(alphanumeric()) == 10
    assert len(alphanumeric(length=200)) == 200

def test_alphanumeric_prefix():
    assert alphanumeric(prefix="test")[:4] == "test"
