"""
Модуль логирования для Todo List Manager
Разработчик: Dev 5
"""

import logging
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional
import traceback


class TaskLogger:
    """Класс для логирования операций с задачами"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup_logger()
        return cls._instance
    
    def _setup_logger(self):
        """Настройка логгера"""
        self.logger = logging.getLogger('TaskManager')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler = logging.FileHandler('todo_manager.log', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_operation(self, operation: str, user: str = "anonymous"):
        """Декоратор для логирования операций"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    start_time = datetime.now()
                    self.logger.info(f"Пользователь {user} начал операцию: {operation}")
                    
                    result = func(*args, **kwargs)
                    
                    end_time = datetime.now()
                    duration = (end_time - start_time).total_seconds()
                    
                    self.logger.info(
                        f"Пользователь {user} завершил операцию '{operation}'. "
                        f"Время выполнения: {duration:.2f}с"
                    )
                    
                    return result
                    
                except Exception as e:
                    self.logger.error(
                        f"Ошибка в операции '{operation}' пользователя {user}: {str(e)}\n"
                        f"{traceback.format_exc()}"
                    )
                    raise
                    
            return wrapper
        return decorator
    
    def log_error(self, error_msg: str, context: dict = None):
        """Логирование ошибок"""
        message = error_msg
        if context:
            message += f" | Контекст: {context}"
        self.logger.error(message)
    
    def log_info(self, info_msg: str):
        """Логирование информационных сообщений"""
        self.logger.info(info_msg)
    
    def get_logs(self, level: str = None, limit: int = 100) -> list:
        """Получение последних логов"""
        try:
            with open('todo_manager.log', 'r', encoding='utf-8') as f:
                logs = f.readlines()
            logs = logs[-limit:]
            if level:
                logs = [log for log in logs if f" - {level.upper()} - " in log]
            return logs
        except FileNotFoundError:
            return []
