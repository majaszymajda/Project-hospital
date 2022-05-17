
from uuid import UUID

import uuid

class Patient:
  def __init__(
    self,
    id = uuid.uuid4(),
    healthValue = 3,
    serviceTotalTime = 10,
    name = "Clone"):
        self.id = id
        self.healthValue = healthValue
        self.serviceTotalTime = serviceTotalTime
        self.name = name

