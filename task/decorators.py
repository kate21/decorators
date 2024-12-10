from task.modules import modul_admin_rights
from task.modules import modul_exception


#task1

@is_admin
def show_customer_receipt(user_type: str):
    print("Here is your receipt")
    # Some very dangerous operation

show_customer_receipt(user_type = 'admin')

#task2

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

