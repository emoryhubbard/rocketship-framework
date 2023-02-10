from object_found import object_found
class objects_counter(object_found):

    def __init__(self, object):
        super().__init__()
        self._object = object


    def found_object(self):
        # maybe this needs to be in here? I'm not sure. Feel free to delete this comment when resolved
        pass

    def object_count(self, object):
        # I'm not sure what to write here, but I know I want this function to count each object as it is found by the user
        pass