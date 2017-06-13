from . import DiabloAPIConfig


class Rune(dict):
    skillIconURL = DiabloAPIConfig.SKILL_ICON_URL
    toolTipURL = DiabloAPIConfig.TOOLTIP_URL

    @property
    def ToolTipURL(self):
        return self.toolTipURL.replace("<ITEM>", str(self['tooltipParams']))

    @property
    def Description(self):
        return self['description']

    @property
    def Level(self):
        return self['level']

    @property
    def Name(self):
        return self['name']

    @property
    def Order(self):
        return int(self['order'])

    @property
    def SimpleDescription(self):
        return self['simpleDescription']

    #Don't know what this is for
    @property
    def SkillCalcID(self):
        return self['skillCalcId']

    @property
    def Slug(self):
        return self['slug']

    @property
    def Type(self):
        return self['type']