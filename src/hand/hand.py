#crea una clase hand que contiene una lista de cartas
# un metodo para dibujar las cartas

from typing import List
from card.card import Card
import pygame

class Hand:
    cards: List[Card]
    screen: pygame.Surface
    def __init__(self, screen):
        self.cards = []
        self.screen = screen

    def add_card(self, card):
        self.cards.append(card)

    def draw(self):
        for i, card in enumerate(self.cards):
            card.sub_surface.get_rect().x = i * 100
            card.sub_surface.get_rect().y = 500
            self.screen.blit(card.draw(), card.sub_surface.get_rect())