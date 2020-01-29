import collections

from datetime import datetime


class TransactionPolicy(collections.UserDict):
    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)


policy = TransactionPolicy({
    "client001": {
        "fee": 1000.0,
        "expiration_date": datetime(2020, 1, 3)
    }
})

print(policy["client001"])
policy.change_in_policy("client001", expiration_date=datetime(2020, 1, 4))
print(policy["client001"])

print(dir(policy))