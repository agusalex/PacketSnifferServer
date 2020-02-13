from abc import ABC


class Listener(ABC):

    def get_percent_complete(self):
        pass

    def start(self):
        pass

    def is_alive(self):
        pass

    def stop(self):
        pass

    def run(self):
        pass