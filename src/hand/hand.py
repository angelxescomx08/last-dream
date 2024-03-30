#crea una clase hand que contiene una lista de cartas
# un metodo para dibujar las cartas

class Hand:
    def __init__(self, screen, current_dir):
        self.cards = []
        self.screen = screen
        self.current_dir = current_dir

    def add_card(self, card):
        self.cards.append(card)

    def draw(self):
        for i, card in enumerate(self.cards):
            card.rect.x = i * 100
            card.rect.y = 500
            self.screen.blit(card.image, card.rect)