


def reduce_stock(sender, instance, **kwargs):
    selected_products=instance.products
    print(selected_products)
    for product in selected_products:
        instance.product.stock -= 1
        instance.product.save()