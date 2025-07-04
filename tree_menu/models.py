from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    name = models.CharField(_("name"), max_length=100)
    named_url = models.CharField(
        _("named URL"),
        max_length=100,
        blank=True,
        help_text=_("Named URL from your urls.py file"),
    )
    url = models.CharField(
        _("url"), max_length=200, blank=True, help_text=_("Relative or absolute URL")
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("parent"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )
    menu_name = models.CharField(
        _("menu name"),
        max_length=50,
        help_text=_("Name of the menu this item belongs to"),
    )
    order = models.PositiveIntegerField(_("order"), default=0)

    class Meta:
        verbose_name = _("menu item")
        verbose_name_plural = _("menu items")
        ordering = ["order"]

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                url = reverse(self.named_url)
            except NoReverseMatch:
                url = self.url
            return url
        return self.url

    def is_active(self, current_url):
        return self.get_url() == current_url
