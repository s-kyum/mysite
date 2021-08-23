from django import template


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

# 기존값 value에서 입력으로 반은값 arg를 빼서 반환한다.