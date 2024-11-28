from cviceni8 import obsah_ctverce, obvod_ctverce


def test_obsah_cvtverce():
    assert obsah_ctverce(4) == 16
    assert obsah_ctverce(5) == 25