import attr
from typing import List, Dict, Optional, Union
from pathlib import Path

import pandas as pd

from kpi_forecasting.inputs import YAML


PARENT_PATH = Path(__file__).parent
HOLIDAY_PATH = PARENT_PATH / "holidays.yaml"
REGRESSOR_PATH = PARENT_PATH / "regressors.yaml"

holiday_collection = YAML(HOLIDAY_PATH)
regressor_collection = YAML(REGRESSOR_PATH)


@attr.s(auto_attribs=True, frozen=False)
class ProphetRegressor:
    """
    Holds necessary data to define a regressor for a Prophet model.
    """

    name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    prior_scale: Union[int, float] = 1
    mode: str = "multiplicative"


@attr.s(auto_attribs=True, frozen=False)
class ProphetHoliday:
    """
    Holds necessary data to define a custom holiday for a Prophet model.
    """

    name: str
    ds: List
    lower_window: int
    upper_window: int
