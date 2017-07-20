from . import DiabloAPIConfig


class Skill(dict):
    skillIconURL = DiabloAPIConfig.SKILL_ICON_URL
    toolTipURL = DiabloAPIConfig.TOOLTIP_URL

    @property
    def ToolTipURL(self):
        return self.toolTipURL.replace("<ITEM>", str(self['tooltipUrl']))

    @property
    def Description(self):
        return self['description']

    @property
    def IconURL(self):
        return self.skillIconURL.replace("<SKILL>", str(self['icon']))

    @property
    def Level(self):
        return self['level']

    @property
    def Name(self):
        return self['name']

    @property
    def Flavor(self):
        return self['flavor']

    #Don't know what this is for
    @property
    def SkillCalcID(self):
        return self['skillCalcId']

    @property
    def Slug(self):
        return self['slug']