from app.models.lesson import Lesson

class Schedule:
  def __init__(self):
  	self.lessons = []

  def to_json(self):
  	return {
  	  'lessons': self.lessons
  	}