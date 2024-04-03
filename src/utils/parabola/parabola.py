from typing import Tuple
import pygame

class Parabola:
    @staticmethod
    def draw_parabola(
        screen: pygame.Surface, 
        a: Tuple[int, int], 
        b: Tuple[int, int], 
        color: pygame.Color,
        width: int = 1
    ):
        # Coordenadas de los puntos a y b
        x1, y1 = a
        x2, y2 = b
        
        # Cálculo de los coeficientes de la ecuación cuadrática ax^2 + bx + c
        a_coef = (y2 - y1) / (((x2 - x1) ** 2) if x2 != x1 else 0.0001)
        b_coef = -2 * a_coef * x1
        c_coef = y1 - a_coef * (x1 ** 2)
        
        # Dibujar la parábola
        for x in range(min(x1, x2), max(x1, x2)):
            y = int(a_coef * (x ** 2) + b_coef * x + c_coef)
            pygame.draw.circle(screen, color, (x, y), 1, width)