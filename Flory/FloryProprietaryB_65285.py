from Consts import FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65285


class FloryProprietaryB_65285(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["WindboardPositionActual"] = int(self.data[0], 16)

