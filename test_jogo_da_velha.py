import pytest
from jogo_da_velha import JogoDaVelha

@pytest.fixture
def jogo():
    return JogoDaVelha()

def test_jogada_valida(jogo):
    jogo.jogar(0, 0)
    assert jogo.tabuleiro[0][0] == 'X'
    assert jogo.jogador == 'O'

def test_jogada_invalida(jogo):
    jogo.jogar(0, 0)
    jogo.jogar(0, 0)  
    assert jogo.tabuleiro[0][0] == 'X'
    assert jogo.jogador == 'O'

def test_vencedor_linha(jogo):
    jogo.jogar(0, 0)  
    jogo.jogar(1, 0)  
    jogo.jogar(0, 1)  
    jogo.jogar(1, 1)  
    jogo.jogar(0, 2) 
    assert jogo.vencedor == 'X'

def test_vencedor_coluna(jogo):
    jogo.jogar(0, 1)  
    jogo.jogar(0, 0)  
    jogo.jogar(1, 1)  
    jogo.jogar(1, 0)  
    jogo.jogar(2, 1)  
    assert jogo.vencedor == 'X'

def test_vencedor_diagonal(jogo):
    jogo.jogar(0, 0)  
    jogo.jogar(0, 1)  
    jogo.jogar(1, 1)  
    jogo.jogar(1, 0)  
    jogo.jogar(2, 2)  
    assert jogo.vencedor == 'X'

def test_empate(jogo):
    
    jogo.jogar(0, 0)  
    jogo.jogar(0, 1)  
    jogo.jogar(0, 2)  
    jogo.jogar(1, 1)  
    jogo.jogar(1, 0) 
    jogo.jogar(2, 0)  
    jogo.jogar(1, 2)  
    jogo.jogar(2, 2)  
    jogo.jogar(2, 1)  
    assert jogo.vencedor is None