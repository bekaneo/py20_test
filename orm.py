# SELECT

# SELECT * FROM product;
# product.objects.all()

# SELECT name, price FROM product;
# product.objects.only('name', 'price')

# SELECT * FROM product WHERE conditions
# product.object.filter(condition)
# сравнения
# ==
# SELECT * FROM product WHERE category_id = 'tv'
# product.objects.filter(category_id='tv')

# !=
# SELECT * FROM products WHERE NOT category_id = 'tv'
# Product.objects.filter(~Q(category_id = 'tv'))
# Product.objects.exclude(category_id = 'tv')
# <
# SELECT * FROM product WHERE price > 5000
# product.objects.filter(price__gt=5000)

# >
# SELECT * FROM product WHERE price < 5000
# product.objects.filter(price__lt=5000)

# <=
# SELECT * FROM product WHERE price <= 5000
# product.objects.filter(price__lte=5000)

# >=
# SELECT * FROM product WHERE price >= 5000
# product.objects.filter(price__gte=5000)

# in
# SELECT * FROM product WHERE category_id IN ('tv', 'smartphones')
# products.objects.filter(category_id__in=['tv', 'smartphones'])

# between
# SELECT * FROM product WHERE price BETWEEN 100 AND 1000
# products.objects.filter(price__range=[100, 1000])

# like
'str'
# SELECT * FROM product WHERE name LIKE 'iphone 13'
# Product.objects.filter(name__exact='iphone 13')

# SELECT * FROM product WHERE name ILIKE 'iphone 13'
# Product.objects.filter(name__iexact='iphone 13')

'str%'
# SELECT * FROM product WHERE name LIKE 'iphone%'
# Product.objects.filter(name__startswith='iphone')

# SELECT * FROM product WHERE name ILIKE 'iphone%'
# Product.objects.filter(name__istartswith='iphone')

'%str'
# SELECT * FROM product WHERE name LIKE '%13'
# Product.objects.filter(name__endswith='13')

# SELECT * FROM product WHERE name ILIKE '%13'
# Product.objects.filter(name__iendswith='13')

'%str%'
# SELECT * FROM product WHERE name LIKE '%hone%'
# Product.objects.filter(name__contains='hone')

# SELECT * FROM product WHERE name ILIKE '%hone%'
# Product.objects.filter(name__icontains='hone')


# ORDER BY
# SELECT * FROM product ORDER BY price ASC
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price DESC
# Product.objects.order_by('-price')

# LIMIT
# SELECT * FROM product LIMIT 10
# Product.objects.all()[:10]
# SELECT * FROM product LIMIT 10 OFFSET 5
# Product.objects.all()[5:15]

# INSERT
# INSERT INTO product (...) VALUES (...)
# Product.objects.create(name='...', description='...', ...)

# product = Product(name='...', description='...', ...)
# product.save()

# INSERT INTO product (...) VALUES (...), (...);
# Product.object.bulk_create([Product(...), Product(...)])

# UPDATE

# UPDATE product SET price = 1000;
# Product.objects.update(price=1000)

# UPDATE product SET price = 1000 WHERE category_id = 'notebooks'
# Product.objects.filter(category_id='notebooks').update(price=1000)

# DELETE

# DELETE FROM product
# Product.objects.delete()

# DELETE FROM product WHERE category_id = 'notebooks'
# Product.objects.filter(category_id='notebooks').delete()

# получить один объект
# Category.objects.get(slug='tv')
# Product.objects.get(id=2)


# quantity
# SELECT COUNT(*) FROM product
# Product.object.count()
# SELECT COUNT(*) FROM product WHERE price < 1000
# Product.object.filter(price__lt=1000).count()
