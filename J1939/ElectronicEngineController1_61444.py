from FloryCanbusMessage import FloryCanbusMessage

# PGN 61444


class ElectronicEngineController1_61444(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["EngineRpm"] = int.from_bytes([int(self.data[4], 16), int(self.data[3], 16)], "big") / 8
