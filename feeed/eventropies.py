import warnings

from .complexity.eventropies import Eventropies

warnings.filterwarnings("default", category=DeprecationWarning, module=__name__)
warnings.warn(
    "feeed.eventropies has moved to feeed.complexity.eventropies and will be removed in a future release",
    DeprecationWarning,
)
