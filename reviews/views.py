from django.shortcuts import render, get_object_or_404
from .models import Wine, Review
from .forms import ReviewForm
import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def review_list(request):
	latest_review_list = Review.objects.order_by('pub_date')[:9]
	context = {'latest_review_list': latest_review_list}
	return render(request, 'reviews/review_list.html', context)

def review_detail(request):
	review=get_object_or_404(Review,pk=review_id)
	return render(request,'reviews/review_detail.html',{'review':review})

def wine_list(request):
	wine_list = Wine.objects.order_by('name')
	context={'wine_list':wine_list}
	return render(request, 'reviews/wine_list.html', context)

def wine_detail(request):
	wine = get_object_or_404(Wine,pk=wine_id)
	return render(request, 'reviews/wine_detail.html', {'wine':wine})	

def add_review(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.wine = wine
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()	
        return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))

    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})