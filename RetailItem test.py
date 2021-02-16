import RetailitemClass as i


def main():
    item_one = i.RetailItem("Jacket", 12, 59.95)
    item_two = i.RetailItem("Designer Jeans", 40, 24.95)
    item_three = i.RetailItem("Shirt", 20, 24.95)

    print(
        "Item One: \n",
        "Description:",
        item_one.get_description(),
        "\n",
        "Units in inventory:",
        item_one.get_invenunit(),
        "\n",
        "Price:",
        item_one.get_price(),
    )

    print()

    print(
        "Item Two: \n",
        "Description:",
        item_two.get_description(),
        "\n",
        "Units in inventory:",
        item_two.get_invenunit(),
        "\n",
        "Price:",
        item_two.get_price(),
    )

    print()

    print(
        "Item Three: \n",
        "Description:",
        item_three.get_description(),
        "\n",
        "Units in inventory:",
        item_three.get_invenunit(),
        "\n",
        "Price:",
        item_three.get_price(),
    )


main()