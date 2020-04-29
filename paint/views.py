from django.shortcuts import render
from .forms import SearchCustomerForm, SearchDistributorForm, SearchProductForm
from django.http import HttpResponse, request
from .models import Customers, Sale_Consists_of, Sales, Delivers, Distributor, Products, Purchase, Sales, Office_Expense
import sqlite3
from django.http import JsonResponse


def home(request):
    return render(request,'index.htm')

def analysis(request):
    return render(request, 'Analysis.htm')

def newrecord(request):
    return render(request, 'NewRecords.htm')

def shoprecord(request):
    return render(request, 'Shoprecords.htm')

def chartj(request):
    return render(request, 'purchasechart.htm')

def chartjy(request):
    return render(request, 'purchasecharty.htm')

def charts(request):
    return render(request, 'salechart.htm')

def chartsy(request):
    return render(request,'salechartyearly.htm')

def chartoe(request):
    return render(request, 'oechart.htm')

def chartoey(request):
    return render(request, 'oecharty.htm')

def chartpl(request):
    return render(request, 'plchart.htm')

def chartply(request):
    return render(request, 'plcharty.htm')

def search_customer(request):
    if request.method == "POST":
        form=SearchCustomerForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('customer_name')
            phone=form.cleaned_data.get('phone')
        name='%'+name+'%'
        phone='%'+phone+'%'
        q = Customers.objects.raw('SELECT * FROM Customers WHERE Contact like %s and Customer_name like %s',[phone,name])
        
        context = {'customer': q}
        return render(request, 'customerdetails.htm', context)


    else:  
        q2= Customers.objects.raw('SELECT * FROM Customers')  
        form = SearchCustomerForm()
    return render(request, 'searchc.htm', {'form': form ,'cust':q2})

def search_Distributor(request):
    if request.method == "POST":
        form=SearchDistributorForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('Distributor_name')
            phone=form.cleaned_data.get('phone')
        name='%'+name+'%'
        phone='%'+phone+'%'
        q = Distributor.objects.raw('SELECT * FROM Distributor WHERE Contact_no like %s and Distributor_name like %s',[phone,name])
       
        context = {'distributor': q}
        return render(request, 'disdetails.htm', context)


    else:  
        q2=Distributor.objects.raw('SELECT * FROM Distributor')  
        form = SearchDistributorForm()
    return render(request, 'searchd.htm', {'form': form,'dist':q2})

def search_product(request):
    if request.method == "POST":
        form=SearchProductForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('product_name')
        name='%'+name+'%'
        q = Products.objects.raw('SELECT * FROM Products WHERE Product_name like %s',[name])
       
        context = {'product': q}
        return render(request, 'prodetails.htm', context)


    else: 
        q2 = Products.objects.raw('SELECT * FROM Products')   
        form = SearchProductForm()
    return render(request, 'searchp.htm', {'form': form,'prod':q2})

def track_delivery(request):
    q2=Customers.objects.raw('SELECT C.Customer_id, C.Customer_name, S.Total_amount, S.Date_of_order, S.Invoice_no, SC.Delivery_status from Customers as C, Sales as S, Delivers as SC where C.Customer_id=S.Customer_id_id and S.Invoice_no=SC.Invoice_no_id and SC.Delivery_status = "NOT DELIVERED"')
    context = {'del': q2}
    return render(request, 'deldetails.htm', context)

def purchasechart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,7) as "Month", sum(Total_amount) as Amount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def purchasechartyear(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,4) as "Month", sum(Total_amount) as Amount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,4)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def salechart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_order,1,7) as "Month", sum(Total_amount) as Amount, Invoice_no from Sales group by substr(Date_of_order,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def salechartyear(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_order,1,4) as "Year", sum(Total_amount) as Amount, Invoice_no from Sales group by substr(Date_of_order,1,4)')
    
    Year=[]
    Amount=[]
    for key in c.fetchall():
      Year.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Year,

        'data': Amount,
    })

def oechart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT substr(Expenditure_date,1,7) as "Month", sum(Amount) as Amount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def oecharty(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT substr(Expenditure_date,1,4) as "Month", sum(Amount) as Amount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,4)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def profitchart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,7) as "Month", sum(Total_amount) as PAmount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,7)') 
    Month=[]
    PAmount=[]
    for key in c.fetchall():
        Month.append(key[0])
        PAmount.append(key[1])
    
   
    c.execute('SELECT  substr(Date_of_order,1,7) as "SMonth", sum(Total_amount) as SAmount, Invoice_no from Sales group by substr(Date_of_order,1,7)')
    SMonth=[]
    SAmount=[]
    for key in c.fetchall():
        SMonth.append(key[0])
        SAmount.append(key[1])
    c.execute('SELECT substr(Expenditure_date,1,7) as "OMonth", sum(Amount) as OEAmount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,7)')
    OEAmount=[]
    for key in c.fetchall():
        OEAmount.append(key[1])
   
    res_list = [] 
    for i in range(0, 4):
        res_list.append(SAmount[i]-(PAmount[i] + OEAmount[i]))
    
    
    return JsonResponse(data={
        'labels': Month,

        'dataa': res_list,
        
    })

def profitcharty(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,4) as "Month", sum(Total_amount) as PAmount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,4)') 
    Month=[]
    PAmount=[]
    for key in c.fetchall():
        Month.append(key[0])
        PAmount.append(key[1])
    
   
    c.execute('SELECT  substr(Date_of_order,1,4) as "SMonth", sum(Total_amount) as SAmount, Invoice_no from Sales group by substr(Date_of_order,1,4)')
    SMonth=[]
    SAmount=[]
    for key in c.fetchall():
        SMonth.append(key[0])
        SAmount.append(key[1])
    c.execute('SELECT substr(Expenditure_date,1,4) as "OMonth", sum(Amount) as OEAmount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,4)')
    OEAmount=[]
    for key in c.fetchall():
        OEAmount.append(key[1])
   
    res_list = [] 
    for i in range(0, len(SAmount)):
        res_list.append(SAmount[i]-(PAmount[i] + OEAmount[i]))
    
    
    return JsonResponse(data={
        'labels': Month,

        'dataa': res_list,
        
    })

def salechartcrm(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_order,1,7) as "Month", sum(Total_amount) as Amount, Invoice_no from Sales group by substr(Date_of_order,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
          Month.append(key[0])
          Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total sales in %s is less than the sales in %s by a margin of Rs. %d . There is a %.2f%% decline in sales" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total sales in %s is more than the sales in %s by a margin of Rs. %d . There is a %.2f%% increase in sales" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total sales in %s is equal to the sales in %s. There is no change in sales" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def salechartcry(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_order,1,4) as "Month", sum(Total_amount) as Amount, Invoice_no from Sales group by substr(Date_of_order,1,4)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
          Month.append(key[0])
          Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total sales in %s is less than the sales in %s by a margin of Rs. %d . There is a %.2f%% decline in sales" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total sales in %s is more than the sales in %s by a margin of Rs. %d . There is a %.2f%% increase in sales" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total sales in %s is equal to the sales in %s. There is no change in sales" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def purchasechartcrm(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,7) as "Month", sum(Total_amount) as Amount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total purchases in %s is less than the purchases in %s by a margin of Rs. %d . There is a %.2f%% decline in purchases" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total purchases in %s is more than the purchases in %s by a margin of Rs. %d . There is a %.2f%% increase in purchases" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total purchases in %s is equal to the purchases in %s. There is no change in purchases" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def purchasechartcry(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,4) as "Month", sum(Total_amount) as Amount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,4)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total purchases in %s is less than the purchases in %s by a margin of Rs. %d . There is a %.2f%% decline in purchases" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total purchases in %s is more than the purchases in %s by a margin of Rs. %d . There is a %.2f%% increase in purchases" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total purchases in %s is equal to the purchases in %s. There is no change in purchases" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def oechartcrm(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT substr(Expenditure_date,1,7) as "Month", sum(Amount) as Amount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total Office Expenses in %s is less than the Office Expenses in %s by a margin of Rs. %d . There is a %.2f%% decline in Office Expenses" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total Office Expenses in %s is more than the Office Expenses in %s by a margin of Rs. %d . There is a %.2f%% increase in Office Expenses" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total Office Expenses in %s is equal to the Office Expenses in %s. There is no change in Office Expenses" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def oechartcry(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT substr(Expenditure_date,1,4) as "Month", sum(Amount) as Amount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,4)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    if(Amount[len(Amount)-1]<Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-2]-Amount[len(Amount)-1]
        per=(mar/Amount[len(Amount)-2])*100
        s=("The total Office Expenses in %s is less than the Office Expenses in %s by a margin of Rs. %d . There is a %.2f%% decline in Office Expenses" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(Amount[len(Amount)-1]>Amount[len(Amount)-2]):
        mar=Amount[len(Amount)-1]-Amount[len(Amount)-2]
        per=(mar/Amount[len(Amount)-1])*100
        s=("The total Office Expenses in %s is more than the Office Expenses in %s by a margin of Rs. %d . There is a %.2f%% increase in Office Expenses" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total Office Expenses in %s is equal to the Office Expenses in %s. There is no change in Office expenses" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})

def profitchartcrm(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,7) as "Month", sum(Total_amount) as PAmount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,7)') 
    Month=[]
    PAmount=[]
    for key in c.fetchall():
        Month.append(key[0])
        PAmount.append(key[1])
    
    c.execute('SELECT  substr(Date_of_order,1,7) as "SMonth", sum(Total_amount) as SAmount, Invoice_no from Sales group by substr(Date_of_order,1,7)')
    SMonth=[]
    SAmount=[]
    for key in c.fetchall():
        SMonth.append(key[0])
        SAmount.append(key[1])
    c.execute('SELECT substr(Expenditure_date,1,7) as "OMonth", sum(Amount) as OEAmount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,7)')
    OEAmount=[]
    for key in c.fetchall():
        OEAmount.append(key[1])
   
    res_list = [] 
    for i in range(0, len(SAmount)):
        res_list.append(SAmount[i]-(PAmount[i] + OEAmount[i]))
    
    if(res_list[len(res_list)-1]<res_list[len(res_list)-2]):
        mar=abs(res_list[len(res_list)-2]-res_list[len(res_list)-1])
        per=abs((mar/res_list[len(res_list)-2])*100)
        s=("The total Revenue in %s is less than the Revenue in %s by a margin of Rs. %d . There is a %.2f%% decline in Revenue. The shop is in loss" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(res_list[len(res_list)-1]>res_list[len(res_list)-2]):
        mar=abs(res_list[len(res_list)-1]-res_list[len(res_list)-2])
        per=abs((mar/res_list[len(res_list)-1])*100)
        s=("The total Revenue in %s is more than the Revenue in %s by a margin of Rs. %d . There is a %.2f%% increase in Revenue. The shop is in gain" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total Revenue in %s is equal to the Revenue in %s. There is no change in Revenue" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})
    
def profitchartcry(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(Date_of_Purchase,1,4) as "Month", sum(Total_amount) as PAmount, Purchase_id from Purchase group by substr(Date_of_Purchase,1,4)') 
    Month=[]
    PAmount=[]
    for key in c.fetchall():
        Month.append(key[0])
        PAmount.append(key[1])
    
   
    c.execute('SELECT  substr(Date_of_order,1,4) as "SMonth", sum(Total_amount) as SAmount, Invoice_no from Sales group by substr(Date_of_order,1,4)')
    SMonth=[]
    SAmount=[]
    for key in c.fetchall():
        SMonth.append(key[0])
        SAmount.append(key[1])
    c.execute('SELECT substr(Expenditure_date,1,4) as "OMonth", sum(Amount) as OEAmount, Expenditure_id from Office_Expense group by substr(Expenditure_date,1,4)')
    OEAmount=[]
    for key in c.fetchall():
        OEAmount.append(key[1])
   
    res_list = [] 
    for i in range(0, len(SAmount)):
        res_list.append(SAmount[i]-(PAmount[i] + OEAmount[i]))
    
    if(res_list[len(res_list)-1]<res_list[len(res_list)-2]):
        mar=abs(res_list[len(res_list)-2]-res_list[len(res_list)-1])
        per=abs((mar/res_list[len(res_list)-2])*100)
        s=("The total Revenue in %s is less than the Revenue in %s by a margin of Rs. %d . There is a %.2f%% decline in Revenue. The shop is in loss" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    elif(res_list[len(res_list)-1]>res_list[len(res_list)-2]):
        mar=abs(res_list[len(res_list)-1]-res_list[len(res_list)-2])
        per=abs((mar/res_list[len(res_list)-1])*100)
        s=("The total Revenue in %s is more than the Revenue in %s by a margin of Rs. %d . There is a %.2f%% increase in Revenue. The shop is in gain" % (Month[len(Month)-1],Month[len(Month)-2],mar,per))

    else:
         s=("The total Revenue in %s is equal to the Revenue in %s. There is no change in Revenue" % (Month[len(Month)-1],Month[len(Month)-2]))
    return render(request, 'test.htm', {'str':s})       
    