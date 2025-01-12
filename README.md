# Task Tracker CLI

A simple command-line task management application built with Python and Click.

## Features

- Create, read, update, and delete tasks
- Filter tasks by status
- Track creation and update timestamps
- Simple JSON-based storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheTruthIsAlwaysComingBack/task_traker.git
cd task_traker
```

2. Install dependencies:
```bash
pip install click
```

## Usage

### List Tasks

Show all tasks:
```bash
python tasktraker.py list
```

Filter tasks by status:
```bash
python tasktraker.py list todo
python tasktraker.py list in-progress
python tasktraker.py list done
```

### Manage Tasks

Add a new task:
```bash
python tasktraker.py add "buy some groceries"
```

Update task status:
```bash
python tasktraker.py update 1 "buy some groceries and practice programming languages"
```

Delete a task:
```bash
python tasktraker.py delete 3
```

## Task Statuses

- `todo` - Task is pending
- `in-progress` - Task is currently being worked on
- `done` - Task is completed

## File Structure

Tasks are stored in a JSON file with the following structure:
```json
{
    "id": 1,
    "description": "Task description",
    "status": "todo",
    "createdAt": "2024-01-12-15",
    "updatedAt": "2024-01-12-15"
}
```

## Contributing

Feel free to submit issues and pull requests.

## Project URL

https://roadmap.sh/projects/task-tracker

## License

This project is open source and available under the [MIT License](LICENSE).