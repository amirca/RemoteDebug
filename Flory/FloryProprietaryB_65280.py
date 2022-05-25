from Consts import FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID, FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65280


class FloryProprietaryB_65280(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID:
            self.dictionary["AirRestrictionIndicatorLevel"] = int(self.data[5], 16)
            value = int(self.data[0], 16)
            self.dictionary["Reel"] = value & 0x01
        elif model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["FuelLevel"] = int(self.data[1], 16) * 0.3922
            value = int(self.data[1], 16)
            self.dictionary["AirFilterPluggedWarning"] = value & 0x01
            value = int(self.data[2], 16)
            self.dictionary["LowHydraulicOilWarning"] = (value >> 4) & 0x01

            value = int(self.data[4], 16)
            self.dictionary["Fan"] = value & 0x01
            self.dictionary["Elevator"] = (value >> 1) & 0x01
            self.dictionary["Shafts"] = (value >> 5) & 0x01