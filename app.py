import pygame
import sys
import numpy as np

# Configuración de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Números de Feigenbaum")

# Parámetros para calcular los números de Feigenbaum
x_min, x_max = 2.4, 4.0
y_min, y_max = 0.0, 1.0
max_iterations = 1000

# Función para calcular los números de Feigenbaum
def calculate_feigenbaum():
    feigenbaum_data = []
    r_values = np.linspace(x_min, x_max, WIDTH)
    for r in r_values:
        x = 0.5
        for _ in range(max_iterations):
            x = r * x * (1 - x)
            if _ > max_iterations // 2:
                feigenbaum_data.append((r, x))
    return feigenbaum_data

feigenbaum_points = calculate_feigenbaum()
feigenbaum_scale = (WIDTH / (x_max - x_min), HEIGHT / (y_max - y_min))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    for r, x in feigenbaum_points:
        # Escala los puntos al tamaño de la pantalla
        px, py = int((r - x_min) * feigenbaum_scale[0]), int((y_max - x) * feigenbaum_scale[1])
        pygame.draw.circle(screen, (255, 255, 255), (px, py), 1)

    pygame.display.flip()

pygame.quit()
sys.exit()
