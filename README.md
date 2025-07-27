# Cuyaventura Pastusa

PARA EJECUTAR, INRRESAR AL LINK EN LA CARPETA LLAMADA "EJECUTABLE"

¡Bienvenido a Cuyaventura Pastusa!

Este es un juego de plataformas 2D desarrollado en Python con Pygame, inspirado en los clásicos de Mario Bros, pero con temática andina y personajes típicos de la región de Pasto, Colombia.

## Características principales
- **Protagonista:** Un cuy (conejillo de indias) que debe llegar a la meta.
- **Enemigos:** Perros que patrullan y persiguen al cuy. En el nivel 2 hay más perros y mayor dificultad.
- **Obstáculos:** Rocas y casas ubicadas estratégicamente en cada nivel.
- **Plataformas:** Terrazas de diferentes alturas y posiciones en cada nivel.
- **Coleccionables:** Hierbas que el cuy debe recolectar para poder ganar el nivel.
- **Meta:** Una bandera dorada al final de cada nivel.
- **Cámara desplazable:** El escenario se mueve siguiendo al cuy.
- **Doble salto:** El cuy puede saltar dos veces en el aire.
- **Menú principal:** Con opciones de jugar, instrucciones, controles, acerca de, activar/desactivar música y salir.
- **Menú en juego:** Accesible con ESC, permite ver instrucciones, controles, acerca de, activar/desactivar música y volver al juego o al menú principal.
- **Pop-ups informativos:** Ventanas emergentes para instrucciones, controles y acerca de, con botón de cerrar.
- **Transición automática de niveles:** Al completar un nivel, se pasa automáticamente al siguiente.
- **Pantalla final:** Mensaje de felicitaciones al completar ambos niveles.
- **Música de fondo:** Activable/desactivable desde el menú.

## Estructura del proyecto

```
├── README.md
├── assets/
│   ├── casa.png
│   ├── cuy.png
│   ├── fondo1.jpg
│   ├── fondo2.jpg
│   ├── hierba.png
│   ├── Music.mp3
│   ├── perro.png
│   └── roca.png
├── docs/
├── src/
│   ├── __init__.py
│   ├── cuy.py
│   ├── hierba.py
│   ├── main.py
│   ├── nivel.py
│   ├── perro.py
│   ├── utils.py
│   └── __pycache__/
└── ...
```

## Instalación y ejecución

1. **Requisitos:**
   - Python 3.8 o superior
   - Pygame 2.x

2. **Instala las dependencias:**
   ```bash
   pip install pygame
   ```

3. **Ejecuta el juego:**
   ```bash
   python src/main.py
   ```

## Cómo jugar
- **Objetivo:** Ayuda al cuy a llegar a la meta dorada recolectando todas las hierbas y evitando a los perros y obstáculos.
- **Controles:**
  - Flechas izquierda/derecha o A/D: Moverse
  - Espacio o Flecha arriba: Saltar (doble salto)
  - ESC: Menú en juego
  - Mouse: Navegar por los menús y pop-ups
- **Música:** Puedes activar o desactivar la música desde el menú principal o el menú en juego.

## Niveles
- **Nivel 1:**
  - Obstáculos y enemigos básicos, terrazas y rocas en posiciones iniciales.
- **Nivel 2:**
  - Mayor dificultad: más perros, terrazas y rocas en nuevas posiciones, y un perro adicional.
  - El diseño del nivel 2 es diferente y más desafiante.

## Menús y pop-ups
- **Menú principal:**
  - Jugar: Inicia el juego desde el primer nivel.
  - Cómo jugar: Muestra el objetivo del juego.
  - Controles: Explica los controles.
  - Acerca de: Información del autor y el proyecto.
  - Música: Activa o desactiva la música de fondo.
  - Salir: Cierra el juego.
- **Menú en juego:**
  - Accesible con ESC.
  - Permite ver instrucciones, controles, acerca de, activar/desactivar música, volver al juego o al menú principal.
- **Pop-ups:**
  - Ventanas emergentes con información, cerrables con un botón "X".

## Créditos
- **Autor:** Dylan Rivera
- **Kodland 2025**
- **Imágenes y música:** Incluidas en la carpeta `assets/`.

## Notas técnicas
- El código está modularizado en clases: `Cuy`, `Perro`, `Hierba`, `Nivel` y utilidades.
- El juego utiliza cámara desplazable y lógica de colisiones robusta.
- El menú y los pop-ups están implementados con soporte para teclado y mouse.
- El juego es fácilmente ampliable para más niveles o mecánicas.

---

¡Disfruta Cuyaventura Pastusa y demuestra tus habilidades de plataformas!
