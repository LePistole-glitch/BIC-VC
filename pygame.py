import pygame
import numpy as np
pygame.init()
# Tamaño de la ventana
WIDTH, HEIGHT = 500, 500
# Tamaño de cada celda
CELL_SIZE = 10
# Cantidad de celdas en cada fila y columna
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Inicializar la ventana de Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la vida")

# Crear una matriz de ceros para almacenar el estado actual de la simulación
current_state = np.zeros((ROWS, COLS))

# Función para actualizar el estado de la simulación en cada iteración
def update_state(state):
    # Copiar el estado actual para poder actualizar todas las celdas al mismo tiempo
    new_state = state.copy()

    # Iterar sobre todas las celdas y actualizar su estado
    for i in range(1, ROWS - 1):
        for j in range(1, COLS - 1):
            # Contar la cantidad de celdas vecinas que están vivas
            num_alive_neighbors = np.sum(state[i-1:i+2, j-1:j+2]) - state[i, j]

            # Aplicar las reglas del juego de la vida de Conway
            if state[i, j] == 1 and (num_alive_neighbors < 2 or num_alive_neighbors > 3):
                new_state[i, j] = 0
            elif state[i, j] == 0 and num_alive_neighbors == 3:
                new_state[i, j] = 1

    return new_state

# Función para dibujar el estado actual de la simulación en la ventana de Pygame
def draw_state(state):
    SCREEN.fill((0, 0, 0))
    for i in range(ROWS):
        for j in range(COLS):
            if state[i, j] == 1:
                pygame.draw.rect(SCREEN, (255, 255, 255), (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Función principal del juego
def main():
    # Configurar el reloj de Pygame
    clock = pygame.time.Clock()

    # Bucle principal del juego
    while True:
        # Actualizar el estado de la simulación
        current_state = update_state(current_state)

        # Dibujar el estado actual de la simulación en la ventana de Pygame
        draw_state(current_state)

        # Actualizar la ventana de Pygame
        pygame.display.flip()

        # Esperar un tiempo para que la simulación no se ejecute demasiado rápido
        clock.tick(10)

        # Detectar si se ha presionado la tecla ESC para salir del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
