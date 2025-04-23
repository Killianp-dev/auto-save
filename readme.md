# Auto Save Project

This project enables automatic daily, weekly, and monthly backups, managing disk space by automatically deleting older backup directories.

## Features
- Automatic directory backup.
- Automatic backup rotation by deleting older backups.
- Advanced operation logging.

## Project Structure

### Main Scripts
- `auto_save_daily.py`: Performs a daily backup and deletes older daily backups.
- `auto_save_weekly.py`: Performs a weekly backup and deletes older weekly backups.
- `auto_save_monthly.py`: Performs a monthly backup and deletes older monthly backups.

### Utility Files
- `utils.py`: Main functions for backup and management of old directories, integrated with Loguru for logging.
- `tests.py`: Test suite using pytest to ensure proper functioning of backups.

### Other Files
- `requirements.txt`: List of Python dependencies required to run the project.
- `auto_save.log`: Automatically generated log file.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Killianp-dev/auto-save
cd <CLONED_DIRECTORY>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To manually run a backup:
```bash
python3 auto_save_daily.py
```

## Scheduling Automatic Tasks

### Cronjob (Linux)
Edit crontab using:
```bash
crontab -e
```
Add an entry for daily backup at 03:00 AM:
```bash
0 3 * * * /usr/bin/python3 /path/to/auto_save_daily.py
```

### Scheduled Task (Windows)
Use Windows Task Scheduler:
- Name: Auto Save Daily
- Trigger: Daily at 03:00 AM
- Action: Start a program
- Program: Path to `python.exe`
- Arguments: Path to `auto_save_daily.py`

## Testing
To run unit tests:
```bash
pytest
```

## Logging
Operations are logged with Loguru in the `auto_save.log` file, with automatic rotation to limit its size.

## License
This project is under the MIT License.


