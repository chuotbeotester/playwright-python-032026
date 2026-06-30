from datetime import datetime


class TextData:
    @staticmethod
    def create_text_data(base_text: str) -> str:
        """Tạo chuỗi duy nhất: base_text_YYYYMMDD-HHMMSS."""
        return f"{base_text}_{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    @staticmethod
    def create_unique_email(prefix: str, domain: str) -> str:
        """Tạo email duy nhất: prefix_YYYYMMDDHHMMSS@domain."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{prefix}_{timestamp}{domain}"

    @staticmethod
    def create_unique_username(prefix: str) -> str:
        """Tạo username duy nhất: prefix_YYYYMMDDHHMMSS."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{prefix}_{timestamp}"
