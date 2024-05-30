from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200,unique=True)
    email =models.EmailField(max_length=105)
    password = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description =models.TextField()
    RecipeMaker = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Ingredients(models.Model):
    title = models.CharField(max_length=200)
    Ourrecipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE, unique=True)  # Assuming unique user-recipe rating
    rateOutOf5 = models.IntegerField()
    RatingGiver = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    comment_text = models.CharField(max_length=300)
    commentor = models.ForeignKey(User,on_delete=models.CASCADE)
    
