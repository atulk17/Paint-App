=====
PaintApp
=====

PaintApp is a Django app for Paint Shop Management. The client
can store all the shop records, access product inventory and get 
meaningful outputs for their shop.


Quick start
-----------

1. Add "paint" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'paint',
    ]

2. Include the paint URLconf in your project urls.py like this::

    path('', include('paint.urls')),

3. Run ``python manage.py migrate`` to create the paint models.

4. Start the development server and visit http://127.0.0.1:8000/

User Names and Passwords
-----------------------
Username->Password
admin -> admin12345
a -> a

============
User Manual
============
1. Home Page
------------
* Here you have three options at the top. 
    1. Shop Records
    2. Analysis
    3. New Records
* There are six most frequently used options:
    1. New Sales
    2. Add Product
    3. Search Customer
    4. Search Product
    5. Search Distributor
    6. Track Delivery
-------
2. Shop Records Page
-------
On this page you get the options to view all the data stored in 
the database. These are all the old data of your shop.
----
3. Analysis
----
This page gives you the options to view your sales, purchases, office expenses
and profit or loss on a monthly or yearly basis in graphical form.
There is a NOTE button on the bottom of each graph which shows you the change in 
sales, purchases, profits or loss compared to previous month/year.
----
4. New Records Page
----
This is the page where you can add the new data of the shop. You will get the
options of all the entries in which the data can be inserted. Clicking on the 
any of the options will take you to the 'add records' page of that entry, where
you can add the new data, modify it or delete it.
---
5. Search Customer Page
---
Clicking on 'Search Customer' tab on the home page takes you to the search form
where you can search the customers using their name or phone number. You can type in 
some pattern and the app will fetch the results which are similar to those patterns.
There is a 'New' and 'Update' tab on this page which takes you to the 'add records/change records'
page of customers.
----
6. Search Products Page
---
Clicking on 'Search Products' tab on the home page takes you to the search form
where you can search the products using their name. You can type in 
some pattern and the app will fetch the results which are similar to those patterns.
There is a 'New' and 'Update' tab on this page which takes you to the 'add records/change records'
page of products.
----
7. Search Distributor Page
---
Clicking on 'Search Distributor' tab on the home page takes you to the search form
where you can search the distributors using their name or phone number. You can type in 
some pattern and the app will fetch the results which are similar to those patterns.
There is a 'New' and 'Update' tab on this page which takes you to the 'add records/change records'
page of distributors.