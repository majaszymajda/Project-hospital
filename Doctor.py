import threading

class Doctor:
  isAvailable = True
  patientCount = 0

  def __init__(self, isAvailable = True, patientCount = 0):  
        self.isAvailable = isAvailable
        self.patientCount = patientCount

  def isFreeToTakeNewPatient(self) -> bool:
    if self.isAvailable:
      return True
    else:
      return False

  def defineAsBusy(self, timeAmount):
    self.isAvailable = False
    self.patientCount += 1
    x = threading.Timer(self.__getBlockingTime(timeAmount), self.__free)
    x.start()

  # Private methods
  def __free(self):
    self.isAvailable = True

  def __getBlockingTime(self, time) -> float:
    return time