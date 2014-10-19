from bson.objectid import ObjectId

class Listing(object):
	def __init__(self, title=None,
		desc=None, price=0.00,
		email=None, phone=None,cllink=None):
		self.title = title
		self.desc = desc
		self.price = price
		self.email = email
		self.phone = phone
		self.cllink = cllink
		self._id = str(ObjectId())

	def save(self,c):
		c.insert(self.__dict__)

	def __getitem__(self,k):
		return self.__dict__[k]
