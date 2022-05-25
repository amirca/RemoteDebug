from FloryCanbusMessage import FloryCanbusMessage

# 65216


class ServiceInformation_65216(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["Service Component Identification [ID]"] = int(self.data[0], 16)
        self.dictionary["Service Distance [Km]"] = int.from_bytes([int(self.data[2], 16), int(self.data[2], 16)], "big") * 5

