# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SupplyList
def test_errors():
    from supplylist import (
        Product, Supplier, Order, OrderItem, PurchasePlan, PlanItem
    )
    from supplylist.exceptions import (
        ProductAlreadyExists, SupplierAlreadyExists,
        ProductNotInPlan, SupplierNotInPlan,
        InsufficientStock, InvalidPriority,
        DuplicateOrderItem, NegativeOrderItem,
        InvalidQuantity, DuplicateOrder, InvalidSupplier,
        OrderNotFound, ProductNotFound, SupplierNotFound
    )

    p1 = Product("A", 100, 10, "note1")
    p2 = Product("B", 200, 20, "note2")
    s1 = Supplier("S1", "addr1", 1000)
    s2 = Supplier("S2", "addr2", 2000)
    plan = PurchasePlan()
    plan.add_product(p1)
    plan.add_product(p2)
    plan.add_supplier(s1)
    plan.add_supplier(s2)
    item1 = OrderItem(p1, s1, 5, 50.0, 1)
    item2 = OrderItem(p2, s2, 3, 30.0, 2)
    order1 = Order("O1", [item1, item2], 1)
    plan.add_order(order1)

    # --- duplicate product ---
    with pytest.raises(ProductAlreadyExists):
        plan.add_product(Product("C", 10, 10, ""))

    # --- duplicate supplier ---
    with pytest.raises(SupplierAlreadyExists):
        plan.add_supplier(s1)

    # --- product not in plan ---
    with pytest.raises(ProductNotInPlan):
        plan.add_order(Order("O2", [OrderItem(Product("X"), s1, 1, 1.0, 1)]))

    # --- invalid priority ---
    with pytest.raises(InvalidPriority):
        plan.add_order(Order("O3", [OrderItem(p1, s1, 1, 1.0, 1)], 0))

    # --- negative quantity ---
    with pytest.raises(NegativeOrderItem):
        plan.add_order(Order("O4", [OrderItem(p1, s1, -1, 1.0, 1)]))

    # --- zero quantity ---
    with pytest.raises(InvalidQuantity):
        plan.add_order(Order("O5", [OrderItem(p1, s1, 0, 1.0, 1)]))

    # --- duplicate order ---
    with pytest.raises(DuplicateOrder):
        plan.add_order(Order("O1", [item1, item2], 1))

    # --- supplier not in plan ---
    s3 = Supplier("S3", "addr3", 100)
    with pytest.raises(SupplierNotInPlan):
        plan.add_order(Order("O6", [OrderItem(p1, s3, 1, 1.0, 1)]))

    # --- duplicate order item (same product+supplier) ---
    dup_item = OrderItem(p1, s1, 2, 50.0, 1)
    with pytest.raises(DuplicateOrderItem):
        plan.add_order(Order("O7", [item1, dup_item], 2))

    # --- insufficient stock ---
    p3 = Product("C", 100, 5, "")
    plan.add_product(p3)
    s4 = Supplier("S4", "addr4", 100)
    plan.add_supplier(s4)
    item3 = OrderItem(p3, s4, 10, 10.0, 1)
    with pytest.raises(InsufficientStock):
        plan.add_order(Order("O8", [item3], 1))

    # --- plan items ---
    plan_item = PlanItem(p1, s1, 2, 100.0, 1)
    plan.add_plan_item(plan_item)
    with pytest.raises(DuplicateOrder):
        plan.add_order(Order("O9", [OrderItem(p1, s1, 1, 50.0, 1)], 1))

    # --- order not found ---
    with pytest.raises(OrderNotFound):
        order1.get_item(99)

    # --- product not found ---
    with pytest.raises(ProductNotFound):
        order1.get_product("X")

    # --- supplier not found ---
    with pytest.raises(SupplierNotFound):
        order1.get_supplier("S99")

    # --- edge: float price ---
    float_item = OrderItem(p1, s1, 1, 50.5, 1)
    order_f = Order("OF", [float_item], 1)
    plan.add_order(order_f)
    assert order_f.get_total() == pytest.approx(50.5)
