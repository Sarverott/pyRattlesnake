
TEMPLATE = lambda filler: f"""# https://apokryf.pl/rattlesnake

version: '3'

{fillers}

tasks:
  selfupdate:
    cmds:
      - uv run python ./scripts/templater.py
    dir: ..
  default:
    cmds:
      - task --list-all

"""
