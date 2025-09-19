import sqlite3
import time

class DatabaseConnection: # Class variable to store the single instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect("Mydatabase.db")
        return cls._instance

    def get_connection(self):
        return self.conn  # Return the single connection instance

class BaseServiceSimple:
    @staticmethod
    def execute_query(query, params=None):
        conn = DatabaseConnection().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchone()

class UserServiceSimple(BaseServiceSimple):
    def get_user(self, user_id):
        return self.execute_query("SELECT * FROM users WHERE user_id = ?", (user_id,))

class OrderServiceSimple(BaseServiceSimple):
    def get_orders(self, order_id):
        return self.execute_query("SELECT * FROM orders WHERE order_id = ?", (order_id,))

def main_singleton():
    user_service = UserServiceSimple()
    order_service = OrderServiceSimple()

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

    end_time = time.perf_counter()  # End time measurement and print execution time
    print(f"Execution time: {end_time - start_time:.10f} seconds")

if __name__ == '__main__':
    main_singleton()
