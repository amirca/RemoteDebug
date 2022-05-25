from FloryCanbusMessage import FloryCanbusMessage

# PGN 65226


class ActiveDiagnosticTroubleCodes_65226(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        pass
        # self.dictionary["Fuel Level"] = int(self.data[1], 16) * 0.3922
        # value = int(self.data[2], 16)
        # self.dictionary["Low Hydraulic Oil Warning [Yes/No]"] = (value >> 4) & 0x01
        #
        # value = int(self.data[4], 16)
        # self.dictionary["Fan [On/Off]"] = value & 0x01
        # self.dictionary["Elevator [On/Off]"] = (value >> 1) & 0x01
        # self.dictionary["Shafts [On/Off]"] = (value >> 5) & 0x01