from django import template
from django.urls import reverse, NoReverseMatch
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag("tree_menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context.get("request")
    if not request:
        return {"menu_tree": []}

    current_url = request.path_info
    menu_items = (
        MenuItem.objects.filter(menu_name=menu_name)
        .select_related("parent")
        .order_by("order")
    )

    # Строим дерево меню
    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                is_active = item.get_url() == current_url
                tree.append(
                    {
                        "item": item,
                        "children": children,
                        "is_active": is_active,
                        "has_active": is_active
                        or any(child["has_active"] for child in children),
                    }
                )
        return tree

    menu_tree = build_tree(menu_items)

    return {"menu_tree": menu_tree, "current_url": current_url}
