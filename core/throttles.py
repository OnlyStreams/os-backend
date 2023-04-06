from rest_framework.throttling import UserRateThrottle

"""
There are three throttling classes (listed from least to most restrictive):
1) low (enabled by default)
2) medium
3) high
In order to see their restrictions checkout `DEFAULT_THROTTLE_RATES` in *settings.py*.
"""


class LowBurstRateThrottle(UserRateThrottle):
    scope = "low_burst"


class LowSustainedRateThrottle(UserRateThrottle):
    scope = "low_sustained"


class MediumBurstRateThrottle(UserRateThrottle):
    scope = "medium_burst"


class MediumSustainedRateThrottle(UserRateThrottle):
    scope = "medium_sustained"


class HighBurstRateThrottle(UserRateThrottle):
    scope = "high_burst"


class HighSustainedRateThrottle(UserRateThrottle):
    scope = "high_sustained"


class ExtremeBurstRateThrottle(UserRateThrottle):
    scope = "extreme_burst"


class ExtremeSustainedRateThrottle(UserRateThrottle):
    scope = "extreme_sustained"
