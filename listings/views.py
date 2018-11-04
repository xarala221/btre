from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator
from .models import Listing
from .choices import *



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings,
    }
    return render(request, "listings/listings.html", context)



def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
      'listing': listing
    }
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #print("query ", queryset_list)
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        queryset_list = queryset_list.filter(description__icontains=keywords)
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        queryset_list = queryset_list.filter(city__iexact=city)
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        queryset_list = queryset_list.filter(state__iexact=state)
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #price
    
    if 'price' in request.GET:
        price = request.GET['price']
        queryset_list = queryset_list.filter(price__lte=price)
    print("query ", queryset_list)
    
    context = {
      'bedroom_choices':bedroom_choices,
      'price_choices': price_choices,
      'state_choices':state_choices,
      'listings': queryset_list,
      'values':request.GET
    }
    return render(request, "listings/search.html", context)