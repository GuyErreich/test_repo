import json

class BaseConfig:
	# def __init__(self, fname, lname):
    #     self.firstname = fname
    #     self.lastname = lname

    def __init__(self):
        self.firstname = "guy"
        self.lastname = "erreich"
		
    def convert_to_json(self):
        #convert to JSON string
        return json.dumps(self.__dict__)