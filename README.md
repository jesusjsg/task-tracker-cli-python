# Task tracker CLI

A simple command-line interface for managing tasks. This app allows users to add, list, update and delete tasks.

## Features

- Add tasks: create new tasks with a description.
- List tasks: view all tasks or filter by status (done, unstarted, in-progress).
- Update tasks: change the description of existing tasks.
- Delete tasks: remove tasks by their ID.
- Mark tasks as done or in progress,

## Requirements

- Python3.
- Click library.
- Tabulate library.

## Commands

- List: python3 cli.py list [status]
- Add: python3 cli.py add "Task description"
- update: python3 cli.py update <id> --description "New description"
- delete: python3 cli.py delete <id>
- mark done: python3 cli.py mark_done <id>
- mark in progress: python3 cli.py mark_progress <id>

All libraries are in the requirements.txt, if you want to use the CLI run the command pip install -r requiremnts.txt
