#!/usr/bin/env python3
"""
rpg_simulator.py — Entry point for RPG Simulator (Tkinter Edition).

Run directly with::

    python rpg_simulator.py

Controls:
  Menu         ↑ ↓ Enter
  Creation     Type name, Enter; then ← → Enter for class
  Exploration  WASD move, G save, Q quit
  Combat       1 Attack, 2 Ability, 3 Potion, 4 Flee
"""

import os
import sys

# Ensure src is on the path (if run directly)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.rpg.game import Game


def main() -> None:
    """Start the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()