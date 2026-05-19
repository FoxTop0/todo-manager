"""
Модуль валидации данных для Todo List Manager
Разработчик: Dev 4
"""

from datetime import datetime
from typing import Tuple, Optional


class TaskValidator:
    """Класс для валидации данных задач"""
    
    @staticmethod
    def validate_title(title: str) -> Tuple[bool, Optional[str]]:
        """Валидация названия задачи"""
        if not title or not isinstance(title, str):
            return False, "Название задачи не может быть пустым"
        
        title = title.strip()
        if len(title) == 0:
            return False, "Название задачи не может быть пустым"
        
        if len(title) > 100:
            return False, "Название задачи не должно превышать 100 символов"
        
        if len(title) < 3:
            return False, "Название задачи должно содержать минимум 3 символа"
        
        forbidden_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in forbidden_chars:
            if char in title:
                return False, f"Название не может содержать символ '{char}'"
        
        return True, None
    
    @staticmethod
    def validate_description(description: str) -> Tuple[bool, Optional[str]]:
        """Валидация описания задачи"""
        if description is None:
            return True, None
        
        description = str(description).strip()
        if len(description) > 500:
            return False, "Описание не должно превышать 500 символов"
        
        return True, None
    
    @staticmethod
    def validate_priority(priority: str) -> Tuple[bool, Optional[str]]:
        """Валидация приоритета задачи"""
        valid_priorities = ['low', 'medium', 'high']
        
        if not priority or priority.lower() not in valid_priorities:
            return False, f"Приоритет должен быть одним из: {', '.join(valid_priorities)}"
        
        return True, None
    
    @staticmethod
    def validate_status(status: str) -> Tuple[bool, Optional[str]]:
        """Валидация статуса задачи"""
        valid_statuses = ['pending', 'in_progress', 'completed']
        
        if not status or status.lower() not in valid_statuses:
            return False, f"Статус должен быть одним из: {', '.join(valid_statuses)}"
        
        return True, None
    
    @staticmethod
    def validate_date(date_str: str) -> Tuple[bool, Optional[str]]:
        """Валидация даты (формат YYYY-MM-DD)"""
        if not date_str:
            return True, None
        
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True, None
        except ValueError:
            return False, "Неверный формат даты. Используйте ГГГГ-ММ-ДД"
