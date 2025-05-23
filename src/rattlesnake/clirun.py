import os
import json

import asyncio

import random
import time

from rich.live import Live
from rich.table import Table


from prompt_toolkit.input import create_input
from prompt_toolkit.keys import Keys

output = json.loads(os.popen("task -a -j").read())

options = [ option for option in output["tasks"] if option["name"]!="default" ]

location = output["location"]

#for option in output["tasks"]:
#    print(option["name"])

index = 0

def generate_table() -> Table:
    global options, index
    """Make a new table."""
    table = Table()
    table.add_column("TASK")
    table.add_column("DESCRIPTION")

    if not len(options):
        return table

    index = (len(options)+index) % len(options)

    for row in range(len(options)):

        #print(output)
        #value = random.random() * 100

        task = f"{options[row]["name"]}"
        desc = f"{options[row]["desc"]}"
        if index == row:
            task = f"[red]{task}[/red]"
            desc = f"[red]{desc}[/red]"
        table.add_row(
            task,
            desc
        )
    return table

#call_at_end = ""


choosen_call = ""


async def main(live) -> None:
    global choosen_call
    done = asyncio.Event()
    input = create_input()

    choosen_call = ""

    def livetab():
        if choosen_call == "":
            live.update(generate_table())

    if len(options):
        livetab()

    def keys_ready():
        global index, options, choosen_call
        
        if not len(options):
            choosen_call = "task"
            done.set()
            return None

        for key_press in input.read_keys():
            #print(key_press)
            #print(key_press.data)
            #print(key_press.data == '\x1b[B')

            if key_press.data == '\x1b[B':
                index += 1
                livetab()
            
            elif key_press.data == '\x1b[A':
                index -= 1
                livetab()
            
            elif key_press.data == "\r":
                #os.popen(f"task {output["tasks"][index]["name"]}")
                choosen_call = f"task {options[index]["name"]}"
                done.set()

            elif key_press.key == Keys.ControlC:
                done.set()

    if len(options):
        with input.raw_mode():
            with input.attach(keys_ready):
                await done.wait()
        choosen_call = f"task {options[index]["name"]}"
    else:
        choosen_call = "task"
        
if __name__ == "__main__":
    if len(options):
        with Live(generate_table(), refresh_per_second=4) as live:
            asyncio.run(main(live))
            #await main(live)
        os.system(f"task {options[index]["name"]}")
    else:
        os.system("task")
