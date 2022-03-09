from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'title', 'description', 'slug', 'categories', 'price', 'quantity_available', 'created',
                  'updated']
        depth = 2
        # name = models.CharField(max_length=200, null=False, default="")
        # title = models.CharField(max_length=200, null=True, default="product title")
        # description = models.TextField(blank=True)
        # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
        # slug = models.SlugField(max_length=200, default=str(uuid4())[:10])
        # categories = models.ManyToManyField(Category, related_name='category')
        # size = models.FloatField(default=0.0)
        # price = models.FloatField(default=0.0)
        # quantity_available = models.IntegerField(default=0)
        # created = models.DateTimeField(auto_now_add=True)
        # updated = models.DateTimeField(auto_now=True)

