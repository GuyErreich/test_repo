from ...base_config import BaseConfig
import json

class DevConfig(BaseConfig):
	# def __init__(self, fname, lname):
    #     self.firstname = fname
    #     self.lastname = lname

    def __init__(self):
        BaseConfig.__init__(self)
        self.age = '15'
        self.color = 'blue'
		
    def convert_to_json(self):
        #convert to JSON string
        return json.dumps(self.__dict__)