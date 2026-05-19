"""
Модуль работы с файлами для Todo List Manager
Разработчик: Dev 2
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime
import shutil


class TaskStorage:
    """Класс для работы с файловым хранилищем задач"""
    
    def __init__(self, filename: str = "tasks.json", backup_dir: str = "backups"):
        self.filename = filename
        self.backup_dir = backup_dir
        
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
    
    def load_tasks(self) -> List[Dict[str, Any]]:
        """Загружает задачи из JSON файла"""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                return tasks if isinstance(tasks, list) else []
        except (json.JSONDecodeError, IOError):
            return self._recover_from_backup()
    
    def save_tasks(self, tasks: List[Dict[str, Any]]) -> bool:
        """Сохраняет задачи в JSON файл с созданием бэкапа"""
        try:
            self._create_backup()
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2, default=str)
            return True
        except IOError:
            return False
    
    def _create_backup(self):
        """Создает бэкап текущего состояния"""
        if os.path.exists(self.filename):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(self.backup_dir, f"tasks_{timestamp}.json")
            shutil.copy2(self.filename, backup_file)
            self._cleanup_old_backups()
    
    def _cleanup_old_backups(self, keep: int = 10):
        """Удаляет старые бэкапы"""
        backups = sorted([f for f in os.listdir(self.backup_dir) if f.startswith("tasks_")])
        for old_backup in backups[:-keep]:
            os.remove(os.path.join(self.backup_dir, old_backup))
    
    def _recover_from_backup(self) -> List[Dict[str, Any]]:
        """Восстанавливает данные из последнего бэкапа"""
        backups = sorted([f for f in os.listdir(self.backup_dir) if f.startswith("tasks_")])
        if backups:
            latest_backup = backups[-1]
            backup_path = os.path.join(self.backup_dir, latest_backup)
            try:
                with open(backup_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return []
