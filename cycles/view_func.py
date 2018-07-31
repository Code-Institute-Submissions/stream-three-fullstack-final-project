from django.contrib import messages
from search.search import SearchCycles
from cyclestatus.models import CycleStatus
from django.db.models import Q

## Helper Function/s for Cycles Views ##

## Get Searched Cycles via Search App Class SearchCycles ##
def get_searched_cycles(request):
    kwargs = {'search': request.GET['search'],
            'order': request.GET['order']}

    cycles = SearchCycles(request, **kwargs)
    if request.GET['sort'] == 'all':
        users_cycles = cycles.search_all_cycles()
    elif request.GET['sort'] == 'pending':
        users_cycles = cycles.search_pending_cycles()
    elif request.GET['sort'] == 'cancelled':
        users_cycles = cycles.search_cancelled_cycles()
    elif request.GET['sort'] == 'complete':
        users_cycles = cycles.search_completed_cycles()
    elif request.GET['sort'] == 'active':
        users_cycles = cycles.search_active_cycles()

    return users_cycles

## Class Set's overall Session Variable Stats Based on User's Cycles ##
class SetSessionValues:
    
    def __init__(self, request):
        self.request = request

## Call this Function to Set all Session Variables from One Method ##
    def set_values(self):
        self.value_of_completed()
        self.value_of_cancelled()
        self.value_of_active()
        self.value_of_pending()
        
## Filter User by Member or Client ##
    def filter_user(self):
        if self.request.user.is_member:
            user = CycleStatus.objects.filter(cycle__member=self.request.user)
        elif self.request.user.is_client:
            user = CycleStatus.objects.filter(cycle__client=self.request.user)
        return user

## Get Total Value of Filtered Status and Strip Away Currency Tag ##
    def total(self, results):
        total = 0
        for status in results:
            total += status.cycle.cycle_value
        total = str(total).split(' ')
        if total[0] == '0':
            total[0] = '0.00'
        return total[0]

## Filter User Queryset by Complete Statuses ##
    def value_of_completed(self):
        results = self.filter_user().filter(complete=True) 
        total = self.total(results)
        self.request.session['complete'] = total
        return total

## Filter User Queryset by Cancelled Statuses ##     
    def value_of_cancelled(self):
        results = self.filter_user().filter(cancelled=True) 
        total = self.total(results)
        self.request.session['cancelled'] = total
        return total

## Filter User Queryset by Pending Statuses ##
    def value_of_pending(self):
        results = self.filter_user().filter(pending=True) 
        total = self.total(results)
        self.request.session['pending'] = total
        return total

## Filter User Queryset by Active Statuses ##
    def value_of_active(self):
        results = self.filter_user().exclude(Q(cancelled=True) | 
                                                Q(complete=True) | 
                                                Q(pending=True))
        total = self.total(results)
        self.request.session['active'] = total
        return total
        
    