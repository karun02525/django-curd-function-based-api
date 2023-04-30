from rest_framework import serializers
from .models import Product,Category,Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name','price']
        #exclude = ['id']
        
    def validate(self, data):
        
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cant not be a number'})
        
        if data['price']<=100:
            raise serializers.ValidationError({'error':'price must be between 100 and 10000'})
                    
        
        return data
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']
            
  
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'       
        depth = 1     