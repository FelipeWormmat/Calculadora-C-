from typing import (
    List,
    Optional,
    Tuple,
    Union,
)

import numpy as np
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.extension import ExtensionIndex as ExtensionIndex

from pandas._libs.interval import (
    Interval as Interval,
    IntervalMixin as IntervalMixin,
)
from pandas._typing import (
    AnyArrayLike as AnyArrayLike,
    DtypeArg as DtypeArg,
)

from pandas.core.dtypes.generic import ABCSeries as ABCSeries

class SetopCheck:
    op_name = ...
    def __init__(self, op_name) -> None: ...
    def __call__(self, setop): ...

class IntervalIndex(IntervalMixin, ExtensionIndex):
    def __new__(
        cls,
        data,
        closed=...,
        dtype=...,
        copy: bool = ...,
        name=...,
        verify_integrity: bool = ...,
    ): ...
    @classmethod
    def from_breaks(
        cls, breaks, closed: str = ..., name=..., copy: bool = ..., dtype=...
    ): ...
    @classmethod
    def from_arrays(
        cls, left, right, closed: str = ..., name=..., copy: bool = ..., dtype=...
    ): ...
    @classmethod
    def from_tuples(
        cls, data, closed: str = ..., name=..., copy: bool = ..., dtype=...
    ): ...
    def __contains__(self, key) -> bool: ...
    def values(self): ...
    def __array_wrap__(self, result, context=...): ...
    def __reduce__(self): ...
    def astype(self, dtype: DtypeArg, copy: bool = ...) -> Index: ...
    @property
    def inferred_type(self) -> str: ...
    def memory_usage(self, deep: bool = ...) -> int: ...
    def is_monotonic(self) -> bool: ...
    def is_monotonic_increasing(self) -> bool: ...
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self): ...
    @property
    def is_overlapping(self): ...
    def get_loc(
        self, key, method: Optional[str] = ..., tolerance=...
    ) -> Union[int, slice, np.ndarray]: ...
    def get_indexer(
        self,
        targetArrayLike,
        method: Optional[str] = ...,
        limit: Optional[int] = ...,
        tolerance=...,
    ) -> np.ndarray: ...
    def get_indexer_non_unique(
        self, targetArrayLike
    ) -> Tuple[np.ndarray, np.ndarray]: ...
    def get_value(self, series: ABCSeries, key): ...
    def where(self, cond, other=...): ...
    def delete(self, loc): ...
    def insert(self, loc, item): ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def __getitem__(self, value): ...
    def argsort(self, *args, **kwargs): ...
    def equals(self, other) -> bool: ...
    @property
    def is_all_dates(self) -> bool: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def interval_range(
    start=..., end=..., periods=..., freq=..., name=..., closed: str = ...
): ...
