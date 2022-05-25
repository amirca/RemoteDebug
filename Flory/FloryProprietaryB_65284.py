from Consts import FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65284


class FloryProprietaryB_65284(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["FrontSweepsSpeedSetPoint"] = int(self.data[7], 16)

