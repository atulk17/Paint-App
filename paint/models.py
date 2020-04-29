from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from .validators import nonneg, alphanumeric, datevalid

DEL_STATUS = (
    ("DELIVERED", "DELIVERED"),
    ("NOT DELIVERED", "NOT DELIVERED"),
)
mop = (
    ("PENDING", "PENDING"),
    ("CHEQUE","CHEQUE"),
    ("CASH","CASH"),
    ("CARD", "CARD"),
)

class Employee(models.Model):
    Employee_id = models.AutoField(verbose_name='Employee Id',primary_key=True)
    Employee_firstname = models.CharField(verbose_name='Employee First Name', max_length=15,validators=[alphanumeric])
    Employee_lastname = models.CharField(verbose_name='Employee Last Name', max_length=15,validators=[alphanumeric])
    Address = models.CharField(verbose_name='Address', max_length=50)
    Job_description = models.CharField(verbose_name='Job Description', max_length=50)
    salary = models.IntegerField(verbose_name='Salary',validators=[nonneg])
    Bank_name = models.CharField(verbose_name='Bank Name', max_length=50)
    Bank_branch = models.CharField(verbose_name='Bank Branch', max_length=50)
    Bank_Accno = models.BigIntegerField(verbose_name='Bank Account Number',validators=[nonneg])
    Email_id = models.EmailField(verbose_name='Email ID', max_length=70)
    Phone_no = models.BigIntegerField(verbose_name='Phone No',validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    Education_level = models.CharField(verbose_name='Educaton Level', max_length=50)
    Date_of_joining = models.DateField(verbose_name='Date Of Joining',validators=[datevalid])
    objects = models.Manager()
    def __str__(self):
        return str(self.Employee_id)
    class Meta: 
        verbose_name_plural='Employee'
        db_table = "Employee"
        


class Distributor(models.Model):
    Distributor_id = models.AutoField(verbose_name='Distributor ID',primary_key=True)
    Distributor_name = models.CharField(max_length=50,validators=[alphanumeric])
    GSTIN = models.CharField(verbose_name='GSTIN', max_length=50)
    Address = models.CharField(verbose_name='Address', max_length=50)
    Email_id = models.EmailField(verbose_name='Email ID', max_length=70)
    Contact_no = models.IntegerField(verbose_name='Contact No',null=True,blank=True,validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    objects = models.Manager()
    def __str__(self):
        return str(self.Distributor_id)
    class Meta: 
        verbose_name_plural='Distributor'
        db_table='Distributor'

class Products(models.Model):
    Prod_code = models.AutoField(verbose_name='Product Code',primary_key=True)
    Product_name = models.CharField(verbose_name='Product Name',max_length=100)
    Quantity = models.CharField(verbose_name='Quantity(kg/L)',max_length=20)
    Rate = models.FloatField(verbose_name='Rate(per unit)',validators=[nonneg])
    Colour = models.CharField(verbose_name='Colour', max_length=50)
    Product_description = models.CharField(verbose_name='Product Description', max_length=50)
    Stock_level = models.IntegerField(verbose_name='Stock Level',validators=[nonneg])
    Shelf_life = models.IntegerField(verbose_name='Shelf Life',null=True,blank=True,validators=[nonneg])
    objects = models.Manager()
    def __str__(self):
        return str(self.Prod_code)
    class Meta:
        verbose_name_plural='Product'
        db_table='Products'

class Customers(models.Model):
    Customer_id = models.AutoField(verbose_name='Customer ID',primary_key=True)
    Customer_name = models.CharField(verbose_name='Customer Name',max_length=50,validators=[alphanumeric])
    Contact = models.IntegerField(verbose_name='Contact',null=True,blank=True,validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    Address = models.CharField(verbose_name='Address', max_length=50,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.Customer_id)
    class Meta: 
        verbose_name_plural='Customer'
        db_table='Customers'


class Purchase(models.Model):
    Purchase_id = models.AutoField(verbose_name='Purchase ID',primary_key=True)
    Employee_id = models.ForeignKey(Employee, on_delete= models.CASCADE,verbose_name='Employee ID')
    Distributor_id = models.ForeignKey(Distributor, on_delete= models.CASCADE,verbose_name='Distributor ID')
    Date_of_Purchase= models.DateField(verbose_name='Date Of Puchase',validators=[datevalid])
    Discount_in_percentage = models.FloatField(verbose_name='Discount(in percent)',validators=[nonneg,MaxValueValidator(100,'Discount can not be more than 100%%')])
    Tax_in_percentage = models.FloatField(verbose_name='Tax(in percent)',validators=[nonneg])
    Total_amount = models.DecimalField(verbose_name='Total Amount',validators=[nonneg],max_digits=10, decimal_places=2,blank=True,null=True)
    Products=models.ManyToManyField(Products,through='Purchase_Consists_of')
    def save(self, *args, **kwargs):
            total = 0.0 # should be DecimalField not integer or float for prices
            for item in Purchase_Consists_of.objects.filter(Purchase_id=self.Purchase_id):
                for item2 in Products.objects.filter(Prod_code=item.Prod_code_id):
                    total += item.Quantity*item2.Rate
            tax=(total*self.Tax_in_percentage)/100
            total=total+tax
            dis=(total*self.Discount_in_percentage)/100
            total=total-dis
            self.Total_amount = total # again this should be changed to DecimalField
            super(Purchase, self).save(*args, **kwargs)
    objects = models.Manager()
    

    def __str__(self):
        return str(self.Purchase_id)
    class Meta: 
        verbose_name_plural='Purchase'
        db_table='Purchase'

class Sales(models.Model):
    Invoice_no = models.AutoField(verbose_name='Invoice No',primary_key=True)
    Employee_id = models.ForeignKey(Employee, on_delete= models.CASCADE,verbose_name='Employee ID')
    Customer_id = models.ForeignKey(Customers, on_delete= models.CASCADE,verbose_name='Customer ID')
    Date_of_order = models.DateField(verbose_name='Date Of Order',validators=[datevalid])
    Discount_in_percentage = models.FloatField(verbose_name='Discount(in percent)',validators=[nonneg,MaxValueValidator(100,'Discount can not be more than 100%%')])
    Tax_in_percentage = models.FloatField(verbose_name='Tax(in percent)',validators=[nonneg])
    Total_amount = models.DecimalField(verbose_name='Total Amount',validators=[nonneg],max_digits=10, decimal_places=2,blank=True,null=True)
    Mode_of_Payment=models.CharField(verbose_name='Mode Of Payment', max_length=50,choices=mop)
    Products=models.ManyToManyField(Products,through='Sale_Consists_of')
    def save(self, *args, **kwargs):
            total = 0.0 # should be DecimalField not integer or float for prices
            for item in Sale_Consists_of.objects.filter(Invoice_no=self.Invoice_no):
                for item2 in Products.objects.filter(Prod_code=item.Prod_code_id):
                    total += item.Quantity*item2.Rate
            tax=(total*self.Tax_in_percentage)/100
            total=total+tax
            dis=(total*self.Discount_in_percentage)/100
            total=total-dis
            self.Total_amount = total # again this should be changed to DecimalField
            super(Sales, self).save(*args, **kwargs)
    objects = models.Manager()
    def __str__(self):
        return str(self.Invoice_no)
    class Meta: 
        verbose_name_plural='Sales'
        db_table='Sales'


class Office_Expense(models.Model):
    Expenditure_id = models.AutoField(verbose_name='Expenditure ID',primary_key=True)
    Employee_id = models.ForeignKey(Employee, on_delete= models.CASCADE,verbose_name='Employee ID')
    Expenditure_date = models.DateField(verbose_name='Expenditure Date',validators=[datevalid])
    Expense_description = models.CharField(verbose_name='Expense Description',max_length=100)
    Mode_of_payment=models.CharField(verbose_name='Mode Of Payment', max_length=50,choices=mop)
    Amount = models.FloatField(verbose_name='Amount',validators=[nonneg])
    objects = models.Manager()
    def __str__(self):
        return str(self.Expenditure_id)
    class Meta: 
        verbose_name_plural='Office Expense'
        db_table='Office_Expense'

class Transport(models.Model):
    Transport_id = models.AutoField(verbose_name='Transport ID',primary_key=True)
    Transport_name = models.CharField(verbose_name='Transport Name', max_length=50,validators=[alphanumeric])
    Address = models.CharField(verbose_name='Address', max_length=50)
    Contact = models.BigIntegerField(verbose_name='Contact No',validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    Sales=models.ManyToManyField(Sales,through='Delivers')
    objects = models.Manager()
    def __str__(self):
        return str(self.Transport_id)
    class Meta: 
        verbose_name_plural='Transport'
        db_table='Transport'


class Delivers(models.Model):
    Invoice_no = models.ForeignKey(Sales, on_delete= models.CASCADE,verbose_name='Invoice No')
    Transport_id = models.ForeignKey(Transport, on_delete= models.CASCADE,verbose_name='Transport ID')
    Date=models.DateField(verbose_name='Date',validators=[datevalid])
    Place_of_Delivery=models.CharField(verbose_name='Place Of delivery', max_length=50)
    Delivery_status=models.CharField(verbose_name='Delivery Status', max_length=50, choices=DEL_STATUS)
    objects = models.Manager()
    def __str__(self):
        return str(self.Invoice_no)
    class Meta: 
        verbose_name_plural='Delivers'
        db_table='Delivers'
        unique_together=(('Invoice_no'),('Transport_id'),)

class Sale_Consists_of(models.Model):
    Invoice_no = models.ForeignKey(Sales, on_delete= models.CASCADE,verbose_name='Invoice No')
    Prod_code = models.ForeignKey(Products, on_delete= models.CASCADE,verbose_name='Product Code')
    Quantity=models.IntegerField(verbose_name='Quantity')
    objects = models.Manager()
    def __str__(self):
        return str(self.Invoice_no)
    class Meta: 
        verbose_name_plural='Sale Consists of'
        db_table='Sale_Consists_Of'
        unique_together=(('Invoice_no'),('Prod_code'),)

class Purchase_Consists_of(models.Model):
    Purchase_id = models.ForeignKey(Purchase, on_delete= models.CASCADE,verbose_name='Purchase ID',parent_link=True)
    Prod_code = models.ForeignKey(Products, on_delete= models.CASCADE,verbose_name='Product Code',blank=False)
    Quantity=models.IntegerField(verbose_name='Quantity',validators=[nonneg])
    objects = models.Manager()
    def __str__(self):
        return str(self.Purchase_id)
    class Meta: 
        verbose_name_plural='Purchase Consists of'
        db_table='Purchase_Consists_Of'
        unique_together=(('Purchase_id'),('Prod_code'),)
