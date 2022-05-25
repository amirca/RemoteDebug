from FloryCanbusMessage import FloryCanbusMessage

# PGN 65276


class DashDisplay1_65276(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["FuelLevel"] = int(self.data[1], 16) * 0.4
