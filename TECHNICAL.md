# Documentación Técnica – RPG Simulator (Edición Tkinter)

## Arquitectura general
El juego utiliza **Tkinter** como capa de presentación y una **máquina de estados finita (FSM)** implementada con frames intercambiables.

Estados:
1. `menu` – Menú principal.
2. `creation` – Creación de personaje (nombre + clase).
3. `exploration` – Mapa de baldosas con movimiento WASD.
4. `combat` – Combate por turnos.
5. `gameover` – Pantalla de derrota.

La clase `Game` (hereda de `tk.Tk`) actúa como controlador y ventana principal. Cada estado es un `tk.Frame` con métodos `on_show()` / `on_hide()` para gestionar bindings de teclas.

## Módulos principales
- `constants.py`: Parámetros globales (estadísticas, colores en hex, balance).
- `characters.py`: Modelos `Jugador` y `Enemigo` con serialización JSON.
- `combat.py`: Funciones puras de cálculo de daño (probables con seed fijo).
- `map_generator.py`: Generación procedural del mapa 5x5 y enemigos escalados.
- `progression.py`: Sistema de niveles y experiencia.
- `persistence.py`: Guardado/carga en `savegame.json`.
- `renderer.py`: Funciones de dibujo con `tk.Canvas` (sprites geométricos, barras).
- `game.py`: FSM, frames y bucle principal (usa `tk.mainloop`).

## Flujo de juego
1. Menú → Nueva/Cargar/Salir.
2. Creación: entrada de nombre (máx 15 caracteres) y selección de clase.
3. Exploración: mapa 5x5, movimiento con W/A/S/D. Al pisar 'E' se inicia combate.
4. Combate: turnos con teclas 1‑4. El enemigo contraataca automáticamente.
5. Victoria → XP, posible subida de nivel, regeneración parcial.
6. Derrota → Game Over → volver al menú.

## Sistema de daño (sin cambios)
- Ataque normal: `max(1, int(ataque * rand(0.8‑1.2)) - defensa//2)`
- Habilidad: `max(1, int(ataque * mult * rand(0.9‑1.1)) - defensa//3)`
- Contraataque enemigo: `max(1, int(ataque * rand(0.8‑1.2)) - defensa//2)`

## Guardado / Carga
- Archivo `savegame.json` contiene diccionario del jugador.
- El mapa se regenera al cargar; solo se conserva posición y estado del personaje.

## Tecnología
- **Tkinter**: interfaz nativa, cero dependencias externas.
- Compatible con Python 3.10+ (incluido 3.13+).
- Sin imágenes externas; todo se dibuja con primitivas geométricas.

## Próximos pasos
- Añadir más tipos de enemigos y mapas.
- Sistema de inventario ampliado.
- Guardado completo del mapa.
- Modo historia.