# Contribuyendo a RPG Simulator

¡Gracias por tu interés en contribuir! Este proyecto sigue un flujo de trabajo ligero:

## Cómo contribuir
1. Haz un fork del repositorio.
2. Crea una rama: `git checkout -b feature/nombre-mejora`.
3. Añade pruebas unitarias si el cambio modifica la lógica.
4. Ejecuta `black src tests` y `flake8 src tests` para mantener el estilo.
5. Asegúrate de que todas las pruebas pasan: `pytest`.
6. Haz commit con mensajes claros.
7. Abre un Pull Request describiendo los cambios.

## Estilo de código
- Seguimos PEP 8 con las reglas definidas en `pyproject.toml`.
- Usa docstrings en todas las funciones públicas (formato Google).
- Nombres de funciones y módulos en inglés, UI del juego en español.

## Reporte de problemas
Si encuentras un bug, abre un Issue con:
- Descripción detallada
- Pasos para reproducirlo
- Versión de Python y sistema operativo