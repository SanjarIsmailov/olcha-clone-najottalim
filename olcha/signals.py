from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Order, Basket, OrderItem, Product, Rate, Category

@receiver(post_save, sender=Order)
def create_order_items(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        basket_items = Basket.objects.filter(user=user)

        for item in basket_items:
            OrderItem.objects.create(
                order=instance,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        basket_items.delete()

@receiver(post_delete, sender=Product)
def delete_related_product_data(sender, instance, **kwargs):
    instance.ratings.all().delete()
    instance.comments.all().delete()
    instance.basket_items.all().delete()
    OrderItem.objects.filter(product=instance).delete()

# Prevent duplicate ratings
@receiver(pre_save, sender=Rate)
def prevent_duplicate_ratings(sender, instance, **kwargs):
    if Rate.objects.filter(user=instance.user, product=instance.product).exists():
        raise ValidationError("You have already rated this product!")
