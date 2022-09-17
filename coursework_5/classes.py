from dataclasses import dataclass
from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    """
    Класс юнита, с характеристиками макс.здоровья, макс.выносливости, навыком и multipliers
    на атаку, выносливость и броню класса
    """
    name: str
    max_health: float
    max_stamina: float
    attack_mltplr: float
    stamina_mltplr: float
    armor_mltplr: float
    skill: Skill


# Инициализируем экземпляры класса UnitClass и присваиваем им значения аттрибутов
WarriorClass = UnitClass(
    name="Воин",
    max_health=20.0,
    max_stamina=15.0,
    attack_mltplr=0.8,
    stamina_mltplr=0.9,
    armor_mltplr=1.2,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=10.0,
    max_stamina=25.0,
    attack_mltplr=1.5,
    stamina_mltplr=1.2,
    armor_mltplr=1.0,
    skill=HardShot()
)


unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
