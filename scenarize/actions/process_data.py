from modules.singleton import Singleton


class Action:
    def name(self):
        return "process_data"
    def run(self, params_definition, artifacts_definition):
        s = Singleton()
        params_with_data = s.interpret_params(params_definition)

        data = {}
        data['id']= params_with_data['data']['id']
        data['title']=  params_with_data['data']['title']
        data['brand']=  params_with_data['data']['brand']
        # data['data2']= response_json["title"]
        if artifacts_definition:
            variable_name, data_values = next(iter(artifacts_definition.items()))
            s.artifacts[variable_name]={}
            for data_value in data_values:
                s.artifacts[variable_name][data_value] = data[data_value]
