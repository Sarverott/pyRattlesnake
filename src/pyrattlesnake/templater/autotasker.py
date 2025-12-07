import json
import yaml
import os
import pathlib
import re

def checkTaskfileContains(direntryItem):
        item_path=direntryItem.path
        item_contains = os.scandir(item_path)
        return "Taskfile.yml" in [subitem.name for subitem in item_contains if subitem.is_file()]

def templatename_to_targetname(templatename):
    return templatename[len("TEMPLATE_"):-len("_.json")]

def targetname_to_templatename(targetname):
    return f"TEMPLATE_{targetname}_.json"

def list_templates(template_location=os.getcwd()):
    regexp = r"^TEMPLATE_([\w\d\.]+)_\.json$" # can be tested here: https://regexr.com/
    test = re.compile(regexp)
    return { templatename_to_targetname(templatename): templatename for templatename in os.listdir(template_location) if test.match(templatename)}
    

def autoincludedScriptsTaskfiles(THIS):
    data = None
    
    with open(os.path.join(THIS["dirpath"],targetname_to_templatename("Taskfile.yml"))) as template:
        data = json.load(template)

    scripts_lib = os.scandir(os.path.join(THIS["scriptspath"]))
    #print("### DIRS")
    to_be_included = [scriptset.name for scriptset in scripts_lib if scriptset.is_dir() and checkTaskfileContains(scriptset)]

    data["includes"] = {}

    for scriptset in to_be_included:
        data["includes"][scriptset] = {
            "dir":os.path.join(".",scriptset),
            "taskfile":os.path.join(".",scriptset,"Taskfile.yml")
        }
    with open(os.path.join(THIS["scriptspath"], "Taskfile.yml"), "w") as louncher:
        yaml.dump(data, louncher, Dumper=yaml.Dumper)

#def appendTerminalComandsByAliasers()