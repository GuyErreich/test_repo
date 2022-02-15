from ...base_config import BaseConfig
import json

class ProdConfig(BaseConfig):
	# def __init__(self, fname, lname):
    #     self.firstname = fname
    #     self.lastname = lname

    def __init__(self):
        BaseConfig.__init__(self)
        self.fav_food = 'sushi'
		
    def convert_to_json(self):
        #convert to JSON string
        return json.dumps(self.__dict__)