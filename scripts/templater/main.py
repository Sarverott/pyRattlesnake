import sys
import pathlib
import git
import os
import argparse

import json
import yaml

from templater import autotasker

def generate_this(file_const):
    return {
        "scriptspath": os.getcwd(),
        "filepath": str((pathlib.Path(file_const) ).resolve()),
        "dirpath": str((pathlib.Path(file_const) / "..").resolve())
    }

THIS = generate_this(__file__)

