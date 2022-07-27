from typing import (
    Callable,
    Optional,
)

from pandas.core.groupby.base import GroupByMixin as GroupByMixin

class WindowGroupByMixin(GroupByMixin):
    def __init__(self, obj, *args, **kwargs) -> None: ...

def calculate_center_offset(window): ...
def calculate_min_periods(
    window: int,
    min_periods: Optional[int],
    num_values: int,
    required_min_periods: int,
    floor: int,
) -> int: ...
def zsqrt(x): ...
def prep_binary(arg1, arg2): ...
def get_weighted_roll_func(cfunc: Callable) -> Callable: ...
