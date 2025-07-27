# Cuyaventura Pastusa - Juego principal
# Autor: Dylan Rivera
# Kodland

import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import mostrar_texto
from src.nivel import Nivel

# Estado de la música como lista mutable para compartir entre menús
musica_activada = [True]
# pylint: disable=no-member

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Cuyaventura Pastusa')
    reloj = pygame.time.Clock()

    # Popup simple reutilizable
    def popup(titulo, lineas):
        ancho, alto = 500, 250
        x, y = 150, 175
        rect = pygame.Rect(x, y, ancho, alto)
        pygame.draw.rect(pantalla, (255,255,255), rect, border_radius=16)
        pygame.draw.rect(pantalla, (139,69,19), rect, 4, border_radius=16)
        mostrar_texto(pantalla, titulo, 36, (x+ancho//2, y+40), (139,69,19))
        for i, linea in enumerate(lineas):
            mostrar_texto(pantalla, linea, 26, (x+ancho//2, y+90+i*32), (0,0,0))
        btn_cerrar = pygame.Rect(x+ancho-40, y+10, 30, 30)
        pygame.draw.rect(pantalla, (200,0,0), btn_cerrar, border_radius=8)
        mostrar_texto(pantalla, 'X', 24, (x+ancho-25, y+25), (255,255,255))
        return btn_cerrar

    # Menú principal
    def menu_loop():
        opciones = [
            '1. Jugar',
            '2. Cómo jugar',
            '3. Controles',
            '4. Acerca de',
            f"5. Música: {'Activada' if musica_activada[0] else 'Desactivada'}",
            '6. Salir'
        ]
        seleccion = 0
        mostrar_info = False
        mostrar_controles = False
        mostrar_acerca = False
        while True:
            pantalla.fill((135, 206, 250))
            mostrar_texto(pantalla, 'CUYAVENTURA PASTUSA', 50, (400, 100), (139,69,19))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_click = False
            for i, opcion in enumerate(opciones):
                color = (0, 100, 0) if i == seleccion else (0,0,0)
                rect = pygame.Rect(200, 210 + i*45, 400, 40)
                if rect.collidepoint(mouse_x, mouse_y):
                    color = (0, 150, 0)
                    seleccion = i
                mostrar_texto(pantalla, opcion, 34, (400, 220 + i*45), color)
            btn_cerrar = None
            if mostrar_info:
                btn_cerrar = popup('OBJETIVO', [
                    'Ayuda al cuy a llegar a la meta,',
                    'evitando perros, saltando terrazas,',
                    'y recolectando toda la hierba.'
                ])
            if mostrar_controles:
                btn_cerrar = popup('CONTROLES', [
                    'Flechas o A/D: Moverse',
                    'Espacio/Arriba: Saltar (doble salto)',
                    'ESC: Menú en juego'
                ])
            if mostrar_acerca:
                btn_cerrar = popup('ACERCA DE', [
                    'Cuyaventura Pastusa',
                    'Autor: Dylan Rivera',
                    'Kodland 2025'
                ])
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(opciones)
                    if evento.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(opciones)
                    if evento.key == pygame.K_RETURN:
                        mouse_click = True
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_click = True
            if btn_cerrar and mouse_click and btn_cerrar.collidepoint(mouse_x, mouse_y):
                mostrar_info = mostrar_controles = mostrar_acerca = False
            elif not (mostrar_info or mostrar_controles or mostrar_acerca) and mouse_click:
                if seleccion == 0:
                    return  # Jugar
                elif seleccion == 1:
                    mostrar_info = True
                elif seleccion == 2:
                    mostrar_controles = True
                elif seleccion == 3:
                    mostrar_acerca = True
                elif seleccion == 4:
                    musica_activada[0] = not musica_activada[0]
                    opciones[4] = f"5. Música: {'Activada' if musica_activada[0] else 'Desactivada'}"
                    if musica_activada[0]:
                        try:
                            pygame.mixer.music.load('assets/Music.mp3')
                            pygame.mixer.music.play(-1)
                        except Exception:
                            pass
                    else:
                        pygame.mixer.music.stop()
                elif seleccion == 5:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            reloj.tick(60)
    def menu_ingame():
        opciones = [
            '1. Cómo jugar',
            '2. Controles',
            '3. Acerca de',
            f"4. Música: {'Activada' if musica_activada[0] else 'Desactivada'}",
            '5. Volver al juego',
            '6. Volver al menú principal'
        ]
        seleccion = 0
        mostrar_info = False
        mostrar_controles = False
        mostrar_acerca = False
        while True:
            pantalla.fill((135, 206, 250))
            mostrar_texto(pantalla, 'MENÚ EN JUEGO', 50, (400, 100), (139,69,19))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_click = False
            for i, opcion in enumerate(opciones):
                color = (0, 100, 0) if i == seleccion else (0,0,0)
                rect = pygame.Rect(200, 210 + i*45, 400, 40)
                if rect.collidepoint(mouse_x, mouse_y):
                    color = (0, 150, 0)
                    seleccion = i
                mostrar_texto(pantalla, opcion, 34, (400, 220 + i*45), color)
            btn_cerrar = None
            if mostrar_info:
                btn_cerrar = popup('OBJETIVO', [
                    'Ayuda al cuy a llegar a la meta,',
                    'evitando perros, saltando terrazas,',
                    'y recolectando toda la hierba.'
                ])
            if mostrar_controles:
                btn_cerrar = popup('CONTROLES', [
                    'Flechas o A/D: Moverse',
                    'Espacio/Arriba: Saltar (doble salto)',
                    'ESC: Menú en juego'
                ])
            if mostrar_acerca:
                btn_cerrar = popup('ACERCA DE', [
                    'Cuyaventura Pastusa',
                    'Autor: Dylan Rivera',
                    'Kodland 2025'
                ])
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(opciones)
                    if evento.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(opciones)
                    if evento.key == pygame.K_RETURN:
                        mouse_click = True
                    if evento.key == pygame.K_ESCAPE:
                        return 'volver'
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_click = True
            if btn_cerrar and mouse_click and btn_cerrar.collidepoint(mouse_x, mouse_y):
                mostrar_info = mostrar_controles = mostrar_acerca = False
            elif not (mostrar_info or mostrar_controles or mostrar_acerca) and mouse_click:
                if seleccion == 0:
                    mostrar_info = True
                elif seleccion == 1:
                    mostrar_controles = True
                elif seleccion == 2:
                    mostrar_acerca = True
                elif seleccion == 3:
                    musica_activada[0] = not musica_activada[0]
                    opciones[3] = f"4. Música: {'Activada' if musica_activada[0] else 'Desactivada'}"
                    if musica_activada[0]:
                        try:
                            pygame.mixer.music.load('assets/Music.mp3')
                            pygame.mixer.music.play(-1)
                        except Exception:
                            pass
                    else:
                        pygame.mixer.music.stop()
                elif seleccion == 4:
                    return 'volver'
                elif seleccion == 5:
                    return 'menu_principal'
            pygame.display.flip()
            reloj.tick(60)



    # Lanzar menú principal
    menu_loop()

    # Iniciar niveles y mostrar mensaje final
    try:
        for nivel_num in [1, 2]:
            print(f"Iniciando Nivel {nivel_num}")
            nivel = Nivel(pantalla, nivel_num)
            resultado = None
            while True:
                resultado = nivel.jugar(menu_ingame)
                if resultado == 'menu_principal':
                    # Volver al menú principal
                    menu_loop()
                    break  # Rompe el ciclo y reinicia el nivel
                elif resultado == 'completado':
                    break  # Siguiente nivel
                elif resultado == 'game_over':
                    pantalla.fill((44, 62, 80))
                    mostrar_texto(pantalla, f'Game Over - Nivel {nivel_num}', 50, (400, 250), (255,255,255))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    break
            if resultado != 'completado':
                break  # Si no completó, termina el juego
        else:
            pantalla.fill((0, 100, 0))
            mostrar_texto(pantalla, '¡FELICITACIONES!', 50, (400, 200), (255,255,255))
            mostrar_texto(pantalla, 'Has acabado el juego', 40, (400, 300), (255,255,255))
            pygame.display.flip()
            pygame.time.wait(4000)
    except Exception as e:
        print(f"Error en el juego: {e}")
    pygame.quit()



if __name__ == '__main__':
    main()
