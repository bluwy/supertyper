# Manages all events from pygame, technically an event is an input :)

import pygame


def handle_quit(all_events):
    """If pygame quiting, terminate self. Returns true if quit"""
    for event in all_events:
        if event.type == pygame.QUIT:
            return True

    return False


def handle_event_group_sprites(all_events, event_group):
    """Let event group sprites handle events"""
    for event in all_events:
        for sprite in event_group.sprites():
            sprite.handle_event(event)


def get_keydown_unicodes(all_events):
    """Get all keydown unicodes"""
    unicodes = []

    for event in all_events:
        if event.type == pygame.KEYDOWN:
            unicodes.append(event.unicode)

    return unicodes


def is_keydown_start_game(all_events):
    """Key down enter or space (For start game)"""
    for event in all_events:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
            return True

    return False
