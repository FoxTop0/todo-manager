class TaskValidator:
    @staticmethod
    def validate_title(title):
        if not title or len(title.strip()) == 0:
            return False, "Название не может быть пустым"
        if len(title) > 100:
            return False, "Название слишком длинное"
        if len(title) < 3:
            return False, "Название слишком короткое"
        return True, None
    
    @staticmethod
    def validate_priority(priority):
        valid = ['low', 'medium', 'high']
        if priority.lower() not in valid:
            return False, f"Приоритет должен быть: {valid}"
        return True, None
