# TOKEN = "6255018670:AAHDRCHL72HP0STq6oHn2WmWv6YcNtQtwoc"
# PAYMENT_TOKEN = "410694247:TEST:5b13aaed-c0e4-47c5-9d80-6e9197b704b4"


from dataclasses import dataclass

@dataclass
class Config:
    token: str = '6255018670:AAHDRCHL72HP0STq6oHn2WmWv6YcNtQtwoc'
    pay_token: str = '410694247:TEST:5b13aaed-c0e4-47c5-9d80-6e9197b704b4'
    admin_ids: int = 1