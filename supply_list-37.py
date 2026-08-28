# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SupplyList
import unittest


class TestSupplyList(unittest.TestCase):
    def test_add_supplier(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_supplier("Vendor A", 100, "Hardware")
        self.assertEqual(len(sl.suppliers), 1)
        self.assertEqual(sl.suppliers[0].name, "Vendor A")

    def test_add_order(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_supplier("Vendor A", 100, "Hardware")
        sl.add_order("Item X", 50, 10, "Vendor A", 100)
        self.assertEqual(len(sl.orders), 1)
        self.assertEqual(sl.orders[0].item, "Item X")
        self.assertEqual(sl.orders[0].qty, 10)
        self.assertEqual(sl.orders[0].price, 100)

    def test_add_note(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_note("Order for Q1")
        self.assertIn("Order for Q1", sl.notes)

    def test_add_reminder(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_reminder("Call Vendor A", 30)
        self.assertEqual(len(sl.reminders), 1)
        self.assertEqual(sl.reminders[0].text, "Call Vendor A")
        self.assertEqual(sl.reminders[0].days, 30)

    def test_add_priority(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_priority("Item X", "Critical")
        self.assertEqual(len(sl.priorities), 1)
        self.assertEqual(sl.priorities[0].item, "Item X")
        self.assertEqual(sl.priorities[0].priority, "Critical")

    def test_add_stock_record(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_stock_record("Item X", 100)
        self.assertEqual(len(sl.stock), 1)
        self.assertEqual(sl.stock[0].item, "Item X")
        self.assertEqual(sl.stock[0].qty, 100)

    def test_add_comment(self):
        from supplylist import SupplyList
        sl = SupplyList()
        sl.add_comment("Item X", "Check price with Vendor A")
        self.assertEqual(len(sl.comments), 1)
        self.assertEqual(sl.comments[0].item, "Item X")
        self.assertEqual(sl.comments[0].text, "Check price with Vendor A")


if __name__ == "__main__":
    unittest.main()
