from datetime import datetime
import json
import decimal


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, decimal.Decimal):
            #return (str(o) for o in [o])
            return float(o)

        return json.JSONEncoder.default(self, o)

def GetUpdateTime(epochSeconds):
    # Convert SecondsFromEpoch to local datetime
    return datetime.fromtimestamp(epochSeconds)