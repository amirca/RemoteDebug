from FloryCanbusMessage import FloryCanbusMessage

# PGN 65270


class IntakeExhaustConditions1_65270(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["After Treatment 1 Diesel Particulate Filter Intake Pressure [kPa]"] = int(self.data[0], 16) * 0.5
