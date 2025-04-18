class Account:
    def __init__(self, username: str, password: str, is_admin=False, is_finance=False, role_access: str = "student"):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_finance = is_finance
        self.role_access = role_access
        self.student = None  # Optional: Back-reference to Student

    def identify_user(self):
        return self.is_admin

    def verify_access(self):
        if self.role_access in ["admin", "student", "finance"]:
            return True
        else:
            print("Access denied.")
            return False
