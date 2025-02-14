from django.shortcuts import render
from datetime import datetime


#Example 1.1-variable
# def template(req):
    
#   coursename= {'cname': 'whaaaat'}
#   return render(req, 'app2/django.html', context=coursename)


#Example 1.2-variable

# def template(req):
  #  name='django'  
  # duration='5 months'
   # seats=10
   # detailes={'nm':name,'du':duration, 'st':seats}
   # return render(req,'app2/django.html', context=detailes)
   
#Example 2-filters
# def template(req):
#   return render(req, 'app2/django.html',context={'name':'django', 'desc':'Django is awesome.'})

#Example 2.2-filters
def template(req):
    d=datetime.now
    return render(req, 'app2/django.html',context={'dt':d})
            

