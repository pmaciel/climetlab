# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from climetlab.helpers import helper
from climetlab.core.ipython import display

# This is needed when running Sphinx on ReadTheDoc
try:
    from .drivers.magics import Driver

except Exception:
    from .drivers.missing import Driver



def plot_map(data, **kwargs):
    # This is a standalone plot, so we reset the driver
    driver = Driver(kwargs)

    if getattr(data, "plot_map", None) is None:
        data = helper(data)

    data.plot_map(driver)

    return display(driver.show())
