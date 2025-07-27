# Lógica de niveles para Cuyaventura Pastusa
import pygame
from src.cuy import Cuy
from src.perro import Perro
from src.hierba import Hierba
from src.utils import mostrar_texto
import sys
# pylint: disable=no-member

class Nivel:
    def __init__(self, pantalla, numero):
        self.pantalla = pantalla
        self.numero = numero
        # Ajustar la posición inicial del cuy y los perros para evitar colisiones inmediatas
        self.cuy = Cuy(50, 450)  # Ajustar posición inicial del cuy
        self.perros = [Perro(300, 400), Perro(600, 350)]  # Ajustar posiciones iniciales de los perros lejos del cuy

        for perro in self.perros:
            perro.movimiento_oscilante = True  # Activar movimiento oscilante

        self.hierbas = [Hierba(150, 520), Hierba(400, 520), Hierba(650, 520), Hierba(250, 400), Hierba(550, 400)]
        self.terrazas = [pygame.Rect(200, 450, 150, 20), pygame.Rect(500, 350, 180, 20)]
        # Crear un fondo temporal si no existe el archivo
        try:
            fondo_nombre = f'fondo{numero}.JPG'
            self.fondo = pygame.image.load(f'assets/{fondo_nombre}')
        except FileNotFoundError:
            # Crear un fondo temporal
            self.fondo = pygame.Surface((800, 600))
            self.fondo.fill((135, 206, 250))  # Color celeste de fondo
            
        self.terminado = False
        
        # Intentar cargar la música si existe
        try:
            pygame.mixer.music.load('assets/Music.mp3')
            pygame.mixer.music.play(-1)  # Repetir en bucle
        except pygame.error:
            print("Música no encontrada, continuando sin audio")

        # Añadir rocas y casas como obstáculos
        self.rocas = [pygame.Rect(500, 500, 50, 50), pygame.Rect(900, 500, 50, 50), pygame.Rect(1300, 500, 50, 50)]
        self.casas = [pygame.Rect(1100, 350, 120, 170), pygame.Rect(1600, 350, 120, 170)]

        # Cambiar estructura del nivel 2: terrazas, rocas, casas y más perros
        if self.numero == 2:
            # Perros en posiciones más difíciles y uno adicional
            self.perros = [
                Perro(350, 500),   # Cerca del inicio
                Perro(900, 420),   # En el centro
                Perro(1450, 350)   # Cerca de la meta, sobre terraza
            ]
            for perro in self.perros:
                perro.movimiento_oscilante = True
            # Terrazas en nuevas posiciones
            self.terrazas = [
                pygame.Rect(250, 480, 180, 20),   # Más alta y más lejos
                pygame.Rect(800, 400, 200, 20),   # Centro
                pygame.Rect(1400, 330, 180, 20)   # Cerca de la meta
            ]
            # Rocas en lugares diferentes
            self.rocas = [
                pygame.Rect(600, 540, 50, 50),    # Antes de la terraza central
                pygame.Rect(1200, 540, 50, 50),   # Después de la terraza central
                pygame.Rect(1700, 500, 50, 50)    # Cerca de la meta
            ]
            # Casas en nuevas posiciones
            self.casas = [
                pygame.Rect(1050, 370, 120, 170),
                pygame.Rect(1750, 350, 120, 170)
            ]

        # Añadir señal de meta al extremo derecho
        self.meta = pygame.Rect(1850, 400, 40, 120)  # Señal de meta
        self.cuy_pos_inicial = (50, 450)

        # Variables para el desplazamiento de cámara
        self.camara_x = 0

    def actualizar_camara(self):
        # Actualizar la posición de la cámara para seguir al cuy
        self.camara_x = max(0, self.cuy.rect.x - 400)

    def dibujar(self):
        # Dibujar el fondo repetido horizontalmente para cubrir todo el nivel
        ancho_fondo = self.fondo.get_width()
        x_inicio = -self.camara_x % ancho_fondo
        for i in range(-1, 4):
            self.pantalla.blit(self.fondo, (x_inicio + i * ancho_fondo, 0))

        # Dibujar terrazas desplazadas
        for terraza in self.terrazas:
            terraza_desplazada = terraza.move(-self.camara_x, 0)
            pygame.draw.rect(self.pantalla, (139, 69, 19), terraza_desplazada)
        # Dibujar rocas desplazadas (con imagen si existe)
        for roca in self.rocas:
            roca_desplazada = roca.move(-self.camara_x, 0)
            try:
                img_roca = pygame.image.load('assets/roca.png')
                img_roca = pygame.transform.scale(img_roca, (50, 50))
                self.pantalla.blit(img_roca, roca_desplazada)
            except:
                pygame.draw.rect(self.pantalla, (105, 105, 105), roca_desplazada)
        # Dibujar casas desplazadas (con imagen si existe)
        for casa in self.casas:
            casa_desplazada = casa.move(-self.camara_x, 0)
            try:
                img_casa = pygame.image.load('assets/casa.png')
                img_casa = pygame.transform.scale(img_casa, (120, 170))
                self.pantalla.blit(img_casa, casa_desplazada)
            except:
                pygame.draw.rect(self.pantalla, (139, 69, 19), casa_desplazada)
        # Dibujar meta desplazada
        meta_desplazada = self.meta.move(-self.camara_x, 0)
        pygame.draw.rect(self.pantalla, (255, 215, 0), meta_desplazada)  # Color dorado para la meta
        # Dibujar bandera de meta
        pygame.draw.polygon(self.pantalla, (255,0,0), [(meta_desplazada.x+20, meta_desplazada.y), (meta_desplazada.x+60, meta_desplazada.y+20), (meta_desplazada.x+20, meta_desplazada.y+40)])

        # Dibujar hierbas desplazadas
        for hierba in self.hierbas:
            if not hierba.comida:
                rect_orig = hierba.rect.copy()
                hierba.rect.x = rect_orig.x - self.camara_x
                hierba.dibujar(self.pantalla)
                hierba.rect = rect_orig
        # Dibujar perros desplazados
        for perro in self.perros:
            rect_orig = perro.rect.copy()
            perro.rect.x = rect_orig.x - self.camara_x
            perro.dibujar(self.pantalla)
            perro.rect = rect_orig
        # Dibujar cuy desplazado
        rect_orig = self.cuy.rect.copy()
        self.cuy.rect.x = rect_orig.x - self.camara_x
        self.cuy.dibujar(self.pantalla)
        self.cuy.rect = rect_orig

    def jugar(self, menu_ingame=None):
        reloj = pygame.time.Clock()
        self.terminado = False
        nivel_completado = False
        mostrar_mensaje_final = False
        resultado = None
        # Esperar 1 segundo antes de iniciar el nivel (después del menú)
        pygame.time.wait(1000)
        while not self.terminado:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                        self.cuy.saltar()
                    if evento.key == pygame.K_ESCAPE and menu_ingame:
                        res = menu_ingame()
                        if res == 'menu_principal':
                            self.terminado = True
                            return 'menu_principal'
                        # Si es 'volver', simplemente continúa
            # Si el nivel fue completado, mostrar mensaje y pausar
            if mostrar_mensaje_final:
                self.dibujar()
                mostrar_texto(self.pantalla, '¡Nivel completado!', 50, (400, 200), (0, 150, 0))
                mostrar_texto(self.pantalla, 'Presiona ENTER para continuar', 32, (400, 300), (0,0,0))
                pygame.display.flip()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                        return 'completado'
                reloj.tick(30)
                continue
            teclas = pygame.key.get_pressed()
            # Solo permitir movimiento si no se ha completado el nivel
            if not nivel_completado:
                self.cuy.mover(teclas)
                self.cuy.actualizar_salto(self.terrazas)
            self.actualizar_camara()
            # Lógica de colisión con rocas y casas
            for roca in self.rocas:
                if self.cuy.rect.colliderect(roca):
                    if self.cuy.rect.centerx < roca.centerx:
                        self.cuy.rect.right = roca.left
                    else:
                        self.cuy.rect.left = roca.right
            for casa in self.casas:
                if self.cuy.rect.colliderect(casa):
                    if self.cuy.rect.centerx < casa.centerx:
                        self.cuy.rect.right = casa.left
                    else:
                        self.cuy.rect.left = casa.right
            # Lógica de enemigos
            if not nivel_completado:
                for perro in self.perros:
                    perro.mover()
                    if self.cuy.rect.colliderect(perro.rect):
                        self.cuy.vida -= 1
                        pygame.time.wait(500)
                        self.cuy.rect.x, self.cuy.rect.y = self.cuy_pos_inicial
                        if self.cuy.vida <= 0:
                            self.terminado = True
                            return 'game_over'
            # Lógica de hierba
            for hierba in self.hierbas:
                if not hierba.comida and self.cuy.rect.colliderect(hierba.rect):
                    hierba.comida = True
                    if self.cuy.vida < 5:
                        self.cuy.vida += 1
            # Verificar si llegó a la meta
            if not nivel_completado and self.cuy.rect.colliderect(self.meta):
                hierbas_faltantes = len([h for h in self.hierbas if not h.comida])
                if hierbas_faltantes == 0:
                    nivel_completado = True
                    mostrar_mensaje_final = True
                    continue
                else:
                    # Mostrar mensaje de hierbas faltantes
                    self.dibujar()
                    mostrar_texto(self.pantalla, f'Te falta consumir {hierbas_faltantes}/ {len(self.hierbas)} hierbas', 36, (400, 200), (200, 0, 0))
                    mostrar_texto(self.pantalla, 'Debes recolectar toda la hierba para ganar', 28, (400, 260), (0,0,0))
                    pygame.display.flip()
                    pygame.time.wait(1800)
                    # Retroceder al cuy un poco para evitar que se quede en la meta
                    self.cuy.rect.x -= 60
                    # No permite completar el nivel hasta recolectar toda la hierba
                    continue
            # Dibujar todo
            self.dibujar()
            mostrar_texto(self.pantalla, f'Vida: {self.cuy.vida}', 30, (80, 30), (255,0,0))
            mostrar_texto(self.pantalla, 'ESC: Menú', 22, (700, 30), (0,0,0))
            pygame.display.flip()
            reloj.tick(60)
        return resultado
