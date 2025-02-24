# from rest_framework.pagination import PageNumberPagination

# class Mypagination(PageNumberPagination):
#     page_size=2
#     page_query_param='pg'   #instead of /?page=2 we can write /?pg=2
#     page_size_query_param='records'   #instead of /?pg=2 we can write /?pg=2&records=5  (whch page you want and pageperview)
#     max_page_size=5  #maximum page size per view
#     last_page_strings=('end',)  #normally /?pg=last gives us last page but we can change it to /?pg=end or any string
    
    
# from rest_framework.pagination import LimitOffsetPagination

# class Mypagination(LimitOffsetPagination):
#     default_limit=2      #by default limit is 2
#     limit_query_param='mylimit'
#     offset_query_param='myoffset'
#     max_limit=5
    
    
from rest_framework.pagination import CursorPagination

class Mypagination(CursorPagination):                    #gives us  previous and next page
    page_size=2
    ordering='name'   #ordering by name  
    cursor_query_param='mycursor'    
