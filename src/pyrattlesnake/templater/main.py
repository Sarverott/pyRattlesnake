import sys
import pathlib
import git
import os
import argparse

import json
import yaml

from pyrattlesnake.templater import autotasker

def this(file_const):
    return {
        "selfprojectdir": str((pathlib.Path(file_const) / "..").resolve())
        "scriptspath": str((pathlib.Path(file_const) ).resolve(),
        "filepath": str((pathlib.Path(file_const) ).resolve()),
        "dirpath": str((pathlib.Path(file_const) / "..").resolve())
    }

THIS = generate_this(__file__)

