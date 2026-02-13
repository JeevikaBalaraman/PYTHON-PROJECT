# customer=[
#
#   {"CustomerID":"C001","Name":"Arun","Gender":"M","Age":28,"City":"Chennai","JoinDate":"2022-01-10"},
#   {"CustomerID":"C002","Name":"Priya","Gender":"F","Age":28,"City":"Bangalore","JoinDate":"2022-02-15"},
#   {"CustomerID":"C003","Name":"Karthik","Gender":"M","Age":30,"City":"Hyderabad","JoinDate":"2021-06-20"},
#   {"CustomerID":"C004","Name":"Divya","Gender":"F","Age":30,"City":"Chennai","JoinDate":"2021-08-12"},
#   {"CustomerID":"C005","Name":"Ramesh","Gender":"M","Age":32,"City":"Coimbatore","JoinDate":"2020-03-18"},
#   {"CustomerID":"C006","Name":"Anitha","Gender":"F","Age":32,"City":"Madurai","JoinDate":"2020-05-22"},
#   {"CustomerID":"C007","Name":"Vijay","Gender":"M","Age":34,"City":"Salem","JoinDate":"2019-07-14"},
#   {"CustomerID":"C008","Name":"Meena","Gender":"F","Age":34,"City":"Trichy","JoinDate":"2019-09-09"},
#   {"CustomerID":"C009","Name":"Suresh","Gender":"M","Age":36,"City":"Chennai","JoinDate":"2018-11-30"},
#   {"CustomerID":"C010","Name":"Kavya","Gender":"F","Age":36,"City":"Bangalore","JoinDate":"2018-12-25"},
#   {"CustomerID":"C011","Name":"Ajith","Gender":"M","Age":38,"City":"Erode","JoinDate":"2021-01-05"},
#   {"CustomerID":"C012","Name":"Sandhya","Gender":"F","Age":38,"City":"Chennai","JoinDate":"2021-02-16"},
#   {"CustomerID":"C013","Name":"Mohan","Gender":"M","Age":40,"City":"Vellore","JoinDate":"2020-10-10"},
#   {"CustomerID":"C014","Name":"Nisha","Gender":"F","Age":40,"City":"Coimbatore","JoinDate":"2020-11-11"},
#   {"CustomerID":"C015","Name":"Rahul","Gender":"M","Age":28,"City":"Bangalore","JoinDate":"2022-04-17"},
#   {"CustomerID":"C016","Name":"Pooja","Gender":"F","Age":30,"City":"Hyderabad","JoinDate":"2021-01-25"},
#   {"CustomerID":"C017","Name":"Mani","Gender":"M","Age":34,"City":"Salem","JoinDate":"2019-06-06"},
#   {"CustomerID":"C018","Name":"Revathi","Gender":"F","Age":32,"City":"Madurai","JoinDate":"2022-10-10"},
#   {"CustomerID":"C019","Name":"Senthil","Gender":"M","Age":36,"City":"Trichy","JoinDate":"2020-02-20"},
#   {"CustomerID":"C020","Name":"Keerthi","Gender":"F","Age":28,"City":"Chennai","JoinDate":"2023-05-01"}
# ]
# product=[
#
#   {"ProductID":"P001","ProductName":"Laptop","Category":"Electronics","Price":55000},
#   {"ProductID":"P002","ProductName":"Mobile","Category":"Electronics","Price":30000},
#   {"ProductID":"P003","ProductName":"Headphones","Category":"Accessories","Price":2000},
#   {"ProductID":"P004","ProductName":"SmartWatch","Category":"Electronics","Price":8000},
#   {"ProductID":"P005","ProductName":"Keyboard","Category":"Accessories","Price":1500},
#   {"ProductID":"P006","ProductName":"Mouse","Category":"Accessories","Price":800},
#   {"ProductID":"P007","ProductName":"Tablet","Category":"Electronics","Price":25000},
#   {"ProductID":"P008","ProductName":"Monitor","Category":"Electronics","Price":12000},
#   {"ProductID":"P009","ProductName":"Printer","Category":"Electronics","Price":9000},
#   {"ProductID":"P010","ProductName":"Speaker","Category":"Accessories","Price":3500},
#   {"ProductID":"P011","ProductName":"PowerBank","Category":"Accessories","Price":1800},
#   {"ProductID":"P012","ProductName":"Router","Category":"Electronics","Price":2200},
#   {"ProductID":"P013","ProductName":"USBDrive","Category":"Accessories","Price":600},
#   {"ProductID":"P014","ProductName":"HardDisk","Category":"Electronics","Price":4500},
#   {"ProductID":"P015","ProductName":"SSD","Category":"Electronics","Price":6500},
#   {"ProductID":"P016","ProductName":"Camera","Category":"Electronics","Price":40000},
#   {"ProductID":"P017","ProductName":"Tripod","Category":"Accessories","Price":1200},
#   {"ProductID":"P018","ProductName":"Webcam","Category":"Electronics","Price":3000},
#   {"ProductID":"P019","ProductName":"Microphone","Category":"Accessories","Price":2500},
#   {"ProductID":"P020","ProductName":"Charger","Category":"Accessories","Price":1000}
# ]
# order=[
#
#   {"OrderID":"O001","CustomerID":"C001","OrderDate":"2023-06-01","Channel":"Online"},
#   {"OrderID":"O002","CustomerID":"C002","OrderDate":"2023-06-02","Channel":"Offline"},
#   {"OrderID":"O003","CustomerID":"C003","OrderDate":"2023-06-03","Channel":"Online"},
#   {"OrderID":"O004","CustomerID":"C004","OrderDate":"2023-06-04","Channel":"Online"},
#   {"OrderID":"O005","CustomerID":"C005","OrderDate":"2023-06-05","Channel":"Offline"},
#   {"OrderID":"O006","CustomerID":"C006","OrderDate":"2023-06-06","Channel":"Online"},
#   {"OrderID":"O007","CustomerID":"C007","OrderDate":"2023-06-07","Channel":"Offline"},
#   {"OrderID":"O008","CustomerID":"C008","OrderDate":"2023-06-08","Channel":"Online"},
#   {"OrderID":"O009","CustomerID":"C009","OrderDate":"2023-06-09","Channel":"Offline"},
#   {"OrderID":"O010","CustomerID":"C010","OrderDate":"2023-06-10","Channel":"Online"},
#   {"OrderID":"O011","CustomerID":"C011","OrderDate":"2023-07-01","Channel":"Online"},
#   {"OrderID":"O012","CustomerID":"C012","OrderDate":"2023-07-02","Channel":"Offline"},
#   {"OrderID":"O013","CustomerID":"C013","OrderDate":"2023-07-03","Channel":"Online"},
#   {"OrderID":"O014","CustomerID":"C014","OrderDate":"2023-07-04","Channel":"Offline"},
#   {"OrderID":"O015","CustomerID":"C015","OrderDate":"2023-07-05","Channel":"Online"},
#   {"OrderID":"O016","CustomerID":"C016","OrderDate":"2023-07-06","Channel":"Offline"},
#   {"OrderID":"O017","CustomerID":"C017","OrderDate":"2023-07-07","Channel":"Online"},
#   {"OrderID":"O018","CustomerID":"C018","OrderDate":"2023-07-08","Channel":"Offline"},
#   {"OrderID":"O019","CustomerID":"C019","OrderDate":"2023-07-09","Channel":"Online"},
#   {"OrderID":"O020","CustomerID":"C020","OrderDate":"2023-07-10","Channel":"Offline"}
# ]
#
# orderdetails=[
#
#   {"OrderID":"O001","ProductID":"P001","Quantity":1},
#   {"OrderID":"O002","ProductID":"P001","Quantity":2},
#   {"OrderID":"O003","ProductID":"P002","Quantity":1},
#   {"OrderID":"O004","ProductID":"P002","Quantity":1},
#   {"OrderID":"O005","ProductID":"P003","Quantity":3},
#   {"OrderID":"O006","ProductID":"P003","Quantity":2},
#   {"OrderID":"O007","ProductID":"P004","Quantity":1},
#   {"OrderID":"O008","ProductID":"P004","Quantity":2},
#   {"OrderID":"O009","ProductID":"P005","Quantity":4},
#   {"OrderID":"O010","ProductID":"P005","Quantity":1},
#   {"OrderID":"O011","ProductID":"P001","Quantity":1},
#   {"OrderID":"O012","ProductID":"P002","Quantity":2},
#   {"OrderID":"O013","ProductID":"P003","Quantity":3},
#   {"OrderID":"O014","ProductID":"P004","Quantity":1},
#   {"OrderID":"O015","ProductID":"P001","Quantity":2},
#   {"OrderID":"O016","ProductID":"P002","Quantity":1},
#   {"OrderID":"O017","ProductID":"P003","Quantity":2},
#   {"OrderID":"O018","ProductID":"P004","Quantity":1},
#   {"OrderID":"O019","ProductID":"P005","Quantity":3},
#   {"OrderID":"O020","ProductID":"P001","Quantity":1}
# ]
# payments=[
#
#   {"OrderID":"O001","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O002","PaymentMode":"Card","PaymentStatus":"Success"},
#   {"OrderID":"O003","PaymentMode":"Cash","PaymentStatus":"Pending"},
#   {"OrderID":"O004","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O005","PaymentMode":"Card","PaymentStatus":"Success"},
#   {"OrderID":"O006","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O007","PaymentMode":"Cash","PaymentStatus":"Failed"},
#   {"OrderID":"O008","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O009","PaymentMode":"Card","PaymentStatus":"Success"},
#   {"OrderID":"O010","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O011","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O012","PaymentMode":"Cash","PaymentStatus":"Success"},
#   {"OrderID":"O013","PaymentMode":"Card","PaymentStatus":"Pending"},
#   {"OrderID":"O014","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O015","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O016","PaymentMode":"Cash","PaymentStatus":"Failed"},
#   {"OrderID":"O017","PaymentMode":"Card","PaymentStatus":"Success"},
#   {"OrderID":"O018","PaymentMode":"UPI","PaymentStatus":"Success"},
#   {"OrderID":"O019","PaymentMode":"Cash","PaymentStatus":"Success"},
#   {"OrderID":"O020","PaymentMode":"Card","PaymentStatus":"Success"}
# ]
# shipping=[
#
#   {"OrderID":"O001","ShippingType":"Standard","DeliveryDays":5},
#   {"OrderID":"O002","ShippingType":"Express","DeliveryDays":2},
#   {"OrderID":"O003","ShippingType":"Standard","DeliveryDays":6},
#   {"OrderID":"O004","ShippingType":"Express","DeliveryDays":3},
#   {"OrderID":"O005","ShippingType":"Standard","DeliveryDays":5},
#   {"OrderID":"O006","ShippingType":"Express","DeliveryDays":2},
#   {"OrderID":"O007","ShippingType":"Standard","DeliveryDays":6},
#   {"OrderID":"O008","ShippingType":"Express","DeliveryDays":3},
#   {"OrderID":"O009","ShippingType":"Standard","DeliveryDays":5},
#   {"OrderID":"O010","ShippingType":"Express","DeliveryDays":2},
#   {"OrderID":"O011","ShippingType":"Standard","DeliveryDays":4},
#   {"OrderID":"O012","ShippingType":"Express","DeliveryDays":2},
#   {"OrderID":"O013","ShippingType":"Standard","DeliveryDays":6},
#   {"OrderID":"O014","ShippingType":"Express","DeliveryDays":3},
#   {"OrderID":"O015","ShippingType":"Standard","DeliveryDays":5},
#   {"OrderID":"O016","ShippingType":"Express","DeliveryDays":2},
#   {"OrderID":"O017","ShippingType":"Standard","DeliveryDays":4},
#   {"OrderID":"O018","ShippingType":"Express","DeliveryDays":3},
#   {"OrderID":"O019","ShippingType":"Standard","DeliveryDays":5},
#   {"OrderID":"O020","ShippingType":"Express","DeliveryDays":2}
# ]
# returns=[
#
#   {"OrderID":"O003","ReturnStatus":"Yes","Reason":"Damaged"},
#   {"OrderID":"O007","ReturnStatus":"Yes","Reason":"Wrong Item"},
#   {"OrderID":"O013","ReturnStatus":"Yes","Reason":"Late Delivery"},
#   {"OrderID":"O016","ReturnStatus":"Yes","Reason":"Payment Failed"}
# ]


Customers= [

    {"CustomerID":"C001","Name":"Arun","Gender":"M","Age":28,"City":"Chennai","JoinDate":"2022-01-10"},
    {"CustomerID":"C002","Name":"Priya","Gender":"F","Age":32,"City":"Bangalore","JoinDate":"2021-11-22"},
    {"CustomerID":"C003","Name":"Karthik","Gender":"M","Age":35,"City":"Hyderabad","JoinDate":"2020-05-18"},
    {"CustomerID":"C004","Name":"Divya","Gender":"F","Age":26,"City":"Chennai","JoinDate":"2023-02-12"},
    {"CustomerID":"C005","Name":"Ramesh","Gender":"M","Age":40,"City":"Coimbatore","JoinDate":"2019-07-30"},
    {"CustomerID":"C006","Name":"Anitha","Gender":"F","Age":29,"City":"Madurai","JoinDate":"2022-09-05"},
    {"CustomerID":"C007","Name":"Vijay","Gender":"M","Age":34,"City":"Salem","JoinDate":"2021-06-21"},
    {"CustomerID":"C008","Name":"Meena","Gender":"F","Age":31,"City":"Trichy","JoinDate":"2020-10-11"},
    {"CustomerID":"C009","Name":"Suresh","Gender":"M","Age":45,"City":"Chennai","JoinDate":"2018-03-14"},
    {"CustomerID":"C010","Name":"Kavya","Gender":"F","Age":27,"City":"Bangalore","JoinDate":"2023-01-01"},
    {"CustomerID":"C011","Name":"Ajith","Gender":"M","Age":36,"City":"Erode","JoinDate":"2021-08-08"},
    {"CustomerID":"C012","Name":"Sandhya","Gender":"F","Age":33,"City":"Chennai","JoinDate":"2020-12-19"},
    {"CustomerID":"C013","Name":"Mohan","Gender":"M","Age":38,"City":"Vellore","JoinDate":"2019-09-09"},
    {"CustomerID":"C014","Name":"Nisha","Gender":"F","Age":24,"City":"Coimbatore","JoinDate":"2023-03-15"},
    {"CustomerID":"C015","Name":"Rahul","Gender":"M","Age":29,"City":"Bangalore","JoinDate":"2022-04-17"},
    {"CustomerID":"C016","Name":"Pooja","Gender":"F","Age":35,"City":"Hyderabad","JoinDate":"2021-01-25"},
    {"CustomerID":"C017","Name":"Mani","Gender":"M","Age":41,"City":"Salem","JoinDate":"2019-06-06"},
    {"CustomerID":"C018","Name":"Revathi","Gender":"F","Age":30,"City":"Madurai","JoinDate":"2022-10-10"},
    {"CustomerID":"C019","Name":"Senthil","Gender":"M","Age":37,"City":"Trichy","JoinDate":"2020-02-20"},
    {"CustomerID":"C020","Name":"Keerthi","Gender":"F","Age":26,"City":"Chennai","JoinDate":"2023-05-01"}
  ]

Products= [

    {"ProductID":"P001","ProductName":"Laptop","Category":"Electronics","Price":55000},
    {"ProductID":"P002","ProductName":"Mobile","Category":"Electronics","Price":30000},
    {"ProductID":"P003","ProductName":"Headphones","Category":"Accessories","Price":2000},
    {"ProductID":"P004","ProductName":"Smart Watch","Category":"Electronics","Price":8000},
    {"ProductID":"P005","ProductName":"Keyboard","Category":"Accessories","Price":1500},
    {"ProductID":"P006","ProductName":"Mouse","Category":"Accessories","Price":800},
    {"ProductID":"P007","ProductName":"Tablet","Category":"Electronics","Price":25000},
    {"ProductID":"P008","ProductName":"Monitor","Category":"Electronics","Price":12000},
    {"ProductID":"P009","ProductName":"Printer","Category":"Electronics","Price":9000},
    {"ProductID":"P010","ProductName":"Speaker","Category":"Accessories","Price":3500},
    {"ProductID":"P011","ProductName":"Power Bank","Category":"Accessories","Price":1800},
    {"ProductID":"P012","ProductName":"Router","Category":"Electronics","Price":2200},
    {"ProductID":"P013","ProductName":"USB Drive","Category":"Accessories","Price":600},
    {"ProductID":"P014","ProductName":"Hard Disk","Category":"Electronics","Price":4500},
    {"ProductID":"P015","ProductName":"SSD","Category":"Electronics","Price":6500},
    {"ProductID":"P016","ProductName":"Camera","Category":"Electronics","Price":40000},
    {"ProductID":"P017","ProductName":"Tripod","Category":"Accessories","Price":1200},
    {"ProductID":"P018","ProductName":"Webcam","Category":"Electronics","Price":3000},
    {"ProductID":"P019","ProductName":"Microphone","Category":"Accessories","Price":2500},
    {"ProductID":"P020","ProductName":"Charger","Category":"Accessories","Price":1000}
  ]

Orders= [

    {"OrderID":"O001","CustomerID":"C001","OrderDate":"2023-06-01","Channel":"Online"},
    {"OrderID":"O002","CustomerID":"C002","OrderDate":"2023-06-01","Channel":"Offline"},
    {"OrderID":"O003","CustomerID":"C003","OrderDate":"2023-06-01","Channel":"Online"},
    {"OrderID":"O004","CustomerID":"C004","OrderDate":"2023-06-07","Channel":"Online"},
    {"OrderID":"O005","CustomerID":"C005","OrderDate":"2023-06-10","Channel":"Offline"},
    {"OrderID":"O006","CustomerID":"C006","OrderDate":"2023-06-12","Channel":"Online"},
    {"OrderID":"O007","CustomerID":"C007","OrderDate":"2023-06-14","Channel":"Offline"},
    {"OrderID":"O008","CustomerID":"C008","OrderDate":"2023-06-15","Channel":"Online"},
    {"OrderID":"O009","CustomerID":"C009","OrderDate":"2023-06-17","Channel":"Offline"},
    {"OrderID":"O010","CustomerID":"C010","OrderDate":"2023-06-18","Channel":"Online"},
    {"OrderID":"O011","CustomerID":"C011","OrderDate":"2023-06-20","Channel":"Online"},
    {"OrderID":"O012","CustomerID":"C012","OrderDate":"2023-06-21","Channel":"Offline"},
    {"OrderID":"O013","CustomerID":"C013","OrderDate":"2023-06-22","Channel":"Online"},
    {"OrderID":"O014","CustomerID":"C014","OrderDate":"2023-06-23","Channel":"Offline"},
    {"OrderID":"O015","CustomerID":"C015","OrderDate":"2023-06-24","Channel":"Online"},
    {"OrderID":"O016","CustomerID":"C016","OrderDate":"2023-06-25","Channel":"Offline"},
    {"OrderID":"O017","CustomerID":"C017","OrderDate":"2023-06-26","Channel":"Online"},
    {"OrderID":"O018","CustomerID":"C018","OrderDate":"2023-06-27","Channel":"Offline"},
    {"OrderID":"O019","CustomerID":"C019","OrderDate":"2023-06-28","Channel":"Online"},
    {"OrderID":"O020","CustomerID":"C020","OrderDate":"2023-06-29","Channel":"Offline"}
  ]

OrderDetails= [

    {"OrderID":"O001","ProductID":"P001","Quantity":1},
    {"OrderID":"O002","ProductID":"P002","Quantity":2},
    {"OrderID":"O003","ProductID":"P003","Quantity":3},
    {"OrderID":"O004","ProductID":"P004","Quantity":1},
    {"OrderID":"O005","ProductID":"P005","Quantity":4},
    {"OrderID":"O006","ProductID":"P006","Quantity":2},
    {"OrderID":"O007","ProductID":"P007","Quantity":1},
    {"OrderID":"O008","ProductID":"P008","Quantity":1},
    {"OrderID":"O009","ProductID":"P009","Quantity":2},
    {"OrderID":"O010","ProductID":"P010","Quantity":3},
    {"OrderID":"O011","ProductID":"P011","Quantity":2},
    {"OrderID":"O012","ProductID":"P012","Quantity":1},
    {"OrderID":"O013","ProductID":"P013","Quantity":5},
    {"OrderID":"O014","ProductID":"P014","Quantity":1},
    {"OrderID":"O015","ProductID":"P015","Quantity":2},
    {"OrderID":"O016","ProductID":"P016","Quantity":1},
    {"OrderID":"O017","ProductID":"P017","Quantity":3},
    {"OrderID":"O018","ProductID":"P018","Quantity":2},
    {"OrderID":"O019","ProductID":"P019","Quantity":2},
    {"OrderID":"O020","ProductID":"P020","Quantity":4}
  ]

Payments=[

    {"OrderID":"O001","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O002","PaymentMode":"Card","PaymentStatus":"Success"},
    {"OrderID":"O003","PaymentMode":"Cash","PaymentStatus":"Pending"},
    {"OrderID":"O004","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O005","PaymentMode":"Card","PaymentStatus":"Success"},
    {"OrderID":"O006","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O007","PaymentMode":"Cash","PaymentStatus":"Failed"},
    {"OrderID":"O008","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O009","PaymentMode":"Card","PaymentStatus":"Success"},
    {"OrderID":"O010","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O011","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O012","PaymentMode":"Cash","PaymentStatus":"Success"},
    {"OrderID":"O013","PaymentMode":"Card","PaymentStatus":"Pending"},
    {"OrderID":"O014","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O015","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O016","PaymentMode":"Cash","PaymentStatus":"Failed"},
    {"OrderID":"O017","PaymentMode":"Card","PaymentStatus":"Success"},
    {"OrderID":"O018","PaymentMode":"UPI","PaymentStatus":"Success"},
    {"OrderID":"O019","PaymentMode":"Cash","PaymentStatus":"Success"},
    {"OrderID":"O020","PaymentMode":"Card","PaymentStatus":"Success"}
  ]

Shipping= [

    {"OrderID":"O001","ShippingType":"Standard","DeliveryDays":5},
    {"OrderID":"O002","ShippingType":"Express","DeliveryDays":2},
    {"OrderID":"O003","ShippingType":"Standard","DeliveryDays":6},
    {"OrderID":"O004","ShippingType":"Express","DeliveryDays":3},
    {"OrderID":"O005","ShippingType":"Standard","DeliveryDays":5},
    {"OrderID":"O006","ShippingType":"Express","DeliveryDays":2},
    {"OrderID":"O007","ShippingType":"Standard","DeliveryDays":6},
    {"OrderID":"O008","ShippingType":"Express","DeliveryDays":3},
    {"OrderID":"O009","ShippingType":"Standard","DeliveryDays":5},
    {"OrderID":"O010","ShippingType":"Express","DeliveryDays":2},
    {"OrderID":"O011","ShippingType":"Standard","DeliveryDays":4},
    {"OrderID":"O012","ShippingType":"Express","DeliveryDays":2},
    {"OrderID":"O013","ShippingType":"Standard","DeliveryDays":6},
    {"OrderID":"O014","ShippingType":"Express","DeliveryDays":3},
    {"OrderID":"O015","ShippingType":"Standard","DeliveryDays":5},
    {"OrderID":"O016","ShippingType":"Express","DeliveryDays":2},
    {"OrderID":"O017","ShippingType":"Standard","DeliveryDays":4},
    {"OrderID":"O018","ShippingType":"Express","DeliveryDays":3},
    {"OrderID":"O019","ShippingType":"Standard","DeliveryDays":5},
    {"OrderID":"O020","ShippingType":"Express","DeliveryDays":2}
  ]

Returns= [

    {"OrderID":"O003","ReturnStatus":"Yes","Reason":"Damaged"},
    {"OrderID":"O007","ReturnStatus":"Yes","Reason":"Wrong Item"},
    {"OrderID":"O013","ReturnStatus":"Yes","Reason":"Late Delivery"},
    {"OrderID":"O016","ReturnStatus":"Yes","Reason":"Payment Failed"}
  ]
#
import pandas as pd
a=pd.DataFrame(Customers)
b=pd.DataFrame(Products)
c=pd.DataFrame(Orders)
d=pd.DataFrame(OrderDetails)
e=pd.DataFrame(Payments)
f=pd.DataFrame(Shipping)
g=pd.DataFrame(Returns)
print(a,b,c,d,e,f,g)
# CUSTERMERS ANALYSE
ab=a[a["Gender"]=="F"].groupby("City").size()
print(ab)
print("--------------------------------------------------\n")
ba=a[a["Age"]>=24].groupby("Gender").size()
print(ba)
print("___________________________________________________\n")
gh=a[a["Age"]>=35]
print(gh)
print("-----------------------------------------------------\n")
m=(a[a["Gender"]=="M"].groupby(["Age","Gender"]).size(),a[a["Gender"]=="F"].groupby(["Age","Gender"]).size())
print(m)
print("___________________________________________________\n")
f = a[(a["Gender"]=="F")&(a["Age"]>=35)].groupby(["City","Gender","Age"]).size()
print(f)
print("___________________________________________________\n")
jee=pd.merge(b,d,how="outer",on="ProductID")
print(jee.groupby("ProductName")["Price"].max().sort_values(ascending=False))
print("___________________________________________________\n")
print(jee.groupby("ProductName")["Price"].max().sort_values(ascending=False).head(5))
print("___________________________________________________\n")
print(a.groupby("City")["CustomerID"].count().sort_values(ascending=False).head(1))
print("____________________________________________________\n")
print(a.groupby("Gender")["Age"].mean())
print("____________________________________________________\n")
s=(a[a["Age"]>=35].groupby("Gender").size())
print(s)
print("____________________________________________________\n")
fg=a.groupby("City")["Age"].mean().head(1)
print(fg)
print("____________________________________________________\n")
ca=a[a["JoinDate"]>"2022-10-10"]
print(ca)
print("____________________________________________________\n")
hj=a.groupby("City")["Age"].max().sort_values(ascending=False).head(5)
print(hj)
print("____________________________________________________\n")
hk=pd.merge(c,d,how="outer",on="OrderID")
io=hk["OrderID"].count()
print(io)
print("____________________________________________________\n")
ui=c["Channel"].value_counts()
print(ui)
print("____________________________________________________\n")
io=pd.merge(a,c,on="CustomerID")
po=io.groupby("CustomerID")["OrderID"].count()
print(po)
print("____________________________________________________\n")
uo=c.groupby("OrderDate")["OrderID"].count().head(1)
print(uo)
print("____________________________________________________\n")
hk=pd.merge(c,d,how="outer",on="OrderID")
jk=hk.groupby("CustomerID")["Quantity"].sum()
print(jk)
print("____________________________________________________\n")
hj=a[a["CustomerID"]>1]
print(hj)
# aa=pd.merge(a,c,on="CustomerID")
# bb=pd.merge(aa,d,on="OrderID")
# cc=pd.merge(bb,b,on="ProductID")
# dd=pd.merge(cc,e,on="OrderID")
# ee=pd.merge(dd,f,on="OrderID")
# ff=pd.merge(ee,g,on="OrderID")
# print(ff)
# print (ff.columns)