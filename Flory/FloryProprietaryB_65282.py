from Consts import FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65282


class FloryProprietaryB_65282(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["ElevatorChainSpeedSetPoint"] = int(self.data[1], 16)
            self.dictionary["WindboardPositionSetPoint"] = int(self.data[4], 16)
            self.dictionary["RotaryTrapSpeedSetPoint"] = int(self.data[5], 16)
            self.dictionary["MachineFaultCodesFmi"] = int(self.data[7], 16)
