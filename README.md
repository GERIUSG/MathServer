# Ex.05 Design a Website for Server Side Processing
## Date:03/12/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<html>
<head>
    <title>LAMP FILAMENT POWER CALCULATOR</title>
    <style>
        body  {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        #powerform {
        display: inline-block;
        border: BLUE;
        width: 600px;
        min-height: 400px;
        font-size: 20px;
 
       }
        .container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid green;
            border-radius: 10px;
            margin-bottom: 200px;
            background-color: teal;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    
        label {
            display: block;
            margin-top: 10px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: rgb(239, 243, 22);
            color: rgb(16, 13, 197);
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: rgb(218, 197, 33);
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }
        #intensity
        {
            height: 30px;
            width: 300px;
        }
        #resistance
        {
            height: 30px;
            width: 300px;
        }
        #power
        {
            height:30px;
            width:300px;
        }
        h2{
            color:rgb(182, 31, 51);
        }
    </style>
</head>
<body> 
    <div class="container" >

        <h2>LAMP FILAMENT POWER CALCULATOR</h2>
        <form id="powerForm" method="post">
            {% csrf_token %}
            <label for="intensity">INTENSITY (I) IN AMPERES:</label>
            <input type="number" id="intensity" name="Intensity" value="{{ i }}">
        
            <label for="resistance">RESISTANCE (R) IN OHMS:</label>
            <input type="number" id="resistance" name="Resistance" value="{{ r }}">
        
            <label for="power">POWER IN WATTS (W):</label>
            <input type="number" id="power" name="power" value="{{ power }}" readonly>
        <br>
            <button type="submit">Calculate Power</button>
        </form>
        
        <font color="red">


        <div class="result" id="result"></div>
    </font>
    </div>
</body>
</html>

views.py
from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['i'] = "0" 
    context['r'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        i = request.POST.get('Intensity','0')
        r = request.POST.get('Resistance','0')
        print('request=',request)
        print('Intensity=',i)  
        print('Resistance=',r) 
        power = int(r) *int(i) *int(i) 
        context['power'] = power
        context['i'] = i
        context['r'] = r
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

    urls.py
from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="calculatepower"),
    path('',views.power,name="calculatepower")
]
```

## SERVER SIDE PROCESSING:

![alt text](<Screenshot (60).png>)
## HOMEPAGE:

![alt text](<Screenshot (61).png>)
## RESULT:
The program for performing server side processing is completed successfully.
