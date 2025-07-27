# Clase Hierba para Cuyaventura Pastusa
import pygame
class Hierba:
    def __init__(self, x, y):
        self.imagen = pygame.image.load('assets/hierba.png')
        self.imagen = pygame.transform.scale(self.imagen, (30, 30))  # Redimensionar a 30x30 píxeles
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.comida = False
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
