from FloryCanbusMessage import FloryCanbusMessage

# PGN 65411


class OmcShakerActivity_65411(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)
        self.load_dictionary()

    def load_dictionary(self):
        self.dictionary["shaker_active"] = int(self.data[6], 16)
