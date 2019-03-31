# Check SQL

```bash
(venv) $ python src/manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(10) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

# Model

```bash
python manage.py shell

from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username='admin')

# create post object and save it to database
post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
post.save()

# Or we can also create it with the following
Post.objects.create(title='One more post', slug='one-more-post', body='Post body', author=user)

# updating objects
post.title = 'New title'
post.save()
```

# About Get Method
The get() method allows us to retrieve a single object form the database.

If no results are returned by the database, this method will raise a DoesNotExist exception,  
and if the database returns more than one result, it will raise a MultipleObjectsReturned.

# Retrieving objects
The Django object-realtion mapping (ORM) is based on QuerySet.

A QuerySet is a collection of objects from our database that can have several filters to limit the results.

```bash
# Retrieve all object from the database
all_posts = Post.objects.all()
```

# Using the filter() method
To filter a QuerySet, you can use the filter() method of the manager.

```bash
Post.objects.filter(publish__year=2017)
Post.objects.filter(publish__year=2017, author__username='admin')

Post.objects.filter(publish__year=2017) \
            .filter(author__username='admin')
```

# Using exclude()
We can exclude certain reuslts from your QuerySet using the exclude() method of the manager.  

```bash
Post.objects.filter(publish__year=2017).exclude(title__startswith='Why')
```

# Using order_by()
We can order results by different fields using the order_by() method of the manager.

```bash
# order
Post.objects.order_by('title')

# Ascending order
Post.objects.order_by('-title'_)
```

# Deleting objects
If we want to delete an object, you can do it from the object instance using the delete() method.

```bash
post = Post.objects.get(id=1)
post.delete()
```

# When QuerySets are evaluated
We can concatenate as many filters as you like to a QuerySet, and you will not hit the database until
the QuerySet is evaluated.

QuerySet are only evaluated in the following case.

* The first time you iterate over them
* When you slice them, for instance, Post.objects.all()[:3]
* When you [picle](https://qiita.com/moroku0519/items/f1f4c059c28cb1575a93) or cache them
* When you can repr() or len() on them
* When you explicitly call list() on them
* When you test them in a statement, such as bool(), or, and, or if

[ref](https://docs.djangoproject.com/en/2.0/ref/models/)
