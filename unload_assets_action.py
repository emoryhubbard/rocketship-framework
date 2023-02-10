from action import Action
import os

class UnloadAssetsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        for file in os.listdir("images"):
            self._output_service.unload_image("images/" + file)

def main():
    for file in os.listdir("images"):
        print(file)

if __name__ == "__main__":
    main()