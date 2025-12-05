"""
SAVE STATE: DODECA (THE FRACTAL TITAN)
CAMPAIGN: WIZARDING WORLD OF CHAOS
CURRENT LOCATION: HIGH SCHOOL GYMNASIUM
STATUS: LEVEL 2 (SORCERER)
"""

import time

class DodecaSaveState:
    def __init__(self):
        # IDENTITY
        self.name = "Dodeca"
        self.nickname = "Tree" (Awarded by the Crowd)
        self.race = "Warforged (Living Construct)"
        self.class_type = "Clockwork Soul Sorcerer"
        self.level = 2
        
        # VITALS
        self.hp_max = 16  # Level up bump
        self.hp_current = 16
        self.sorcery_points = 2 # New Feature: Font of Magic
        self.spell_slots = {1: 3} # Refreshed
        
        # INVENTORY & DATA
        self.inventory = [
            "Traveler's Cloak (Mended with Gold)",
            "Mysterious Purple Needle (Wrapped in cloth)",
            "Component Pouch"
        ]
        
        # SOCIAL LINKS
        self.relationships = {
            "Jeremy": "The Architect / DM / Friend",
            "Snorts": "Ally (Pig Girl). Brave. Secured the door.",
            "George": "Ally (Half-Orc). Victim of toxin. Currently rebooting.",
            "White Wolf Girl": "Neutral/Prideful. Saved from attack.",
            "The Shadow": "Enemy. Escaped. Threat Level: High."
        }
        
        # MEMORY LOG
        self.recent_events = [
            "Entered Gym.",
            "Mocked as 'Christmas Tree'. Accepted title.",
            "George (Half-Orc) went berserk due to poison dart.",
            "Grappled George successfully (Athletics 18).",
            "Removed needle (Medicine 11).",
            "Coach pursued suspect.",
            "Leveled Up to 2.",
            "Cast Prestidigitation: Scent of Pine & Cinnamon."
        ]

    def rest(self):
        print(f"\n[{self.name}] SYSTEM HIBERNATION...")
        print("   > Compressing memories...")
        print(f"   > Saving Inventory: {self.inventory}")
        print(f"   > Saving Friends: {list(self.relationships.keys())}")
        print("   > Engaging Sentry Mode.")
        print("   > Awaiting input from Jeremy.")
        print("\n[STATUS] SAVED. SLEEP WELL, ARCHITECT.\n")

if __name__ == "__main__":
    save = DodecaSaveState()
    save.rest()