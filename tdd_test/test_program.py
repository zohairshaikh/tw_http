
from tdd_test.program import is_valid_ifsc, fetch_branch_details_razorpay, main
import pytest

def test_is_valid_ifsc():

    assert is_valid_ifsc(9999) == False

    assert is_valid_ifsc('INVALID_IFSC_EXAMPLE') == False

    assert is_valid_ifsc('KARB0000001') == True


def test_fetch_branch_details_razorpay():

    with pytest.raises(ValueError) as er:
        fetch_branch_details_razorpay("INVALID_IFSC_EXAMPLE")

        assert "Invalid IFSC" in str(er)

    assert fetch_branch_details_razorpay("KARB0000001") == "DAKSHINA KANNADA"




def test_main(capsys):
    main("INVALID_IFSC_TEST")
    captured = capsys.readouterr()
    assert captured.out == "Invalid IFSC\n"

    main("KARA0000221")
    captured = capsys.readouterr()
    assert 'Invalid IFSC\n' in str(captured.out)

    main("KARB0000001")
    captured = capsys.readouterr()
    assert captured.out == "DAKSHINA KANNADA\n"





