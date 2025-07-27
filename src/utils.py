# Funciones utilitarias para Cuyaventura Pastusa
import pygame

def cargar_imagen(ruta):
    return pygame.image.load(ruta)

def mostrar_texto(pantalla, texto, tamano, posicion, color):
    fuente = pygame.font.SysFont('arial', tamano)
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=posicion)
    pantalla.blit(superficie, rect)
