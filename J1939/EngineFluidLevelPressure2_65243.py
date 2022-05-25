from FloryCanbusMessage import FloryCanbusMessage

# PGN 65243


class EngineFluidLevelPressure2_65243(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["Engine Fuel Injection Control Pressure [MPa]"] = int.from_bytes([int(self.data[1], 16), int(self.data[0], 16)], "big") * 0.00390625
        self.dictionary["Engine Fuel 1 Injector Metering Rail 1 Pressure [MPa]"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * 0.00390625
        self.dictionary["Engine Fuel 1 Injector Timing Rail 1 Pressure [MPa]"] = int.from_bytes([int(self.data[5], 16), int(self.data[4], 16)], "big") * 0.00390625
        self.dictionary["Engine Fuel 1 Injector Metering Rail 2s Pressure [MPa]"] = int.from_bytes([int(self.data[7], 16), int(self.data[6], 16)], "big") * 0.00390625
