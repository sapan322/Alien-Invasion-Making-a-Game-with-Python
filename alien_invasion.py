import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Set the background color
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
