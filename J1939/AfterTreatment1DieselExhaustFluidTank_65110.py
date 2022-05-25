from FloryCanbusMessage import FloryCanbusMessage

# PGN 65110


class AfterTreatment1DieselExhaustFluidTank_65110(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["DieselExhaustFluidVolume"] = int(self.data[0], 16) * 0.4
        self.dictionary["DieselExhaustFluidTemperature"] = int(self.data[1], 16)
        self.dictionary["DieselExhaustFluidLevel"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * 0.1
