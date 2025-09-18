import sqlite3
import time
from contextlib import contextmanager


@contextmanager
def get_db_connection():
    conn = sqlite3.connect("Mydatabase.db")
    try:
        yield conn
    finally:
        conn.close()


class BaseService:
    @staticmethod
    def execute_query(query, params=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchone()

class UserService(BaseService):
    def get_user(self, user_id):
        return self.execute_query("SELECT * FROM users WHERE user_id = ?", (user_id,))

class OrderService(BaseService):
    def get_orders(self, order_id):
        return self.execute_query("SELECT * FROM orders WHERE order_id = ?", (order_id,))
def main():
    user_service = UserService()
    order_service = OrderService()
    start_time = time.perf_counter()
    try:
        user = user_service.get_user(1)
        print("User Details:", user)

        orders = order_service.get_orders(1)
        print("User Orders:", orders)
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.10f} seconds")


if __name__ == '__main__':
    main()
