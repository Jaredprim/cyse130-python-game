# Interactive Text-Based Adventure Game (CYSE 130)

## Overview
This is a semester-long Python project for CYSE 130. It is an interactive text-based adventure game where the player makes choices that influence the story’s outcome. The game includes branching paths, inventory management, and simple combat and/or puzzle-solving mechanics.

## Gameplay Features
- **Branching story paths:** player decisions lead to different scenes and endings
- **Inventory system:** collect/use items to unlock choices or solve problems
- **Combat / puzzles:** simple mechanics that impact progress (ex: health, item checks, or puzzle answers)
- **Input validation:** handles invalid choices and keeps the game moving

## How It Works (High Level)
The game is structured as connected story “scenes.” Each scene prints narrative text, asks the player to choose an option, and then routes to the next scene based on their input. Inventory is tracked using variables (and/or lists) and checked to unlock certain actions. Combat/puzzles use simple rules (ex: health points, required items, or correct answers) to determine outcomes.

## How to Run
1. Download or clone this repository
2. Run the program:

```bash
python3 game.py
