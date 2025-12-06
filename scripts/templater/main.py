import sys
import pathlib
import git
import os
import argparse

from templater import templates

def makeTaskfile():
    return templates.Taskfile