import warnings

from .complexity.epa_based import Epa_based

warnings.filterwarnings("default", category=DeprecationWarning, module=__name__)
warnings.warn(
    "feeed.epa_based has moved to feeed.complexity.epa_based and will be removed in a future release",
    DeprecationWarning,
)
