
import os
import shutil
from datetime import datetime

def backup_database():
    backup_dir = 'data/backups'
    os.makedirs(backup_dir, exist_ok=True)
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    source = 'data/energy_data.db'
    destination = f'{backup_dir}/energy_data_backup_{current_time}.db'
    
    shutil.copy(source, destination)
    print(f"Backup created at {destination}")

if __name__ == "__main__":
    backup_database()
