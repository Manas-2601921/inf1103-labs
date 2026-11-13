from abc import ABC, abstractmethod
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_costs(self) -> float:
        pass
