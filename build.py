#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pyb"
default_task = "publish"


@init
def set_properties(project):
    pass
def initialize(project):
    project.depends_on('coverage')

    project.set_property('coverage_break_build', True)  # Break the build if coverage is below threshold
    project.set_property('coverage_branch_threshold_warn', 50)  # Minimum coverage threshold (50%)
    # Add other properties as needed