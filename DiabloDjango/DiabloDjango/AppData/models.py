#"""
#Definition of models.
#"""
from django.db import models
from django_mysql.models import Bit1BooleanField


#from django.db import models
#from django.core.urlresolvers import reverse

##career = Diablo.career_profile(Diablo.US_SERVER, 'heretic', '1984')

## Create your models here.

##Diablo Profile class/table
#class Profile(models.Model):
#    #Slug = auto indexed key?
#    Slug = models.SlugField(unique = True, max_length = 255)
#    BattleTag = models.CharField(max_length = 255)
#    BattleTagHuman = models.CharField(max_length = 255)
#    ParagonLevel = models.IntegerField()
#    ParagonLevelHardcore = models.IntegerField()
#    ParagonLevelSeason = models.IntegerField()
#    ParagonLevelSeasonHardcore = models.IntegerField()
#    LastHeroPlayed = models.BigIntegerField()
#    LastUpdated = models.BigIntegerField()
#    #Kills Table
#    #Progression Table
#    #TimePlayed Table
#    #Fallen Heroes Table
#    #Artisan Tables
#    SeasonId = models.IntegerField()
#    HighestHardcoreLevel = models.IntegerField()
#    LastChecked = models.DateTimeField(auto_now_add = True)
#    #Heroes = List of heroes class

#    # How to order the 'Table'
#    class Meta:
#        ordering = ['-LastChecked']

#    # Display to humans?
#    def __unicode__(self):
#        return u'%s' % self.title

#    # Link specific Profile
#    def get_absolute_url(self):
#        return reverse('blog.views.post', args = [self.Slug])

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from __future__ import unicode_literals


class DimensionClass(models.Model):
    classid = models.AutoField(db_column='ClassID', primary_key=True)
    classname = models.CharField(db_column='ClassName', max_length=64)
    externalclassname = models.CharField(db_column='ExternalClassName', max_length=64)

    class Meta:
        managed = False
        db_table = 'Dimension_Class'


class DimensionConfig(models.Model):
    configid = models.SmallIntegerField(db_column='ConfigID', primary_key=True)
    configname = models.CharField(db_column='ConfigName', max_length=128)
    configvalue = models.CharField(db_column='ConfigValue', max_length=8192, blank=True, null=True)
    configdescription = models.CharField(db_column='ConfigDescription', max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dimension_Config'


class DimensionGender(models.Model):
    genderid = models.IntegerField(db_column='GenderID', primary_key=True)
    gendername = models.CharField(db_column='GenderName', max_length=64)

    class Meta:
        managed = False
        db_table = 'Dimension_Gender'


class DimensionLocale(models.Model):
    localeid = models.AutoField(db_column='LocaleID', primary_key=True)
    localename = models.CharField(db_column='LocaleName', max_length=128)
    localenameapi = models.CharField(db_column='LocaleNameAPI', max_length=128)
    serverurl = models.CharField(db_column='ServerURL', max_length=256)
    iconurl = models.CharField(db_column='IconURL', max_length=256, blank=True, null=True)
    tooltipurl = models.CharField(db_column='ToolTipURL', max_length=256, blank=True, null=True)
    skilliconurl = models.CharField(db_column='SkillIconURL', max_length=256, blank=True, null=True)
    classimageurl = models.CharField(db_column='ClassImageURL', max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dimension_Locale'


class DimensionUser(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)
    battletag = models.CharField(db_column='BattleTag', max_length=128)
    battletagdisplay = models.CharField(db_column='BattleTagDisplay', max_length=128)
    lastupdated = models.DateTimeField(db_column='LastUpdated')
    localeid = models.ForeignKey(DimensionLocale, models.DO_NOTHING, db_column='LocaleID')

    class Meta:
        managed = False
        db_table = 'Dimension_User'


class FactCareer(models.Model):
    careerid = models.IntegerField(db_column='CareerID', primary_key=True)
    userid = models.ForeignKey(DimensionUser, models.DO_NOTHING, db_column='UserID')
    seasonid = models.SmallIntegerField(db_column='SeasonID')
    paragonlevel = models.SmallIntegerField(db_column='ParagonLevel', blank=True, null=True)
    paragonlevelhardcore = models.SmallIntegerField(db_column='ParagonLevelHardcore', blank=True, null=True)
    paragonlevelseason = models.SmallIntegerField(db_column='ParagonLevelSeason', blank=True, null=True)
    paragonlevelseasonhardcore = models.SmallIntegerField(db_column='ParagonLevelSeasonHardcore', blank=True, null=True)
    guildname = models.CharField(db_column='GuildName', max_length=256, blank=True, null=True)
    lastheroplayed = models.CharField(db_column='LastHeroPlayed', max_length=128, blank=True, null=True)
    lastupdateddatetime = models.DateTimeField(db_column='LastUpdatedDateTime', blank=True, null=True)
    monsterkills = models.IntegerField(db_column='MonsterKills', blank=True, null=True)
    elitekills = models.IntegerField(db_column='EliteKills', blank=True, null=True)
    monsterkillshardcore = models.IntegerField(db_column='MonsterKillsHardcore', blank=True, null=True)
    highesthardcorelevel = models.SmallIntegerField(db_column='HighestHardcoreLevel', blank=True, null=True)
    progressionact1 = Bit1BooleanField(db_column='ProgressionAct1', blank=True, null=True)
    progressionact2 = Bit1BooleanField(db_column='ProgressionAct2', blank=True, null=True)
    progressionact3 = Bit1BooleanField(db_column='ProgressionAct3', blank=True, null=True)
    progressionact4 = Bit1BooleanField(db_column='ProgressionAct4', blank=True, null=True)
    progressionact5 = Bit1BooleanField(db_column='ProgressionAct5', blank=True, null=True)
    blacksmithlevel = models.IntegerField(db_column='BlackSmithLevel', blank=True, null=True)
    blacksmithhardcorelevel = models.IntegerField(db_column='BlackSmithHardcoreLevel', blank=True, null=True)
    blacksmithseasonlevel = models.IntegerField(db_column='BlackSmithSeasonLevel', blank=True, null=True)
    blacksmithseasonhardcorelevel = models.IntegerField(db_column='BlackSmithSeasonHardcoreLevel', blank=True, null=True)
    jewelerlevel = models.IntegerField(db_column='JewelerLevel', blank=True, null=True)
    jewelerhardcorelevel = models.IntegerField(db_column='JewelerHardcoreLevel', blank=True, null=True)
    jewelerseasonlevel = models.IntegerField(db_column='JewelerSeasonLevel', blank=True, null=True)
    jewelerseasonhardcorelevel = models.IntegerField(db_column='JewelerSeasonHardcoreLevel', blank=True, null=True)
    mysticlevel = models.IntegerField(db_column='MysticLevel', blank=True, null=True)
    mystichardcorelevel = models.IntegerField(db_column='MysticHardcoreLevel', blank=True, null=True)
    mysticseasonlevel = models.IntegerField(db_column='MysticSeasonLevel', blank=True, null=True)
    mysticseasonhardcorelevel = models.IntegerField(db_column='MysticSeasonHardcoreLevel', blank=True, null=True)
    updatedatetime = models.DateTimeField(db_column='UpdateDatetime', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Fact_Career'
        unique_together = (('userid', 'seasonid'),)

class FactHero(models.Model):
    heroid = models.AutoField(db_column='HeroID', primary_key=True)
    userid = models.ForeignKey(DimensionUser, models.DO_NOTHING, db_column='UserID')
    apiheroid = models.IntegerField(db_column='APIHeroID')
    name = models.CharField(db_column='Name', max_length=128)
    classid = models.ForeignKey(DimensionClass, models.DO_NOTHING, db_column='ClassID')
    genderid = models.ForeignKey(DimensionGender, models.DO_NOTHING, db_column='GenderID')
    level = models.SmallIntegerField(db_column='Level', blank=True, null=True)
    paragonlevel = models.SmallIntegerField(db_column='ParagonLevel', blank=True, null=True)
    monsterkills = models.IntegerField(db_column='MonsterKills', blank=True, null=True)
    elitekills = models.IntegerField(db_column='EliteKills', blank=True, null=True)
    hardcore = Bit1BooleanField(db_column='Hardcore', blank=True, null=True)
    seasonal = Bit1BooleanField(db_column='Seasonal', blank=True, null=True)
    seasoncreated = models.SmallIntegerField(db_column='SeasonCreated', blank=True, null=True)
    lastupdateddatetime = models.DateField(db_column='LastUpdatedDateTime', blank=True, null=True)
    progressionact1 = Bit1BooleanField(db_column='ProgressionAct1', blank=True, null=True)
    progressionact2 = Bit1BooleanField(db_column='ProgressionAct2', blank=True, null=True)
    progressionact3 = Bit1BooleanField(db_column='ProgressionAct3', blank=True, null=True)
    progressionact4 = Bit1BooleanField(db_column='ProgressionAct4', blank=True, null=True)
    progressionact5 = Bit1BooleanField(db_column='ProgressionAct5', blank=True, null=True)
    dead = Bit1BooleanField(db_column='Dead', blank=True, null=True)
    life = models.IntegerField(db_column='Life', blank=True, null=True)
    damage = models.FloatField(db_column='Damage', blank=True, null=True)
    toughness = models.IntegerField(db_column='Toughness', blank=True, null=True)
    healing = models.FloatField(db_column='Healing', blank=True, null=True)
    attackspeed = models.FloatField(db_column='AttackSpeed', blank=True, null=True)
    armor = models.IntegerField(db_column='Armor', blank=True, null=True)
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)
    dexterity = models.IntegerField(db_column='Dexterity', blank=True, null=True)
    vitality = models.IntegerField(db_column='Vitality', blank=True, null=True)
    intelligence = models.IntegerField(db_column='Intelligence', blank=True, null=True)
    physicalresist = models.IntegerField(db_column='PhysicalResist', blank=True, null=True)
    fireresist = models.IntegerField(db_column='FireResist', blank=True, null=True)
    coldresist = models.IntegerField(db_column='ColdResist', blank=True, null=True)
    lightningresist = models.IntegerField(db_column='LightningResist', blank=True, null=True)
    poisonresist = models.IntegerField(db_column='PoisonResist', blank=True, null=True)
    arcaneresist = models.IntegerField(db_column='ArcaneResist', blank=True, null=True)
    critdamage = models.FloatField(db_column='CritDamage', blank=True, null=True)
    blockchance = models.FloatField(db_column='BlockChance', blank=True, null=True)
    blockamountmin = models.IntegerField(db_column='BlockAmountMin', blank=True, null=True)
    blockamountmax = models.IntegerField(db_column='BlockAmountMax', blank=True, null=True)
    thorns = models.FloatField(db_column='Thorns', blank=True, null=True)
    lifesteal = models.FloatField(db_column='LifeSteal', blank=True, null=True)
    lifeperkill = models.FloatField(db_column='LifePerKill', blank=True, null=True)
    goldfind = models.FloatField(db_column='GoldFind', blank=True, null=True)
    magicfind = models.FloatField(db_column='MagicFind', blank=True, null=True)
    damageincrease = models.FloatField(db_column='DamageIncrease', blank=True, null=True)
    critchance = models.FloatField(db_column='CritChance', blank=True, null=True)
    damagereduction = models.FloatField(db_column='DamageReduction', blank=True, null=True)
    lifeonhit = models.FloatField(db_column='LifeOnHit', blank=True, null=True)
    primaryresource = models.IntegerField(db_column='PrimaryResource', blank=True, null=True)
    secondaryresource = models.IntegerField(db_column='SecondaryResource', blank=True, null=True)
    updatedatetime = models.DateTimeField(db_column='UpdateDatetime', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fact_Hero'
        unique_together = (('userid', 'apiheroid'),)

     


