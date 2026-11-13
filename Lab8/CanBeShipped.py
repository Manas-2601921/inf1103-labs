from abc import ABC, abstractmethod
class CanBeShipped(ABC):
    @staticmethod
    @abstractmethod
    def calculate_shipping_costs(self):
        pass
