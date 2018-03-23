import pygame

from settings import Settings 
from ship import Ship#alle Einstellungen in der Klasse koennen
 #hier auch verwendet werden
import game_functions as gf

def run_game():
	#initialize pygame, settings and screen objects
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, 
	ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#make a ship
	ship = Ship(ai_settings, screen)
	
	#Start the main loop for the game
	
	while True:
		
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
			
run_game()
