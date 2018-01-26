# Copyright (C) 2018  Nathan Sullivan

from . import Logger


__all__ = ['init', 'G']


G = None
log = None

class _Controller():
    def __init__(self):
        self.current_card = 0
        self.headers = None
        self.data = []

        self.card_ranges = {}

        self.cards_start = 0
        self.cards_end = 0

def init():
    global G, log
    if log is None:
        log = Logger.getChildLogger(__name__)

    log.debug("Initialising controller")

    if G is None:
        G = _Controller()

    return G
