import mongoengine as me


class StinkAppearances(me.Document):
    ep_number = me.IntField(required=True)
    isStinky = me.BooleanField(required=True)
    air_date = me.DateField(required=True)
    stink_start = me.IntField(default=0)  # Start time of stink sighting in seconds
    stink_end = me.IntField(default=0)  # End time of stink sighting in seconds
