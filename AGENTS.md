# AGENTS.md

This document provides guidelines and commands for agents working on this repository.

## Project Overview

This is a collection of console brain games built with Python 3.10+. The project uses Poetry for dependency management and flake8 for linting.

## Build/Lint/Test Commands

### Dependency Management (Poetry)
```bash
# Install dependencies
poetry install

# Build package
poetry build

# Run a specific command in poetry environment
poetry run <command>
```

### Linting
```bash
# Run flake8 linter on the brain_games package
poetry run flake8 brain_games

# Or use make
make lint
```

### Running Games
```bash
# Using Poetry
poetry run brain-games      # Welcome screen
poetry run brain-even      # Even number game
poetry run brain-calc      # Calculator game
poetry run brain-gcd       # GCD game
poetry run brain-prime     # Prime number game
poetry run brain-progression  # Arithmetic progression game

# Using Make
make brain-games
make brain-even
make brain-calc
make brain-gcd
make brain-prime
make brain-progression
```

### Publishing
```bash
# Dry-run publish
poetry publish --dry-run

# Install locally built package
python3 -m pip install --user dist/*.whl
```

## Code Style Guidelines

### General
- **Python version**: 3.10+ (uses match/case syntax)
- **Max line length**: 80 characters
- **Max complexity**: 6 (per flake8 configuration)
- **Encoding**: UTF-8

### Formatting
- Use 4 spaces for indentation
- Remove trailing whitespace
- Use blank lines sparingly to separate logical sections (2 blank lines between top-level definitions)
- Use single blank line between function definitions within a module

### Naming Conventions
- **Modules/Packages**: `snake_case` (e.g., `brain_games`, `brain_even`)
- **Functions/Variables**: `snake_case` (e.g., `get_gcd`, `is_even`)
- **Constants**: `SCREAMING_SNAKE_CASE` (e.g., `MAX_STEPS`, `GAME_RULE`)
- **Scripts/Entry points**: `snake_case` files (e.g., `brain_even.py`)
- **Class names** (if used): `PascalCase`

### Imports
- Group imports in order: standard library, third-party, local
- Use absolute imports for local modules (e.g., `from brain_games.cli import ...`)
- Sort imports with isort using multi-line output mode 3 with trailing comma
- `__init__.py` files can have F401 (unused imports) ignored

### Type Annotations
- No explicit type hints are currently used in this codebase
- Follow the existing pattern (untyped) unless adding new features

### Error Handling
- Simple return-based error handling (no exception raising for game logic)
- Wrong answers return early from the game loop (see `engine.py`)
- Print error messages directly to console

### Code Structure

Each game follows this pattern:

1. **Game Logic Module** (`brain_games/games/brain_*.py`):
   - Define `GAME_RULE` constant (description string)
   - Implement helper functions (e.g., `is_even()`, `get_gcd()`)
   - Implement `generate_*_game()` function that returns `(question, answer)` tuple

2. **Script Module** (`brain_games/scripts/brain_*.py`):
   - Entry point with `main()` function
   - Calls `run_game(GAME_RULE, generate_*_game)`
   - Uses `if __name__ == '__main__': main()` pattern

3. **Engine** (`brain_games/engine.py`):
   - `run_game(game_rule, game_parts)` - main game loop
   - Runs 3 rounds (MAX_STEPS = 3)
   - Handles user input via `prompt.string()`
   - Prints results and congratulates or encourages

### CLI Interaction
- Use `prompt.string()` for user input (from `prompt` library)
- Use `print()` for all output
- Keep welcome/greeting in `brain_games/cli.py`

### File Organization
```
brain_games/
├── __init__.py
├── cli.py              # Welcome/greeting functions
├── engine.py           # Main game loop engine
├── games/              # Game logic modules
│   ├── brain_even.py
│   ├── brain_calc.py
│   ├── brain_gcd.py
│   ├── brain_prime.py
│   └── brain_progression.py
└── scripts/            # Entry point scripts
    ├── brain_even.py
    ├── brain_calc.py
    ├── brain_gcd.py
    ├── brain_prime.py
    └── brain_progression.py
```

### Things to Avoid
- Do not add comments unless necessary (code should be self-documenting)
- Do not exceed max complexity of 6
- Do not exceed 80 character line length
- Do not use `print()` for debugging (remove before committing)
- Do not commit secrets or credentials
- Do not modify the hexlet-check workflow file
