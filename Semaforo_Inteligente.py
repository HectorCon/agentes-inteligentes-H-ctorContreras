import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado_semaforo = "Red"
        self.cantidad_carros = 0
    
    def dector_carros(self):
        self.cantidad_carros = random.randint(0, 10)  #aca colocamos los vehiculos
        print(f"Vehículos detectados: {self.cantidad_carros}")

    def cambio_color(self):
        if self.estado_semaforo == "Red":
            self.dector_carros()
            tiempo_espera = max(5, min(10, self.cantidad_carros // 2))  # Ajusta el tiempo entre 5 y 10 segundos
            print(f"Cambio a VERDE (duración: {tiempo_espera} seg)")
            self.estado_semaforo = "Green"
        elif self.estado_semaforo == "Green":
            tiempo_espera = 3  # Duración fija 3segundos para amarillo
            print(f"Cambio a AMARILLO (duración: {tiempo_espera} seg)")
            self.estado_semaforo = "Yellow"
        elif self.estado_semaforo == "Yellow":
            tiempo_espera = 5  # Rojo siempre dura 5 seg
            print(f"Cambio a ROJO (duración: {tiempo_espera} seg)")
            self.estado_semaforo = "Red"
        
        time.sleep(tiempo_espera)

    def run(self, ciclo=5):  # la cantidad de ciclos que colocamos en semaforo
        for _ in range(ciclo):
            self.cambio_color()

if __name__ == "__main__":
    trafico = SemaforoInteligente()
    trafico.run()
