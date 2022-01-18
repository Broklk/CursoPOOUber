from mimetypes import init


class Payment:
    id = int

    def __init__(self, id):
        self.id     = id