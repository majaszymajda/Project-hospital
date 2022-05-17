# from Doctor import Doctor
class Queue:

  def __init__(self, queue, limit = 1000): 
        self.queue = queue 
        self.limit = limit
  
  def addToQueue(self, patient):
    self.queue.append(patient)
  
  def takeFirstToDoctor(self, doctor) -> str:
    patie = self.queue[0]
    self.queue.pop(0)
    doctor.defineAsBusy(patie.serviceTotalTime)
    return patie