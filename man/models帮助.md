数据库操作
https://docs.djangoproject.com/en/1.9/topics/db/queries/
```python

#取回所有
article_list = Article.objects.all();

#过滤
article_list = Article.objects.filter(title='testtitle');
article_list = Article.objects.all().filter(title='testtitle');#chain

#排除
article_list = Article.objects.exclude(title='testtitle');
article_list = Article.objects.all().exclude(title='testtitle');

#chain
article_list = Article.objects.all().exclude(
    title='testtitle').filter(
    time=...
    );


#取单个元素
one_article=Article.objects.get(pk=1);

#另一些取操作
#Python’s array-slicing syntax
Entry.objects.all()[:5] #取前5个
Entry.objects.all()[5:10]#取第6个到第10个

```
