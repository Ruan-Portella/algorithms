import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('Ruan Portella', 4) == 'alletroP _nauR'
    assert encrypt_message('Ruan Portella', 30) == 'alletroP nauR'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('RuanP', 2.2)
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)
