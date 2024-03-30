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
            card = card.draw()
            card.get_rect().x = i * 300
            card.get_rect().y = i * 500
            self.screen.blit(card, card.get_rect())