from FloryCanbusMessage import FloryCanbusMessage

# PGN 65260


class VehicleIdentification_65260(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["VehicleIdentificationNumber"] = int(self.data[0], 16)
