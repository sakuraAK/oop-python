from  datetime import datetime

"""
Module to manage personal expenses
"""
class Expense:
    """
    Represents a single expense
    """
    def __init__(self, description: str, amount: float, date: str = None):
        """
        Initialize expense object
        
        Args:
        :param description: Expense description
        :type description: str
        :param amount: Amount of the expense
        :type amount: float
        :param date: Date of the expense. If not provided will be defaulted to today date. Expect date in formt YYYY-MM-DD (2025-12-19)
        :type date: str
        
        Raises: 
            ValueError: If amount 0 or negative
        
        """
        self._amount = 0
        self.amount = amount
        self.description = description
        if not date:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date
        
    
    
    @property
    def amount(self) -> float:
        return self._amount
    
    @amount.setter
    def amount(self, value: float):
        if value <= 0:
            raise ValueError(f"Expense amount should be greater than 0. Got {value}")
        self._amount = value
            
    
    def __str__(self):
        """
         Return string representation of expense
        """
        
        return  f"{self.description} - ${self.amount:.2f} {self.date}"
    
    
    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    
    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            description=data["description"],
            amount=data["amount"],
            date=data["date"]
        )
        
    