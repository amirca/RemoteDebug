from Consts import FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID, FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65281


class FloryProprietaryB65281(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID:
            self.dictionary["MachineFaultCodesSpn"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16), int(self.data[1], 16), int(self.data[0], 16)], "big")
            self.dictionary["MachineFaultCodesFmi"] = int(self.data[4], 16)
        elif model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["FanSpeed"] = int.from_bytes([int(self.data[1], 16), int(self.data[0], 16)], "big")
            self.dictionary["AirRestrictionIndicatorLevel"] = int(self.data[4], 16)
