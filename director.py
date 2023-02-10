class Director:

    def __init__(self, output_service):
        self._output_service = output_service

    def start_game(self, cast, script):
        self._output_service.open_window()
        self._execute_actions("loading", cast, script)
        
        while self._output_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        
        self._execute_actions("unloading", cast, script)
        self._output_service.close_window()

    def _execute_actions(self, group, cast, script):
        actions = script.get_actions(group)

        for action in actions:
            action.execute(cast)