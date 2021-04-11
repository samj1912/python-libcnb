"""Python libcnb namespace."""

from importlib_metadata import PackageNotFoundError, version

__author__ = "Sambhav Kothari"
__email__ = "sambhavs.email@gmail.com"

# Used to automatically set version number from github actions
# as well as not break when being tested locally
try:
    __version__ = version(__package__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"


from libcnb._buildpack import (
    Buildpack,
    BuildpackGroupEntry,
    BuildpackInfo,
    BuildpackOrder,
    BuildpackStack,
    License,
)
from libcnb._detect import DetectContext, Detector, DetectResult, detect
from libcnb._layers import Environment, ExecD, Layer, Layers, Profile
from libcnb._output import (
    BOMEntry,
    BuildMetadata,
    Label,
    LaunchMetadata,
    Process,
    Slice,
    Store,
    UnmetPlanEntry,
)
from libcnb._plan import (
    BuildpackPlan,
    BuildpackPlanEntry,
    BuildPlan,
    BuildPlanProvide,
    BuildPlanRequire,
)
from libcnb._platform import Platform

__all__ = [
    "detect",
    "DetectContext",
    "DetectResult",
    "Detector",
    "BOMEntry",
    "BuildMetadata",
    "Buildpack",
    "BuildpackGroupEntry",
    "BuildpackInfo",
    "BuildpackOrder",
    "BuildpackPlan",
    "BuildpackPlanEntry",
    "BuildpackStack",
    "BuildPlan",
    "BuildPlanProvide",
    "BuildPlanRequire",
    "Environment",
    "ExecD",
    "Label",
    "LaunchMetadata",
    "Layer",
    "Layers",
    "License",
    "Platform",
    "Process",
    "Profile",
    "Slice",
    "Store",
    "UnmetPlanEntry",
]
