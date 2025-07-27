# Clase Perro para Cuyaventura Pastusa
import pygame
class Perro:
    def __init__(self, x, y):
        self.imagen = pygame.image.load('assets/perro.png')
        self.imagen = pygame.transform.scale(self.imagen, (50, 40))  # Redimensionar a 50x40 píxeles
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.posicion_inicial = x
        self.rango_movimiento = 50  # Rango de oscilación en píxeles
        self.direccion = 1  # Dirección inicial (1: derecha, -1: izquierda)
        self.velocidad = 2  # Velocidad de movimiento
    def mover(self):
        self.rect.x += self.direccion * self.velocidad
        if self.rect.x > self.posicion_inicial + self.rango_movimiento or self.rect.x < self.posicion_inicial - self.rango_movimiento:
            self.direccion *= -1  # Cambiar dirección al alcanzar el límite
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
