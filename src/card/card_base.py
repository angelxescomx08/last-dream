from abc import ABC, abstractmethod
from typing import List
from pygame import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND, Rect, Surface, mouse, draw
from src.game_object.live_character import LiveCharacter


class CardBase(ABC):

    # maximun range that a card can be dragged
    MAX_DRAG_RANGE = 100

    # global variable to store if a card is being dragged
    _dragging_card = None

    # global variable to store if a card is being hovered
    _hovering_card = None

    @property
    @abstractmethod
    def initial_position(self) -> tuple[int, int]:
        pass

    @property
    @abstractmethod
    def position(self) -> tuple[int, int]:
        pass

    @position.setter
    @abstractmethod
    def position(self, value: tuple[int, int]):
        pass

    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass

    @property
    @abstractmethod
    def is_hovered(self) -> bool:
        pass

    @is_hovered.setter
    @abstractmethod
    def is_hovered(self, value: bool):
        pass

    @property
    @abstractmethod
    def is_dragged(self) -> bool:
        pass

    @is_dragged.setter
    @abstractmethod
    def is_dragged(self, value: bool):
        pass

    @property
    @abstractmethod
    def player(self) -> LiveCharacter:
        pass

    @property
    @abstractmethod
    def enemies(self) -> List[LiveCharacter]:
        pass

    @property
    @abstractmethod
    def targeted_enemy(self) -> LiveCharacter:
        pass

    @abstractmethod
    def effect(
        self,
        player: LiveCharacter,
        enemies: List[LiveCharacter],
        targeted_enemy: LiveCharacter,
    ) -> None:
        pass

    def drag(self) -> None:
        # Verifica si ninguna carta está siendo arrastrada
        if CardBase._dragging_card is None:
            if mouse.get_pressed()[0] and self.rect.collidepoint(mouse.get_pos()):
                # Establece esta carta como la que se está arrastrando
                CardBase._dragging_card = self
                self.is_dragged = True

        if CardBase._dragging_card is self and self.is_dragged:
            center_pos = (
                mouse.get_pos()[0] - self.rect.width // 2,
                mouse.get_pos()[1] - self.rect.height // 2,
            )

            # Limita la posición de la carta dentro del rango máximo
            max_x = self.initial_position[0]
            max_y = min(
                max(center_pos[1], self.initial_position[1] - self.MAX_DRAG_RANGE),
                self.initial_position[1] + self.MAX_DRAG_RANGE,
            )
            self.position = (max_x, max_y)

            mouse.set_cursor(SYSTEM_CURSOR_HAND)

        if CardBase._dragging_card is self and not mouse.get_pressed()[0]:
            self.is_dragged = False
            # Libera la carta actual al soltar el botón del ratón
            CardBase._dragging_card = None

            # Verifica si la carta está dentro del rango máximo y ejecuta una acción si es así
            if (
                self.initial_position[0] - self.MAX_DRAG_RANGE
                <= self.position[0]
                <= self.initial_position[0] + self.MAX_DRAG_RANGE
                and self.initial_position[1] - self.MAX_DRAG_RANGE
                <= self.position[1]
                <= self.initial_position[1] + self.MAX_DRAG_RANGE
            ):
                self.effect(self.player, self.enemies, self.targeted_enemy)

            # Restaura la posición inicial si no se realiza ninguna acción
            self.position = self.initial_position

    def hover(self):
        mouse_pos = mouse.get_pos()
        # Verifica si alguna carta ya está en hover o si esta carta es la que está en hover
        if CardBase._hovering_card is None or CardBase._hovering_card is self:
            if self.rect.collidepoint(mouse_pos):
                if not self.is_hovered:
                    self.is_hovered = True
                    mouse.set_cursor(SYSTEM_CURSOR_HAND)
                    # Establece esta carta como la que está en hover
                    CardBase._hovering_card = self
            else:
                if self.is_hovered:
                    self.is_hovered = False
                    mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    # Libera la carta en hover
                    CardBase._hovering_card = None

    def draw(self, screen: Surface):
        self.hover()
        self.drag()

        color = (
            (200, 200, 200) if self.is_hovered or self.is_dragged else (255, 255, 255)
        )
        self.rect.topleft = self.position
        draw.rect(screen, color, self.rect)
