from enum import Enum


class Units(str, Enum):
    STANDARD = "standard"
    IMPERIAL = "imperial"
    METRIC = "metric"

    @staticmethod
    def get_symbol(units: "Units") -> str:
        return "C" if units == Units.METRIC else "F"
