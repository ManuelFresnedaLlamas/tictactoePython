
# Tic-Tac-Toe Game

Este proyecto implementa el juego de Tic-Tac-Toe utilizando Django.

## Requisitos

- Python 3.x
- Django

## Instalación

1. Clona el repositorio:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd tictactoe
    ```

2. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py migrate
    ```

4. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

## Uso

### Crear un nuevo juego

Para crear un nuevo juego, utiliza el siguiente comando:

```sh
curl -X POST http://127.0.0.1:8000/new/
```

Esto devolverá un JSON con el `game_id` del nuevo juego.

### Hacer un movimiento

Para hacer un movimiento, usa el siguiente comando, reemplazando `<game_id>` con el ID del juego y `position` con la posición (de 0 a 8) donde quieres hacer el movimiento:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"position": 0}' http://127.0.0.1:8000/move/<game_id>/
```

### Reglas del Juego

1. **Jugadores**: El juego es para dos jugadores, `X` y `O`, que se alternan en los turnos.
2. **Tablero**: El tablero es una cuadrícula de 3x3.
3. **Objetivo**: El objetivo es ser el primero en colocar tres de tus marcas en una fila (horizontal, vertical o diagonal).
4. **Movimientos**:
   - Los jugadores se alternan para colocar sus marcas (`X` o `O`) en una de las 9 posiciones disponibles.
   - Las posiciones están numeradas del 0 al 8, comenzando desde la esquina superior izquierda y avanzando de izquierda a derecha y de arriba a abajo:
     ```
     0 | 1 | 2
     ---------
     3 | 4 | 5
     ---------
     6 | 7 | 8
     ```
5. **Ganador**: El primer jugador que consiga alinear tres de sus marcas en una fila, columna o diagonal, gana el juego.
6. **Empate**: Si todas las posiciones están ocupadas y ningún jugador ha conseguido alinear tres marcas, el juego termina en empate.
7. **Validación**:
   - No se permiten movimientos en posiciones ya ocupadas.
   - No se permiten movimientos cuando el juego ha terminado.

## Tests

Para ejecutar los tests unitarios:

```sh
python manage.py test
```

## Contribución

Por favor, envía un PR o abre un issue para contribuir a este proyecto.

## Ejemplo Completo de Secuencia de Movimientos

1. Crear el juego:

    ```sh
    curl -X POST http://127.0.0.1:8000/new/
    ```

    Respuesta:

    ```json
    {
      "game_id": 1,
      "board": "         ",
      "current_player": "X"
    }
    ```

2. Primer movimiento por 'X' en la posición 0:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 0}' http://127.0.0.1:8000/move/1/
    ```

    Respuesta:

    ```json
    {
      "game_id": 1,
      "board": "X        ",
      "current_player": "O",
      "winner": null,
      "game_over": false
    }
    ```

3. Segundo movimiento por 'O' en la posición 1:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 1}' http://127.0.0.1:8000/move/1/
    ```

    Respuesta:

    ```json
    {
      "game_id": 1,
      "board": "XO       ",
      "current_player": "X",
      "winner": null,
      "game_over": false
    }
    ```

4. Tercer movimiento por 'X' en la posición 2:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 2}' http://127.0.0.1:8000/move/1/
    ```

    Respuesta:

    ```json
    {
      "game_id": 1,
      "board": "XOX      ",
      "current_player": "O",
      "winner": null,
      "game_over": false
    }
    ```

Continúa así hasta que se declare un ganador o se detecte un empate.
```

### Instrucciones de Uso

- **Crear un juego**: Utiliza el comando `curl -X POST http://127.0.0.1:8000/new/` para iniciar un nuevo juego.
- **Hacer un movimiento**: Usa el comando `curl -X POST -H "Content-Type: application/json" -d '{"position": POSITION}' http://127.0.0.1:8000/move/GAME_ID/` para hacer un movimiento. Reemplaza `POSITION` con la posición en el tablero y `GAME_ID` con el ID del juego.

Asegúrate de seguir estos pasos y comandos para jugar una partida completa y verificar el correcto funcionamiento del juego.

```


# Tic-Tac-Toe Game

This project implements the Tic-Tac-Toe game using Django.

## Requirements

- Python 3.x
- Django

## Installation

1. Clone the repository:

    ```sh
    git clone <REPOSITORY_URL>
    cd tictactoe
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Apply the database migrations:

    ```sh
    python manage.py migrate
    ```

4. Start the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

### Create a new game

To create a new game, use the following command:

```sh
curl -X POST http://127.0.0.1:8000/new/
```

This will return a JSON with the `game_id` of the new game.

### Make a move

To make a move, use the following command, replacing `<game_id>` with the game ID and `position` with the position (from 0 to 8) where you want to make the move:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"position": 0}' http://127.0.0.1:8000/move/<game_id>/
```

### Game Rules

1. **Players**: The game is for two players, `X` and `O`, who alternate turns.
2. **Board**: The board is a 3x3 grid.
3. **Objective**: The objective is to be the first to place three of your marks in a row (horizontal, vertical, or diagonal).
4. **Moves**:
   - Players take turns placing their marks (`X` or `O`) in one of the 9 available positions.
   - Positions are numbered from 0 to 8, starting from the top left corner and proceeding left to right and top to bottom:
     ```
     0 | 1 | 2
     ---------
     3 | 4 | 5
     ---------
     6 | 7 | 8
     ```
5. **Winner**: The first player to align three of their marks in a row, column, or diagonal wins the game.
6. **Draw**: If all positions are filled and no player has aligned three marks, the game ends in a draw.
7. **Validation**:
   - Moves in already occupied positions are not allowed.
   - Moves are not allowed once the game is over.

## Tests

To run the unit tests:

```sh
python manage.py test
```

## Contribution

Please send a PR or open an issue to contribute to this project.

## Complete Move Sequence Example

1. Create the game:

    ```sh
    curl -X POST http://127.0.0.1:8000/new/
    ```

    Response:

    ```json
    {
      "game_id": 1,
      "board": "         ",
      "current_player": "X"
    }
    ```

2. First move by 'X' in position 0:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 0}' http://127.0.0.1:8000/move/1/
    ```

    Response:

    ```json
    {
      "game_id": 1,
      "board": "X        ",
      "current_player": "O",
      "winner": null,
      "game_over": false
    }
    ```

3. Second move by 'O' in position 1:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 1}' http://127.0.0.1:8000/move/1/
    ```

    Response:

    ```json
    {
      "game_id": 1,
      "board": "XO       ",
      "current_player": "X",
      "winner": null,
      "game_over": false
    }
    ```

4. Third move by 'X' in position 2:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"position": 2}' http://127.0.0.1:8000/move/1/
    ```

    Response:

    ```json
    {
      "game_id": 1,
      "board": "XOX      ",
      "current_player": "O",
      "winner": null,
      "game_over": false
    }
    ```

Continue like this until a winner is declared or a draw is detected.

```
### Usage Instructions

- **Create a game**: Use the command `curl -X POST http://127.0.0.1:8000/new/` to start a new game.
- **Make a move**: Use the command `curl -X POST -H "Content-Type: application/json" -d '{"position": POSITION}' http://127.0.0.1:8000/move/GAME_ID/` to make a move. Replace `POSITION` with the position on the board and `GAME_ID` with the game ID.

Make sure to follow these steps and commands to play a complete game and verify the proper functioning of the game.
```