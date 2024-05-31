import requests
from modules.singleton import Singleton


class Action:
    def name(self):
        return "fetch_data"
    def run(self, params_definition, artifacts_definition):
        s = Singleton()

        params_with_data = s.interpret_params(params_definition)
        api_url = self.username=s.get_global_variables('API_URL')

        api_call = params_with_data["api_call"]

        response = requests.get(f"{api_url}{api_call}" )
        s.debug_log(response.json())
        response_json = response.json()
        data = {}
        data['data']= response_json
        if artifacts_definition:
            variable_name, data_values = next(iter(artifacts_definition.items()))
            s.artifacts[variable_name]={}
            for data_value in data_values:
                s.artifacts[variable_name][data_value] = data[data_value]
