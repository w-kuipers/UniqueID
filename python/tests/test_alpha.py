from simpleuid import alpha

def test_alphanumeric():
    assert alpha().isalpha() == True

def test_alphanumeric_length():
    assert len(alpha()) == 10
    assert len(alpha(length=200)) == 200

def test_alphanumeric_prefix():
    assert alpha(prefix="test")[:4] == "test"
