class Lesson:
  def __init__(self):
  	self.lessonNumber = 0
  	self.week = 0
  	self.day = 0
  	self.subgroup = ''
  	self.type = ''
  	self.name = ''
  	self.teacher = ''


  def to_json(self):
  	return {
      'lessonNumber': self.lessonNumber, 
      'week': self.week,
      'day': self.day,
      'subgroup': self.subgroup, 
      'type': self.type,
      'name': self.name,
      'teacher': self.teacher
    }