# PEP 673 – Self Type
from typing import Self


class Character:
    def __init__(self, name: str, level: 1):
        self.name = name
        self.level = level

    @classmethod
    def create(cls, name: str) -> Self:
        return cls(name, 1)


class Wizard(Character):
    def cast_spell(self, spell_name: str):
        print(f"{self.name} of level {self.level} casts {spell_name}!")


npc_cat = Character.create("Black Cat")
gandolf = Wizard.create("Gandolf")
