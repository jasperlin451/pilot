class Person:
	def __init__(self,jhed,firstname,lastname,email,subject,preference,availability):
		self.jhu=jhed
		self.name=firstname+' '+lastname
		self.mail=email
		self.avail=availability
		self.pref=preference
		self.taken=False
