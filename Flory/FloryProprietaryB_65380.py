from Consts import FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID, FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_NAME, \
    FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID, FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_NAME
from FloryCanbusMessage import FloryCanbusMessage

# PGN 65380


class FloryProprietaryB_65380(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, mld_id=None):
        model_id = int(self.data[0], 16)
        self.dictionary["ModelId"] = model_id
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID:
            self.dictionary["ModelName"] = FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_NAME
        elif model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            self.dictionary["ModelName"] = FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_NAME

    @staticmethod
    def get_model_id(data):
        model_id = int(data[0], 16)
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID or \
           model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            return model_id
        return None

    @staticmethod
    def get_model_name(model_id):
        if model_id == FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_ID:
            return FLORY_VEHICLE_PRODUCT_LINE_34_SERIES_SWEEPER_NAME
        elif model_id == FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_ID:
            return FLORY_VEHICLE_PRODUCT_LINE_8770_HARVESTER_NAME
        return None

