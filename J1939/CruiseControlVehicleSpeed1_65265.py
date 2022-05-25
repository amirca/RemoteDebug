from FloryCanbusMessage import FloryCanbusMessage

# PGN 65265


class CruiseControlVehicleSpeed1_65265(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["GroundSpeed"] = int.from_bytes([int(self.data[2], 16), int(self.data[1], 16)], "big") * (1.0/256.0)
