class State :

    butters = [0 for i in range(10)]
    robot = None
    depthIDS = 0

    @classmethod
    def setRobot(cls ,newPosition):
        cls.robot = newPosition

    @classmethod
    def setButter(cls , which , newPosition):
        cls.butters[which] =newPosition 

    @classmethod
    def getRobot(cls):
        return cls.robot

    @classmethod
    def getButters(cls):
        return cls.butters

    @classmethod
    def setDepthIDS(cls , value):
        cls.depthIDS = value

    @classmethod
    def getDepthIDS(cls):
        return cls.depthIDS

