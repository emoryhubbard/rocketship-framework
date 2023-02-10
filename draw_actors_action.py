from action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        basic_items = cast.get_actors("basic_items")
        basic_description = cast.get_first_actor("basic_description")
        portrait = cast.get_first_actor("portrait")
        player = cast.get_first_actor("players")
        legendary_items = cast.get_actors("legendary_items")
        self._output_service.clear_buffer()

        self._output_service.draw_player(player)
        for actor in basic_items:
            self._output_service.draw_basic_item(actor)
        for actor in legendary_items:
            self._output_service.draw_legendary_item(actor)
        self._output_service.draw_basic_description(basic_description)
        self._output_service.draw_portrait(portrait)
        
        self._output_service.flush_buffer()