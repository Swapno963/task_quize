
from .models import User,Recipe,Rating,Comment,Ingredients
from .userSerializer import userSerializer
from .RecipeSerializer import RecipeSerializer
from .RatingSerializer import RatingSerializer
from .CommentSerializer import CommentSerializer
from .IngredientsSerializer import IngredientsSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class =RecipeSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class IngradientViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
