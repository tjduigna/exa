# -*- coding: utf-8 -*-
# Copyright (c) 2015-2017, Exa Analytics Development Team
# Distributed under the terms of the Apache License 2.0
"""
The purpose of this package is to provide a framework for reading data from disk,
organizing this data into related, systematic, and efficient data structures, and
attaching these data structures to a container to allow visualization and other
interactive exploration within the `Jupyter notebook`_. The following is a compact
summary.

- editors: Classes that facilitate creation of data containers
- data: Classes that facilitate data visualization via the container
- containers: Flexible device for processing, analyzing and visualizing data

Complete documentation is available on the web https://exa-analytics.github.io/exa/.
The following is a brief description of the source code structure, which may aid
in usage.

- :mod:`~exa._version`: Version information
- :mod:`~exa.single`: Singleton metaclass
- :mod:`~exa.typed`: Strongly typed metaclass
- :mod:`~exa.mpl`: Matplotlib wrappers
- :mod:`~exa.tex`: Text manipulation utilities
- :mod:`~exa.units`: Physical units
- :mod:`~exa.constants`: Physical constants
- :mod:`~exa.isotopes`: Chemical isotopes

- :mod:`~exa.core.base`: Abstract base classes
- :mod:`~exa.core.editor`: Base editors
- :mod:`~exa.core.container`: Frame container
- :mod:`~exa.core.data`: Frame data

- :mod:`~exa.widgets.abcwidgets`: Abstract base widgets
- :mod:`~exa.widgets.threejs`: ThreeJS widgets

Warning:
    The ``_static`` directory in the source code contains static data. It does
    not contain Python or other source code files and is not importable. It is
    included as 'package_data'.

Note:
    Tests are always located in the ``tests`` directory of each package or
    sub-package.

.. _Jupyter notebook: https://jupyter.org/
"""
def _jupyter_nbextension_paths():
    """
    Automatically generated by the `cookiecutter`_.

    .. _cookiecutter: https://github.com/jupyter/widget-cookiecutter
    """
    return [{
        'section': "notebook",
        'src': "../build/widgets",
        'dest': "jupyter-exa",
        'require': "jupyter-exa/extension"
    }]


from ._version import __version__
from .core import Editor, Sections, Parser, DataSeries, Container
from . import constants, isotopes, mpl, tex, units
