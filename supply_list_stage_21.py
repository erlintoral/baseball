# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SupplyList
class Reminder:
    """Simple reminder with due date and optional message."""
    
    def __init__(self, text="", due_date=None):
        self.text = text
        self.due_date = due_date or datetime.now()
        self.is_done = False
    
    @property
    def is_overdue(self):
        if not self.is_done:
            return self.due_date < datetime.now()
        return False
    
    def __str__(self):
        status = "✓" if self.is_done else ("⚠" if self.is_overdue else "")
        return f"{status} [{self.due_date.strftime('%Y-%m-%d')}] {self.text}"


def add_reminders():
    """Add reminders to the global list. Returns count of added reminders."""
    from datetime import timedelta, date
    
    today = date.today()
    
    # Example: 3 sample reminders for different priorities
    reminders_data = [
        {"text": "Позвонить поставщику 'Электроника-Мир'", "days_until": 2},
        {"text": "Заказать бумагу для принтера", "days_until": 0},
        {"text": "Обновить контакты у логистов", "days_until": 5},
    ]
    
    reminders = []
    for item in reminders_data:
        d = today + timedelta(days=item["days_until"])
        r = Reminder(text=item["text"], due_date=d)
        reminders.append(r)
    
    return reminders, len(reminders)


def show_reminder_status():
    """Display all active and overdue reminders."""
    from datetime import date
    
    today = date.today()
    
    reminder_list = [
        Reminder(text="Позвонить поставщику 'Электроника-Мир'", due_date=today - timedelta(days=1)),
        Reminder(text="Заказать бумагу для принтера", due_date=today),
        Reminder(text="Обновить контакты у логистов", due_date=today + timedelta(days=3)),
    ]
    
    print("\n📋 Статус напоминаний:")
    for r in reminder_list:
        if r.is_done:
            print(f"  ✓ {r.text}")
        elif r.is_overdue:
            print(f"  ⚠ Просрочено! {r.text} (срок: {r.due_date.strftime('%Y-%m-%d')})")
        else:
            days_left = (r.due_date - today).days
            print(f"  📅 Через {days_left} дн. — {r.text}")


# Примеры использования
if __name__ == "__main__":
    reminders, count = add_reminders()
    print(f"Добавлено напоминаний: {count}\n")
    
    for r in reminders:
        print(r)
    
    show_reminder_status()
