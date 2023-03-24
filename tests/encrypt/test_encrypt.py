# from challenges.challenge_encrypt_message import encrypt_message
from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("", 5) == ""
    assert encrypt_message("abcdef", 0) == "fedcba"
    assert encrypt_message("abcdef", 7) == "fedcba"
    assert encrypt_message("teste de mensagem", 5) == "etset_megasnem ed "

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcdef", "3")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 5)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 5)
