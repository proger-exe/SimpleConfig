
class SimpleConfig:
	def __init__(self):
		self.data = {}

	def parse(self, file: str) -> None:
		file = open(file, 'r')
		data = file.readlines()
		
		for i in data:
			
			index = i.split(':')

			self.data.update({index[0]: index[1].replace('\n', '').split("//")[0]})

		file.close()

	def get(self, what: str) -> str:

		return self.data[what]
