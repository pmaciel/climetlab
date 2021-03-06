# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from climetlab.datasets import Dataset
from climetlab.sources import DataSource

from .core.caching import CACHE as cache
from .core.metadata import init_metadata
from .core.settings import SETTINGS as settings
from .datasets import load as load_dataset
from .plotting import new_plot
from .plotting import options as plotting_options
from .plotting import plot_map
from .sources import load as load_source

# from climetlab.core.ipython import ipython_active


# import logging

__version__ = "0.1.0"


# if ipython_active:
#     logging.


__all__ = [
    "load_source",
    "load_dataset",
    "plot_map",
    "new_plot",
    "settings",
    "cache",
    "Dataset",
    "DataSource",
    "plotting_options",
]

init_metadata()
