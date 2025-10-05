from django import template

register = template.Library()


@register.simple_tag
def get_discounted_price(course, discount_percent=10):
    if course.price > 0:
        discounted = course.price * (100 - discount_percent) / 100
        return "%.2f" % discounted
    return "0.00"
