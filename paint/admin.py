from django.contrib import admin
from totalsum.admin import TotalsumAdmin
from .models import Employee, Distributor, Products, Customers, Purchase, Sales, Office_Expense, Transport, Delivers, Sale_Consists_of, Purchase_Consists_of

admin.site.site_header = "Amruta Threads"
admin.site.index_title = "Amruta Threads Administration"

def make_published(modeladmin, request, queryset):
        queryset.update(Delivery_status='DELIVERED')
make_published.short_description = "Mark selected as Delivered"


#admin.site.register(Employee)
#admin.site.register(Distributor)
#admin.site.register(Products)
#admin.site.register(Customers)
#admin.site.register(Purchase)
#admin.site.register(Sales)
#admin.site.register(Office_Expense)
#admin.site.register(Transport)
#admin.site.register(Delivers)
#admin.site.register(Sale_Consists_of)
#admin.site.register(Purchase_Consists_of)
class Sales_Consists_OfInline(admin.TabularInline):
    model = Sale_Consists_of
    min_num=1

class Purchase_Consists_OfInline(admin.TabularInline):
    model = Purchase_Consists_of
    min_num=1

class DeliversInline(admin.TabularInline):
    model = Delivers
  
class SalesInline(admin.TabularInline):
    model = Customers

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( 'Employee_id','Employee_firstname','Employee_lastname','Address','Job_description' ,'salary','Bank_name','Bank_branch' ,'Bank_Accno','Email_id','Phone_no','Education_level' ,'Date_of_joining')
class DistributorAdmin(admin.ModelAdmin):
    list_display = ( 'Distributor_id' ,'Distributor_name','GSTIN','Address', 'Email_id', 'Contact_no')
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('Prod_code','Product_name','Quantity','Rate','Colour','Product_description','Stock_level','Shelf_life')
    list_filter = ('Shelf_life','Stock_level','Rate')    
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Customer_id','Customer_name','Contact','Address')
    
      
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('Purchase_id','Employee_id','Distributor_id','Date_of_Purchase','Discount_in_percentage','Tax_in_percentage','Total_amount')
    inlines=[Purchase_Consists_OfInline]
    list_filter = ('Date_of_Purchase','Discount_in_percentage','Tax_in_percentage','Total_amount')    
class SalesAdmin(admin.ModelAdmin):
    list_display = ('Invoice_no','Employee_id','Customer_id','Date_of_order','Discount_in_percentage','Tax_in_percentage','Total_amount','Mode_of_Payment')
    inlines=[Sales_Consists_OfInline,DeliversInline]
    list_filter = ('Date_of_order','Mode_of_Payment','Tax_in_percentage')      

class Office_ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Expenditure_id','Employee_id','Expenditure_date','Expense_description','Mode_of_payment','Amount')
    list_filter = ('Expenditure_date','Mode_of_payment','Expense_description')     
class TransportAdmin(admin.ModelAdmin):
    list_display = ( 'Transport_id','Transport_name','Address' ,'Contact')
        
class DeliversAdmin(admin.ModelAdmin):
    list_display = ( 'Invoice_no','Transport_id','Date','Place_of_Delivery','Delivery_status')
    list_filter = ('Date','Delivery_status')    
    actions = [make_published]
class Sales_consits_ofAdmin(admin.ModelAdmin):
    list_display = ('Invoice_no','Prod_code','Quantity')
        
class Purchase_Consisits_ofAdmin(admin.ModelAdmin):
    list_display = ('Purchase_id','Prod_code','Quantity')


        

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Customers,CustomersAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Sales,SalesAdmin)
admin.site.register(Office_Expense,Office_ExpenseAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Delivers,DeliversAdmin)
admin.site.register(Sale_Consists_of,Sales_consits_ofAdmin)
admin.site.register(Purchase_Consists_of,Purchase_Consisits_ofAdmin)

