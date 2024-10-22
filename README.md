# Automated-Energy-Data-Backup-and-Reporting-System

This project automates the backup of energy data stored in an SQLite database and generates periodic reports. It uses Python, Docker, and GitLab CI/CD.

## Features
- Automated backups with `backup.py`
- Automated report generation with `report.py`
- CI/CD pipeline with GitLab to automate the process

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/energy-data-backup-system.git
   ```

2. Build the Docker container:
   ```
   docker build -t energy-backup-system .
   ```

3. Run the Docker container:
   ```
   docker run -d energy-backup-system
   ```

4. To manually run the backup:
   ```
   python scripts/backup.py
   ```

5. To generate the report:
   ```
   python scripts/report.py
   ```

## GitLab CI/CD
The CI/CD pipeline automates the backup and report generation process.
