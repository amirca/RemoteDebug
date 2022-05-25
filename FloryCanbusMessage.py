
class FloryCanbusMessage:

    def __init__(self, pgn, data):
        super().__init__()
        self.dictionary = {}
        self.pgn = pgn
        self.data = data
        self.dictionary["Pgn"] = pgn

    def get_dictionary(self):
        return self.dictionary

    @staticmethod
    def to_signed_byte(value):
        return (value & 0x7F) * -1 if value & 0x80 == 0x80 else value

    @staticmethod
    def to_signed_int(value):
        return (value & 0x7F) * -1 if value & 0x80 == 0x80 else value

