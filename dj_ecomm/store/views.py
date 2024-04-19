from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"
#end class

# We should inherit the LoginRequiredMixin first. because python will consider the method 
# dispatch from the first inherited class
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = { 'object': order }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
#end class

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
#end class