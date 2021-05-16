from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    #primer metodo
    #Trae todo el objeto del serializer los campos que se indico en este caso "el id y la description"
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    #segundo metodo
    #solo trae lo que hayamos colocado en el __str__ de los modelos
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date',)

    #tercer metodo
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            "image": instance.image if instance.image != '' else '',
            "measure_unit": instance.measure_unit.description,
            "category_product": instance.category_product.description,
        }