from enum import Enum


class Units(str, Enum):
    STANDARD = "standard"
    IMPERIAL = "imperial"
    METRIC = "metric"

    @staticmethod
    def get_symbol(units: "Units") -> str:
        match units:
            case units.METRIC:
                return "C"
            case units.IMPERIAL:
                return "F"
            case _:
                return "K"
