from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    @property
    def products_count(self):
        count = self.products.count()
        return count

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BooleanField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", null=True
    )

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all()]
        if not stars:
            return 0
        average_mark = round(sum(stars) / len(stars), 2)
        return average_mark

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="reviews", null=True
    )
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True)

    def __str__(self):
        return self.text
