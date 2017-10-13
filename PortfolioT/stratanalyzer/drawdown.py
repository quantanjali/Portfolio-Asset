





class DrawDownHelper(object):
    def __init__(self):
        self.__highWatermark = None
        self.__lowWatermark = None
        self.__lastLow = None
        self.__highDateTime = None
        self.__lastDateTime = None
        
# Has-a relationship
class DrawDown():
    def __init__(self):
        super(DrawDown, self).__init__()
        self.__maxDD = 0
        self.__longestDDDuration = datetime.timedelta()
        self.__currDrawDown = DrawDownHelper()
        
