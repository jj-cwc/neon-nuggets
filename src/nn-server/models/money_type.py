from sqlalchemy.types import TypeDecorator, Numeric
from money import Money

class MoneyType(TypeDecorator):
    impl = Numeric
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(Numeric(12, 2))  # Assuming you want to store amounts with 2 decimal places
    
    def process_bind_param(self, value, dialect):
        return value.amount if value is not None else None
    
    def process_result_value(self, value, dialect):
        return Money(value, 'XXX') if value is not None else None  # XXX is a placeholder for your currency code
