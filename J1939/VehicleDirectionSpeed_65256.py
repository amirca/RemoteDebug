from FloryCanbusMessage import FloryCanbusMessage

# PGN 65256


class VehicleDirectionSpeed_65256(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["Compass Bearing [deg]"] = int.from_bytes([int(self.data[1], 16), int(self.data[0], 16)], "big") * (1.0/128.0)
        self.dictionary["Navigation-Based Vehicle Speed [km]"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * (1.0/256.0)
        self.dictionary["Pitch [deg]"] = int.from_bytes([int(self.data[5], 16), int(self.data[4], 16)], "big") * (1.0/128.0)
        self.dictionary["Altitude [m]"] = int.from_bytes([int(self.data[7], 16), int(self.data[6], 16)], "big") * 0.125
