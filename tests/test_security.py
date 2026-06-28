# tests/test_security.py

from security.access_control import has_access

def test_access():

    assert has_access("admin", "delete") == True

    assert has_access("viewer", "write") == False

    print("TEST PASSED")


if __name__ == "__main__":
    test_access()