# HELPERS
from Patient import Patient
from Queue import Queue
import time
import random

class Helpers:
    def convertPatient(self, health):
        if health == 3:
            return Patient(healthValue=health, serviceTotalTime=self.defineTotalServiceTime(startRange=15, endRange=25))
        if health == 2:
            return Patient(healthValue=health, serviceTotalTime=self.defineTotalServiceTime(startRange=10, endRange=15))
        if health == 1:
            return Patient(healthValue=health, serviceTotalTime=self.defineTotalServiceTime(startRange=5, endRange=10))

    def isAnyoneInQueue(self, queue) -> bool:
        if len(queue) != 0: return True
        else: return False
    
    def isAnyoneInAnyQueue(self, queueColection) -> bool:
        for q in queueColection:
            if len(q.queue) != 0: return True
        return False
    
    def getQueueWithPeople(self, queueColection) -> Queue:
        # For now we are selecting the first one - the light one
        for q in queueColection:
            if len(q.queue) != 0: return q
    
    def defineWorkingHours(self) -> time:
        # Starting the whole process
        return time.time() + (60 * 60 * 8) / 100
        # use: + 60 * 60 * 2 when testing
        # use: + 60 * 60 * 8  on production
    
    def defineTotalServiceTime(self, startRange, endRange) -> int:
        return (self.__defineWalkingTime() + self.__defineServiceTime(startRange, endRange))
    
    def __defineServiceTime(self, startRange, endRange) -> int:
        return random.randint(startRange, endRange)
    
    def __defineWalkingTime(self) -> int:
        return random.randint(1, 5) 