from FloryCanbusMessage import FloryCanbusMessage

# PGN 65253


class EngineHoursRevolutions_65253(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["HourMeter"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16), int(self.data[1], 16), int(self.data[0], 16)], "big") * 0.05
        # self.dictionary["Engine Total Revolutions [r]"] = int.from_bytes([int(self.data[7], 16), int(self.data[6], 16), int(self.data[5], 16), int(self.data[4], 16)], "big") * 1000
