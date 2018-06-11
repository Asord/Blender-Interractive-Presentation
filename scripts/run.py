from bge import logic, events
from Managers.SlidesManager import SlidesManager

gestSlide = SlidesManager()

keyboard = logic.keyboard

JUST_ACTIVATED = logic.KX_INPUT_JUST_ACTIVATED

if keyboard.events[events.SPACEKEY] == JUST_ACTIVATED:
        print(gestSlide.posActiveSlide)