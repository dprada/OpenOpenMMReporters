"""
ProjectName
A short description of the project.
"""
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# Add imports here
from . import demo
from .molsysmt_TrajectoryDict import MolSysMTTrajectoryDictReporter
from .tqdm import TQDMReporter




