class TaskValidator:
    @staticmethod
    def validate_title(title):
        if not title or len(title.strip()) == 0:
            return False, "Название не может быть пустым"
        if len(title) > 100:
            return False, "Название слишком длинное"
        return True, None
