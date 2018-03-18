class Group:
  def __init__(self):
  	self.id = 0
  	self.name = ''
  	self.faculty = ''


  def to_json(self):
  	return {
  	  'id': self.id,
  	  'name': self.name,
  	  'faculty': self.faculty
  	}