import json
from modules.singleton import Singleton


class Action:
    def name(self):
        return "save_data_to_file"
    def run(self, params_definition, artifacts_definition):
        s = Singleton()
        params_with_data = s.interpret_params(params_definition)

        with open(params_with_data['file_name'], 'w') as f:
                json.dump(params_with_data['data'], f)

