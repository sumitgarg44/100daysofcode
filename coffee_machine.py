from static.arts.coffee_machine_art import coffee_emoji
from static.coffee_machine_const import coins, menu, resources
from static.colors import color

is_on = True


def report_resources(current=True):
    """Print current resources"""
    for resource in resources:
        if isinstance(resources[resource], list):
            if current:
                print(f"{resource}: ${resources[resource][1]}")
            else:
                print(f"{resource}: ${resources[resource][0]}")
        else:
            if resource == "money":
                print(f"{resource}: ${resources[resource]}")
            elif resource == "coffee":
                print(f"{resource}: {resources[resource]}g")
            else:
                print(f"{resource}: {resources[resource]}ml")


def have_enough_resources(flavor):
    """Validate if have enough resources to fulfil the order"""
    for resource in resources:
        req_resource = menu[flavor]["ingredients"][resource]
        avail_resource = resources[resource]
        if req_resource > avail_resource:
            return (
                False,
                f"\n{color.BOLD}{color.RED}Sorry there is not enough {resource}.{color.END}",
            )
        else:
            return True, "All Ok!"


def process_coins():
    """Accepts coins and calculate their total value"""
    coins_value = 0
    print("\nPlease enter the coins:")
    for coin in coins:
        num_of_coins = int(input(f"How many {coin} coins? "))
        coins_value += num_of_coins * coins[coin]
    return coins_value


def is_transaction_successful(flavor, amount):
    """
    Returns False if not successful, otherwise returns amount
    should be refunded after taking out the drink cost
    """
    req_amount = menu[flavor]["cost"]
    if amount >= req_amount:
        if isinstance(resources["money"], list):
            resources["money"][0] = resources["money"][1]
            resources["money"][1] = resources["money"][1] + req_amount
        else:
            resources["money"] = [resources["money"], req_amount]
        refund = round((amount - req_amount), 2)
        return refund
    else:
        return False


def make_coffee(flavor):
    """It makes coffee"""
    print(f"\n{color.DARKCYAN}Report before purchasing {flavor}:{color.END}")
    report_resources(current=False)

    for ingredient in menu[flavor]["ingredients"]:
        resources[ingredient] = (
            resources[ingredient] - menu[flavor]["ingredients"][ingredient]
        )

    print(f"\n{color.DARKCYAN}Report after purchasing {flavor}:{color.END}")
    report_resources(current=True)
    print(
        f"\n{color.BOLD}{color.PURPLE}Here is your {flavor} {coffee_emoji}. Enjoy!{color.END}"
    )


def main(coffee):
    """Main logic to process coffee order"""
    res_status, res_msg = have_enough_resources(flavor=coffee)
    if res_status:
        amt_received = process_coins()
        should_refund = is_transaction_successful(flavor=coffee, amount=amt_received)
        if not should_refund:
            print(
                f"\n{color.RED}Sorry that's not enough money. Money refunded.{color.END}"
            )
        else:
            print(f"\n{color.BLUE}Here is ${should_refund} in change.{color.END}")
            make_coffee(flavor=coffee)
    else:
        print(res_msg)


while is_on:
    order = str(input(f"\nWhat would you like? {tuple(menu.keys())}: ")).lower()
    if order == "off":
        is_on = False
    elif order == "latte":
        main(coffee=order)
    elif order == "cappuccino":
        main(coffee=order)
    elif order == "espresso":
        main(coffee=order)
    elif order == "report":
        report_resources()
    else:
        print(f"{color.RED}Ops! {order} is not available{color.END}")
