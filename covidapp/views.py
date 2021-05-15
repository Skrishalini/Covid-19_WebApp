from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    'x-rapidapi-key': "63fb33f6e2msh61d754ddfcb7af5p116d4ajsnae4038f9b20c",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


def helloworldview(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range (0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']

        for x in range (0,noofresults):
            if selectedcountry == response['response'] [x] ['country']:
              new = response['response'] [x] ['cases'] ['new']
              active = response['response'] [x] ['cases'] ['active']
              critical = response['response'] [x] ['cases'] ['critical']
              recovered = response['response'] [x] ['cases'] ['recovered']
              total = response['response'] [x] ['cases'] ['total']
              deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry':selectedcountry,'mylist':mylist, 'new' : new, 'active' : active ,'critical': critical, 'recovered' : recovered, 'deaths' : deaths, 'total': total}
        return render(request,'helloworld.html',context)
    
    mylist = []
    for x in range (0,noofresults):
        mylist.append(response['response'][x]['country'])
    context ={'mylist':mylist} 
    return render(request,'helloworld.html',context)
    
