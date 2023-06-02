class Triqui:
    def _init_(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador = 'X'
        
    def imprimir_tablero(self):
        print('---------')
        for fila in self.tablero:
            print('|', end='')
            for cell in fila:
                print(cell, end='|')
            print('\n---------')

    def enLinea(self, fila, col):
        if self.tablero[fila][col] == ' ':
            self.tablero[fila][col] = self.jugador
            self.jugador = 'O' if self.jugador == 'X' else 'X'
        else:
            print('Movimiento invalido. Intenta de nuevo.')

