from Consts import FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65283


class FloryProprietaryB_65283(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["MachineFaultCodesSpn]"] = int.from_bytes([int(self.data[7], 16), int(self.data[6], 16), int(self.data[5], 16), int(self.data[4], 16)], "big")

