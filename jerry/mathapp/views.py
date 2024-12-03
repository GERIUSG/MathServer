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
