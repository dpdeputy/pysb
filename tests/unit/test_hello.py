from base.examples.hello import hello_world


def test_hello_world():
    """Tests the hello_world function."""
    assert hello_world() == "Hello, World!"
