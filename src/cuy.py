# Clase Cuy para Cuyaventura Pastusa
import pygame
# pylint: disable=no-member
class Cuy:
    def __init__(self, x, y):
# Manejo temporal para el cuy si falta el archivo de imagen
        try:
            self.imagen = pygame.image.load('assets/cuy.png')
            self.imagen = pygame.transform.scale(self.imagen, (40, 30))  # Redimensionar a 40x30 píxeles
        except FileNotFoundError:
            self.imagen = pygame.Surface((40, 30))
            self.imagen.fill((139, 69, 19))  # Color marrón para el cuy

        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.velocidad = 5
        self.vida = 3  # Cambié de 1 a 3 para mejor jugabilidad
        self.saltando = False
        self.vel_y = 0
        self.en_suelo = False
        self.saltos_restantes = 2  # Para doble salto
    def mover(self, teclas):
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if self.rect.x < 0:
            self.rect.x = 0
        # Eliminar límite derecho para permitir avanzar por todo el nivel
    def saltar(self):
        if self.saltos_restantes > 0:
            self.saltando = True
            self.vel_y = -15
            self.en_suelo = False
            self.saltos_restantes -= 1
    def actualizar_salto(self, terrazas):
        self.rect.y += self.vel_y
        self.vel_y += 1  # gravedad
        if self.rect.y >= 500:
            self.rect.y = 500
            self.vel_y = 0
            self.saltando = False
            self.en_suelo = True
            self.saltos_restantes = 2  # Restablecer doble salto al tocar el suelo
        else:
            self.en_suelo = False
            for terraza in terrazas:
                if self.rect.colliderect(terraza) and self.vel_y > 0:
                    self.rect.bottom = terraza.top
                    self.vel_y = 0
                    self.saltando = False
                    self.en_suelo = True
                    self.saltos_restantes = 2  # Restablecer doble salto al tocar terraza
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
