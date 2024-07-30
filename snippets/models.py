from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):

    name =models.CharField(max_length=50,blank=False,null=False)
    age =models.IntegerField()
    createdOn =models.DateTimeField( auto_now=True,)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=["createdOn"]
    
    
    
class Post(models.Model):
    author =models.ForeignKey("Author", on_delete=models.CASCADE)  
    createdOn =models.DateField(auto_now=True)
    title =models.CharField(max_length=200)
    content =models.TextField()
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE,blank=True,null=True,)
    
    class Meta:
        ordering=["createdOn"]
    
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    
    createdOn =models.DateTimeField(auto_now=True)
    Text =models.TextField()
    
    posts =models.OneToOneField("Post", on_delete=models.CASCADE,related_name="post_comment",null=True, default=1)
    # post =models.OneToOneField("Post", on_delete=models.CASCADE)
    
    user =models.ForeignKey(User, on_delete=models.CASCADE)  
    class Meta:
        ordering=["createdOn"]
        
    def __str__(self) -> str:
        return self.commentContent
    
    
      

