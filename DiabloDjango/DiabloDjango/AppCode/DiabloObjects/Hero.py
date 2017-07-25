from decimal import Decimal
from . import Item
from DiabloDjango.AppData import models


class Hero(dict):
    # Create Hero Object
    def ActiveSkillsDictionary(self):
        skills = self['skills']
        return skills['active']

    def PassiveSkillsDictionary(self):
        skills = self['skills']
        return skills['passive']

    def Stats(self):
        return self['stats']

    def Items(self):
        return self['items']

    # Create Item Properties
    @property
    def Bracers(self):
        return Item.Item(self.Items()['bracers'])

    @property
    def Chest(self):
        return Item.Item(self.Items()['torso'])

    @property
    def Feet(self):
        return Item.Item(self.Items()['feet'])

    @property
    def Hands(self):
        return Item.Item(self.Items()['hands'])

    @property
    def Head(self):
        return Item.Item(self.Items()['head'])

    @property
    def LeftFinger(self):
        return Item.Item(self.Items()['leftFinger'])

    @property
    def Legs(self):
        return Item.Item(self.Items()['legs'])

    @property
    def MainHand(self):
        return Item.Item(self.Items()['mainHand'])

    @property
    def Neck(self):
        return Item.Item(self.Items()['neck'])

    @property
    def OffHand(self):
        return Item.Item(self.Items()['offHand'])

    @property
    def RightFinger(self):
        return Item.Item(self.Items()['rightFinger'])

    @property
    def Shoulder(self):
        return Item.Item(self.Items()['shoulders'])

    @property
    def Waist(self):
        return Item.Item(self.Items()['waist'])

    # Create Hero Properties
    @property
    def statList(self):
        return self.Stats()
    
    @property
    def Act1Completed(self):
        progression = self['progression']
        act1 = progression['act1']
        return act1['completed']

    @property
    def Act2Completed(self):
        progression = self['progression']
        act2 = progression['act2']
        return act2['completed']

    @property
    def Act3Completed(self):
        progression = self['progression']
        act3 = progression['act3']
        return act3['completed']

    @property
    def Act4Completed(self):
        progression = self['progression']
        act4 = progression['act4']
        return act4['completed']

    @property
    def Act5Completed(self):
        progression = self['progression']
        act5 = progression['act5']
        return act5['completed']

    @property
    def ArcaneResist(self):
        return int(self.Stats()['arcaneResist'])

    @property
    def Armor(self):
        return int(self.Stats()['armor'])

    @property
    def AttackSpeed(self):
        return round(Decimal(self.Stats()['attackSpeed']), 2)
    
    @property
    def BlockChance(self):
        return self.Stats()['blockChance']
    
    @property
    def BlockAmountMin(self):
        return self.Stats()['blockAmountMin']
    
    @property
    def BlockAmountMax(self):
        return self.Stats()['blockAmountMax']

    @property
    def ColdResist(self):
        return int(self.Stats()['coldResist'])

    @property
    def CriticalDamage(self):
        return int(self.Stats()['critDamage'] * 100)

    @property
    def CriticalChance(self):
        return int(self.Stats()['critChance'] * 100)

    @property
    def Class(self):
        classId = str(self['class'])
        #return DiabloAPIConfig.classes[classId]
        Class = models.DimensionClass.objects.get(externalclassname=classId)
        return Class

    @property
    def Damage(self):
        return int(self.Stats()['damage'])

    @property
    def DamageIncrease(self):
        return int(self.Stats()['damageIncrease'] * 100)

    @property
    def DamageReduction(self):
        return int(self.Stats()['damageReduction'] * 100)
    
    @property
    def Dead(self):
        return self['dead']
    
    @property
    def Dexterity(self):
        return int(self.Stats()['dexterity'])

    @property
    def DisplayLevel(self):
        if (self.Level < 70):
            return self.Level
        else:
            return "{:,}".format(self.ParagonLevel)

    @property
    def EliteKills(self):
        kills = self['kills']
        return kills['elites']

    @property
    def FireResist(self):
        return int(self.Stats()['fireResist'])

    @property
    def Gender(self):
        genderId = int(self['gender'])
        #return DiabloAPIConfig.genders[genderId]
        return models.DimensionGender.objects.get(genderid=genderId)

    @property
    def GoldFind(self):
        return int(self.Stats()['goldFind'] * 100)
    
    @property
    def Hardcore(self):
        return self['hardcore']

    @property
    def Healing(self):
        return int(self.Stats()['healing'])

    @property
    def HeroId(self):
        return self['id']
    
    @property
    def Intelligence(self):
        return int(self.Stats()['intelligence'])

    @property
    def LastUpdated(self):
        return int(self['last-updated'])

    @property
    def Level(self):
        return int(self['level'])

    @property
    def Life(self):
        return int(self.Stats()['life'])
    
    @property
    def LifePerKill(self):
        return int(self.Stats()['lifePerKill'])

    @property
    def LifeOnHit(self):
        return int(self.Stats()['lifeOnHit'])

    @property
    def LifeSteal(self):
        return int(self.Stats()['lifeSteal'])
    
    @property
    def LightningResist(self):
        return int(self.Stats()['lightningResist'])

    @property
    def MagicFind(self):
        return int(self.Stats()['magicFind'] * 100)
    
    @property
    def MonsterKills(self):
        kills = self['kills']
        #monsterKills = kills['monsters'] 
        return 0

    @property
    def Name(self):
        return self['name']

    @property
    def ParagonLevel(self):
        return self['paragonLevel']

    @property
    def PhysicalResist(self):
        return int(self.Stats()['physicalResist'])

    @property
    def PoisonResist(self):
        return int(self.Stats()['poisonResist'])

    @property
    def PrimaryResource(self):
        return self.Stats()['primaryResource']
    
    @property
    def Seasonal(self):
        return self['seasonal']
    
    @property
    def SeasonCreated(self):
        return self['seasonCreated']
    
    @property
    def SecondaryResource(self):
        return self.Stats()['secondaryResource']
    
    @property
    def Strength(self):
        return int(self.Stats()['strength'])
    
    @property
    def Thorns(self):
        return self.Stats()['thorns']
    
    @property
    def Toughness(self):
        return int(self.Stats()['toughness'])
    
    @property
    def Vitality(self):
        return int(self.Stats()['vitality'])