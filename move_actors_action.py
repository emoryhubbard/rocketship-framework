from action import Action

class MoveActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        actors = cast.get_all_actors()
        #do updates is essential for output service's time keeping
        self._output_service.do_updates()
        delta_time = self._output_service.get_delta_time()

        for actor in actors:
            actor.move_next(delta_time)