def calculate_storage(users):
    return users * 5

required_storage = calculate_storage(100)
print("Required Storage:", required_storage, "GB")


def calculate_revenue(customers, subscription_fee):
    return customers * subscription_fee

monthly_revenue = calculate_revenue(250, 20)
print("Monthly Revenue: $", monthly_revenue)
