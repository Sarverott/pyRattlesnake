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

#for option in output["tasks"]:
#    print(option["name"])

index = 0

def generate_table() -> Table:
    global output, index
    """Make a new table."""
    table = Table()
    table.add_column("TASK")
    table.add_column("DESCRIPTION")

    index = (len(output["tasks"])+index) % len(output["tasks"])

    for row in range(len(output["tasks"])):
        #print(output)
        #value = random.random() * 100
        task = f"{output["tasks"][row]["name"]}"
        desc = f"{output["tasks"][row]["desc"]}"
        if index == row:
            task = f"[red]{task}[/red]"
            desc = f"[red]{desc}[/red]"
        table.add_row(
            task,
            desc
        )
    return table

async def main(live) -> None:
    done = asyncio.Event()
    input = create_input()

    def livetab():
        live.update(generate_table())

    livetab()

    def keys_ready():
        global index, output
        
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
                print(output["tasks"][index])
                exit()

            elif key_press.key == Keys.ControlC:
                done.set()

    with input.raw_mode():
        with input.attach(keys_ready):
            await done.wait()
    
    #livetab()
        
if __name__ == "__main__":
    with Live(generate_table(), refresh_per_second=4) as live:
        asyncio.run(main(live))