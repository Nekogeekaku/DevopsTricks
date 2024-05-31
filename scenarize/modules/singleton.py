
class Singleton:
    _instance = None
    global_variables = None  # Shared variable
    artifacts = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls.global_variables = {}
            cls.artifacts = {}
        return cls._instance


    def get_global_variables(self, key):
        """Retrieve a global_variables value by key."""
        return self.global_variables.get(key, None)
    def set_global_variables(self, key, value):
        """Set a global_variables value by key."""
        self.global_variables[key] = value

    def debug_log(self, data):
        if (self.get_global_variables("DEBUG_MODE") == True):
            print(data)

    def navigate_to_path(self,d, path):
        keys = path.split('.')
        for key in keys:
            d = d[key]
        return d
    def append_value_to_path(self,d, path, value):
        keys = path.split('.')
        base = d
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d=d.setdefault(keys[-1], [])
        d.append (value)

    def interpret_param(self,value):
        result =None
        if str(value).isnumeric() :
            result = value
        elif value[0] == '$':
            path = value[1:]
            result = self.navigate_to_path(self.artifacts,path)
        else:
            result = value
        return result
    def interpret_params(self, params_definition):
        params_with_data = {}
        for k, v in params_definition.items():
            self.debug_log(k,v)
            params_with_data[k] =  self.interpret_param(v)
        return params_with_data
