from decimal import Decimal
from . import DiabloAPIConfig
from . import Item
from DiabloDjango.AppCode import helper
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
    def ArcaneResist(self):
        return int(self.Stats()['arcaneResist'])

    @property
    def Armor(self):
        return int(self.Stats()['armor'])

    @property
    def AttackSpeed(self):
        return round(Decimal(self.Stats()['attackSpeed']), 2)

    @property
    def BackImage(self):
        if (int(self['gender']) == 0):
            backImage = 'VitruvianMan.jpg'
        else:
            backImage = 'VitruvianWoman.jpg'
        return str(backImage)

    @property
    def CareerTableRow(self):
        return str(
            '<tr><td>' + str(self.Name) + '</td><td>' + str(self.DisplayLevel) +
            '</td><td>' + str(self.Class) + '</td><td>' + str(self.Gender) +
            '</td><td>' + str("{:,}".format(self.EliteKills)) + '</td><td>' +
            helper.GetUpdateTime(self.LastUpdated).strftime("%Y-%m-%d") +
            '</td></tr>')

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
        ClassName = models.DimensionClass.objects.get(externalclassname=classId)
        return ClassName.classname

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
        return models.DimensionGender.objects.get(genderid=genderId).gendername

    @property
    def GoldFind(self):
        return int(self.Stats()['goldFind'] * 100)

    @property
    def Healing(self):
        return int(self.Stats()['healing'])

    @property
    def HeroId(self):
        return self['id']

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
    def LifeOnHit(self):
        return int(self.Stats()['lifeOnHit'])

    @property
    def LifeSteal(self):
        return int(self.Stats()['lifeSteal'])

    @property
    def MagicFind(self):
        return int(self.Stats()['magicFind'] * 100)

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
    def Portrait(self):
        LevelType = 'level' if (self.Level < 70) else 'paragon-level'
        #Return the div for individual hero
        #Need to add a span to distinguish paragon from standard
        if (self['seasonal']):
            nameDisplay = str('<div class="name seasonal">' +
            '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-true">&nbsp;</div>')
        else:
            nameDisplay = str('<div class="name">' +
            '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-false">&nbsp;</div>')

        return str('<li class="heroMenuItem"><div class="hero clickable" value="' + str(self['id']) + '">' +
                    '<a href="/hero?battletag=' + DiabloAPIConfig.BATTLETAG + '&heroid=' + str(self.HeroId) + '" class="fill-div">' +
                    '<div class="face ' + self['class'] + '-' + self.Gender + '">&nbsp;</div>' + nameDisplay + '</a></div></li>')

    @property
    def Toughness(self):
        return int(self.Stats()['toughness'])