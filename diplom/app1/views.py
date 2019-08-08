from django.shortcuts import render,redirect
from . import sql_work
import hashlib
# Create your views here.

DATATOV=[]

def pswd(pwd):
    res = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    return res
def index(request):

    return render(request,'index.html')

def showSignUp(request):
    return render(request, 'signup.html')

def showSignIn(request):
    return render(request, 'signin.html')

def SignIn(request):
    name = request.GET['inputName']
    password = request.GET['inputPassword']
    str(name)
    str(password)
    password = pswd(password)
    print(sql_work.check_user_password(name,password))
    dataproducts = sql_work.view_products()
    DATATOV.append(dataproducts)
    context = {"name":name,"tovar":dataproducts }
    if sql_work.check_user_password(name,password)!=[]:
        return render(request, 'shop.html',context)
    else:
        return render(request, 'index.html')
def bsk(request):
    n = sql_work.sizeof_product()
    print(DATATOV)
    print(DATATOV[0][0][2])
    name =request.GET["Customer"]
    for i in range(0,n):
        data=request.GET["btnBsk"+str(i+1)]

        npr=str(DATATOV[0][i][1])
        price = str(DATATOV[0][i][2])

        if data !="0" :
            sql_work.insert_bsk(str(name),str(i+1),str(npr),str(data),str(price))
            sql_work.update_products(str(i+1),str(data))
    zapisi = sql_work.sizeof_bsk_name(name)
    databsk= sql_work.bsk_name_data(name)
    itogprice = sql_work.itog_price(name)
    global NAME
    NAME = name
    context={'size':zapisi,'data':databsk,'itog':itogprice,"name":name}
    return render(request,"bsk.html",context)
def shop(request):
    return render(request, "shop.html")
def ord(request):
    name = NAME
    work = sql_work.bsk_name_data(name)
    for i in work:

        sql_work.ord_registred(i[0],i[1],i[2],i[3],i[4])
    sql_work.clear_bsk(name)
    context={"name":name}
    return render(request, "ord.html",context)

def stylo(request):
    return render(request,"stylo.html")

def SignUp(request):
    name = request.GET['inputName']
    email = request.GET['inputEmail']
    password = request.GET['inputPassword']
    str(password)
    password = pswd(password)
    if sql_work.check_user(name) ==[]:
        sql_work.add_user(name,email,password)
    return render(request, 'index.html')


def com(request):
    comment = request.GET["inputСomment"]
    name = request.GET["Customer"]
    sql_work.add_comment(name,comment)
    data = sql_work.all_comments()
    context={'data':data}
    return render(request,'comments.html',context)