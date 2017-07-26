import logging
import re

class Leaderboard(dict):
    def Row(self):
        return self['row']