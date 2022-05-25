from FloryCanbusMessage import FloryCanbusMessage

# PGN 65271

class VehicleElectricalPower1_65271(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["SLI Battery 1 Net Current [A]"] = int(self.data[0], 16) * 0.05
        self.dictionary["Alternator Current [A]"] = int(self.data[1], 16) * 0.05
        self.dictionary["Charging System Potential [V]"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * 0.05
        self.dictionary["Battery Potential / Power Input 1 [V]"] = int.from_bytes([int(self.data[5], 16), int(self.data[4], 16)], "big") * 0.05
        self.dictionary["Key Switch Battery Potential [V]"] = int.from_bytes([int(self.data[7], 16), int(self.data[6], 16)], "big") * 0.05

