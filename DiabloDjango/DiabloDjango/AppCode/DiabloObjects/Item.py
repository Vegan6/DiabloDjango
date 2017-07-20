from . import DiabloAPIConfig


class Item(dict):
    iconURL = DiabloAPIConfig.ICON_URL
    toolTipURL = DiabloAPIConfig.TOOLTIP_URL

    @property
    def IconURL(self):
        return self.iconURL.replace("<ITEM>", str(self['icon']))

    @property
    def ToolTipURL(self):
        return self.toolTipURL.replace("<ITEM>", str(self['tooltipParams']))

    @property
    def DisplayColor(self):
        return self['displayColor']

    @property
    def Name(self):
        return self['name']

    @property
    def ID(self):
        return self['id']

    @property
    def SetItemsEquipped(self):
        return self['setItemsEquipped']