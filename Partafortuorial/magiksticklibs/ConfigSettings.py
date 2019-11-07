from .Scrollbar import Scrollbar
from .LineNumber import LineMain
from .StationaryFunc import StationaryFunction
# import .Scrollbar

class Connect:
    def __init__(self, pad):
        self.pad = pad
        self.modules_connections()

    def modules_connections(self):
        LineMain(self.pad)
        Scrollbar(self.pad)
        StationaryFunction(self.pad)

        return
