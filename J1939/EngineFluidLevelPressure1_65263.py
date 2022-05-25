from FloryCanbusMessage import FloryCanbusMessage

# PGN 65263


class EngineFluidLevelPressure1_65263(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["OilPressure"] = int(self.data[3], 16) * 4
