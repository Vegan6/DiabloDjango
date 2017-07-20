from datetime import datetime


def GetUpdateTime(epochSeconds):
    # Convert SecondsFromEpoch to local datetime
    return datetime.fromtimestamp(epochSeconds)