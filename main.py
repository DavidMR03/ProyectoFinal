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

    def Verificar_Ganador(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                return self.tablero[0][col]
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        
        return None
    
    def Jugar(self):
        while True:
            self.imprimir_tablero()
            print(f"Turno de {self.jugador}.")
            fila = int(input('Ingresa la posición de la fila (0-2): '))
            col = int(input('Ingresa la posición de la columna (0-2): '))
            
            self.enLinea(fila, col)
            
            ganador = self.Verificar_Ganador()
            if ganador:
                self.imprimir_tablero()
                print(f'{ganador} gana!')
                break
            
            if all(cell != ' ' for fila in self.tablero for cell in fila):
                self.imprimir_tablero()
                print("¡Empate!")
                break
    game = Triqui()
    game.Jugar()
