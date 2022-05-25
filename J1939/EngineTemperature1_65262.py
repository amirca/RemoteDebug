from FloryCanbusMessage import FloryCanbusMessage

# PGN 65262


class EngineTemperature1_65262(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["CoolantTemperature"] = int(self.data[0], 16)
        # self.dictionary["Engine Fuel 1 Temperature 1 [C deg]"] = int(self.data[1], 16)
        # self.dictionary["Engine Oil Temperature [C deg]"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * 0.03125
        # self.dictionary["Engine Turbocharger 1 Oil Temperature [C deg]"] = int.from_bytes([int(self.data[5], 16), int(self.data[4], 16)], "big") * 0.03125
        # self.dictionary["Engine Intercooler Temperature [C deg]"] = int(self.data[6], 16)
        # self.dictionary["Engine Charge Air Cooler Thermostat Opening [%]"] = int(self.data[7], 16) * 0.4
