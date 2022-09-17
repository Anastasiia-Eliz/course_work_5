from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import json


@dataclass
class Armor:
    """
    Класс брони, с характеристиками название, значение защиты (defence),
    затрачиваемое значение выносливости за раунд боя (stamina_per_turn)
    """
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    """
    Класс оружия, с характеристиками название, минимальный и максимальный урон оружия,
    затрачиваемое значение выносливости за раунд боя (stamina_per_hit)
    """
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        """
        генерация рандомного числа между минимальным и максимальным значениями
        """
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    """
    Класс содержит список с оружием и список с броней
    """
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:
    """
    Класс представляет собой интерфейс для взаимодействия с классом BaseUnit
    """
    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name: str) -> Optional[Weapon]:
        """
        принимает имя_оружия и возвращает класс Weapon
        """
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name: str) -> Optional[Armor]:
        """
        принимает имя_брони и возвращает класс Armor
        """
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        return None

    def get_weapons_names(self) -> List[str]:
        """
        возвращает список с названиями оружия
        """
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> List[str]:
        """
        возвращает список с названиями брони
        """
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        метод загружает json в переменную EquipmentData
        """
        with open("./data/equipment.json", encoding="utf-8") as equipment_file:
            data = json.load(equipment_file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)

            return equipment_schema().load(data)
