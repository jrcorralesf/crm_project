


def reduce_stock(sender, instance, **kwargs):
    print('///////////////////////////////////////////////////////////////')
    print(instance)
    selected_products=instance.products
    print('///////////////////////////////////////////////////////////////')
    print(selected_products)
    for product in selected_products:
        product.stock -= 1
        product.save()