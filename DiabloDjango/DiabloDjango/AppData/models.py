#"""
#Definition of models.
#"""

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
