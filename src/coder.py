class TargetCoder:
    
    _POSITIONS_MAPPER = {
        "ST": "ST", "CF": "ST",
        "LW": "LW", "LF": "LW", "LM": "LW",
        "RW": "RW", "RM": "RW", "RF": "RW",
        "CM": "CM", "CAM": "CM", "CDM": "CM",
        "RB": "RB", "RWB": "RB",
        "LB": "LB", "LWB": "LB",
        "CB": "CB"
    }

    _TARGET_ENCODER = {
        "ST": 0, "LW": 1, "RW": 2,
        "CM": 3, "RB": 4, "LB": 5, "CB": 6
    }
    
    _TARGET_DECODER = {
        0: "ST", 1: "LW", 2: "RW",
        3: "CM", 4: "RB", 5: "LB", 6: "CB"
    }
    
    @staticmethod
    def encode(target: str) -> int:
        return TargetCoder._TARGET_ENCODER[TargetCoder.map(target)]
    
    @staticmethod
    def decode(target: int) -> str:
        return TargetCoder._TARGET_DECODER[target]
    
    @staticmethod
    def map(target: str) -> str:
        return TargetCoder._POSITIONS_MAPPER[target]