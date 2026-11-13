from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Order import Order

supplier = Supplier("S2601921", "Manas", "manas@gmail.com")
laptop = PhysicalProduct("P1", "Laptop", 1200.00, 10, 2.5, supplier)
ebook = DigitalProduct("P2", "E-book", 15.00, 100, 3.2, supplier)

#3 OrderLine objects and 2 Product objects.
order_a = Order("O-001")
order_a.add_order_line(laptop, 2)
order_a.add_order_line(ebook, 3)

# Display each order line and the order total
for line in order_a.get_order_lines():
    line.display_orderline()
    print(f"Subtotal: ${line.calculate_subtotal():.2f}\n")
print(f"Order O-001 total: ${order_a.calculate_order_total():.2f}")

# Add the same Product to a different Order
order_b = Order("O-002")
order_b.add_order_line(laptop, 1)

for line in order_b.get_order_lines():
    line.display_orderline()
    print(f"Subtotal: ${line.calculate_subtotal():.2f}\n")
print(f"Order O-002 total: ${order_b.calculate_order_total():.2f}")

# Each Order creates and owns its own OrderLine; both lines refer to the same Product.
line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]
all_lines = order_a.get_order_lines() + order_b.get_order_lines()
product_count = len({id(line.get_product()) for line in all_lines})
print(f"\nOrderLine objects: {len(all_lines)}")
print(f"Product objects: {product_count}")
print(f"\nSame OrderLine object? {line_a is line_b}")
print(f"id(line_a) = {id(line_a)}, id(line_b) = {id(line_b)}")
print(f"Same Product object? {line_a.get_product() is line_b.get_product()}")
print(f"id(line_a product) = {id(line_a.get_product())}, id(line_b product) = {id(line_b.get_product())}")
assert len(all_lines) == 3
assert product_count == 2
assert line_a is not line_b
assert line_a.get_product() is line_b.get_product()

# Remove the line through its owning Order, rather than managing the OrderLine directly.
order_b.remove_order_line(laptop)
assert order_b.get_order_lines() == []
print(f"\nOrder O-002 lines after removal: {len(order_b.get_order_lines())}")
