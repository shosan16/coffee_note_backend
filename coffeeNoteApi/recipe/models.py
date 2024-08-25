from django.db import models


class Recipe(models.Model):
    """
    レシピモデル
    """

    class Meta:
        db_table = "recipe"
        ordering = ["created_at"]
        verbose_name = "レシピ"

    name = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    click_count = models.IntegerField(default=0)
    grind_size = models.CharField(max_length=50, blank=True)
    coffee_amount = models.IntegerField(default=0)
    water_amount = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
