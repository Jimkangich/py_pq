

from bank import greeting_return


def test_correct_greetings():
    assert greeting_return("Hello") == "$0"
    assert greeting_return("Hum") == "$20"
    assert greeting_return("ello") == "$100"
    assert greeting_return("Ohio") == "$100"
    assert greeting_return("wadup") == "$100"
    assert greeting_return("Hello, Newman") == "$0"
    assert greeting_return("How you doing?") == "$20"
    assert greeting_return("What's happening?") == "$100"
