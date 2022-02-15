import json

class BaseConfig:
	# def __init__(self, fname, lname):
    #     self.firstname = fname
    #     self.lastname = lname

    def __init__(self):
        self.firstname = "Shel"
        self.lastname = "Levin"
		
    def convert_to_json(self):
        #convert to JSON string
        return json.dumps(self.__dict__)