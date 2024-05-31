import os
import sys
from modules.singleton import Singleton
import yaml

action_path="actions/"
actions ={}

# load Actions
def load_action():
    sys.path.insert(0,action_path)
    for f in os.listdir(action_path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            mod = __import__(fname)
            actions[fname] = mod.Action()
    sys.path.pop(0)
    return actions

def run_action(acton_name, data,artifact_definitions):
    for action in actions.values():
        if action.name() == acton_name:
            result = action.run(data,artifact_definitions)




def execute_scenario(scenario_file):

    # load all available actions
    actions = load_action()
    # init th singleton
    s = Singleton()

    # load the scenario
    with open(scenario_file, 'r') as file:
        scenario = yaml.safe_load(file)

    # load the global variables
    for k, v in scenario['variables'].items():
        s.set_global_variables(k,v)

    # Process each actions    
    for action in scenario['actions']:
        # The first element is always the action name
        first_key = next(iter(action))
        action_name = first_key
        action.pop(first_key)

        print(f"-------------------- action : {action_name} ----------------------------")
        # load the params for the action
        data = {}
        artifact_definitions= None
        if action:
            params = action.get('params',None)
            if params:
                data = params
        s.debug_log(f"-------------------- data : {data}")

        # load the artifact definition
        artifact_definitions = action.get('artifact',None)

        # run the action
        run_action(action_name,data,artifact_definitions)

        s.debug_log(f"-------------------- artifacts -----------------------------")
        s.debug_log(f"{s.artifacts}")




if __name__ == "__main__":
    execute_scenario('scenario.yaml')
 