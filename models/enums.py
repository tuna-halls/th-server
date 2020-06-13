import enum

class HallState(enum.Enum):
    OPEN = "OP"
    CLOSED = "CL"


class HallSecurityMode(enum.Enum):
    ALLOW_ANY = "AA"
    ALLOW_ANY_WITH_PASSWORD = "AP"
    ALLOW_MEMBERS_ONLY = "AM"


class HallLogMode(enum.Enum):
    PLAIN = "PL"
    E2EE = "E2"
    SYMMETRIC = "SY"


class FeatureType(enum.Enum):
    LOBBY = "LB"
    CHAT = "CT"
    VIDEOCALL = "VC"
    LIVE_CODING = "LC"
    LIVE_REVIEW = "LR"


class Presence(enum.Enum):
	UKNOWN = "UK"
	CONNECTED = "CN"
	AWAY = "AW"
	DISCONNECTED = "DC"


class Role(enum.Enum):
	ADMIN = "AD"
	STANDARD = "ST"
	GUEST = "GT"
