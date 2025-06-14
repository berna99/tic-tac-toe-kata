class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[None]*3 for _ in range(3)]  
        self.jogador = 'X'
        self.vencedor = None

    def jogar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] is None and not self.vencedor:
            self.tabuleiro[linha][coluna] = self.jogador
            self.verificar_vencedor()
            self.jogador = 'O' if self.jogador == 'X' else 'X'  

    def verificar_vencedor(self):
        
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] is not None:
                self.vencedor = self.tabuleiro[i][0]
                return
        
        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] is not None:
                self.vencedor = self.tabuleiro[0][j]
                return
        
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] is not None:
            self.vencedor = self.tabuleiro[0][0]
        elif self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] is not None:
            self.vencedor = self.tabuleiro[0][2]