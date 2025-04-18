from account import Account

class Student:
    def __init__(self, name: str, financial_aid_eligible: bool, has_scholarship: bool, account: Account):
        self.name = name
        self.financial_aid_eligible = financial_aid_eligible
        self.has_scholarship = has_scholarship
        self.course_material_access = {}
        self.account = account
        account.student = self

    def search_courses(self, keyword, courses):
        print(f"\n{self.name} is searching for '{keyword}':")
        for c in courses:
            if keyword.lower() in c.name.lower():
                print(f"{c.course_id}: {c.name} - ${c.price}")

    def pay_for_courses(self, price):
        discount = 0.5 if self.has_scholarship else (0.2 if self.financial_aid_eligible else 0)
        final_price = price * (1 - discount)
        print(f"{self.name} paid ${final_price:.2f}")
