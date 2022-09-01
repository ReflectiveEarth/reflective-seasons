import os
#import numpy as np
from warnings import warn
from google.cloud import storage


def check_environment(name):
    """Check the current conda environment and warn if other than expected."""
    if os.environ["CONDA_DEFAULT_ENV"] != name:
        warn(f"conda environment: {name} not activated."
              "Some dependencies may not be installed.")
