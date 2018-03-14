from app.models.lesson import Lesson

class Schedule:
  def __init__(self):
  	self.lessons = []
  	self.day = 0

  def to_json(self):
  	return {
  	  'lessons': self.lessons,
  	  'day': self.day
  	}