import random
import time

class AgenteBuscador:
    def __init__(self, columnas=5):
        self.columnas = columnas
        self.posicion_agente = [0, 0]
        self.object_position = [random.randint(0, columnas-1), random.randint(0, columnas-1)]  # Posición del objeto
    
    def display_columna(self):
        for i in range(self.columnas):
            row = []
            for j in range(self.columnas):
                if [i, j] == self.posicion_agente:
                    row.append("A")
                elif [i, j] == self.object_position:  # Corregido para mostrar "R"
                    row.append("R")
                else:
                    row.append(".")
            print(" ".join(row))
        print()
    
    def move_agent(self):
        if self.posicion_agente[0] < self.object_position[0]:
            self.posicion_agente[0] += 1
        elif self.posicion_agente[0] > self.object_position[0]:
            self.posicion_agente[0] -= 1
        elif self.posicion_agente[1] < self.object_position[1]:
            self.posicion_agente[1] += 1
        elif self.posicion_agente[1] > self.object_position[1]:
            self.posicion_agente[1] -= 1
    
    def buscador(self):
        while self.posicion_agente != self.object_position:
            self.display_columna()
            self.move_agent()
            time.sleep(0.5)
        self.display_columna()
        print("Objeto encontrado!")

if __name__ == "__main__":
    agent = AgenteBuscador()
    agent.buscador()