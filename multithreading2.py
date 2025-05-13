import threading
import time

total_tickets = 5
lock = threading.Lock()

def book_ticket(user_name):
    global total_tickets
    print(f"{user_name} is trying to book a ticket...")

    with lock:
        if total_tickets > 0:
            time.sleep(1)
            total_tickets -= 1
            print(f"✅ {user_name} successfully booked a ticket. Tickets left: {total_tickets}")
        else:
            print(f"❌ {user_name} failed to book. No tickets left.")

user_list = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

threads = []
for user in user_list:
    t = threading.Thread(target=book_ticket, args=(user,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("🎟️ Booking session ended.")
