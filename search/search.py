from cyclestatus.models import CycleStatus
from django.db.models import Q


## Class for Searching and Filtering Users Cycles ##
class SearchCycles:
    
    def __init__(self, request, **kwargs):
        self.request = request
        self.user = request.user
        self.query = kwargs.get('search')
        self.order = kwargs.get('order')

        ## Set Order to Correct Search String ##
        if self.order == 'newest':
            self.order_by = '-cycle__created'
        elif self.order == 'oldest':
            self.order_by = 'cycle__created'

    def filter_by_member(self):
        cycles = CycleStatus.objects.filter(cycle__member__username=self.user.username)
        return cycles

    def filter_by_client(self):
        cycles = CycleStatus.objects.filter(cycle__client__username=self.user.username)
        return cycles

    def search_all_cycles(self):
        if self.user.is_member:
            cycles = self.filter_by_member()
            cycles = cycles.filter(Q(cycle__job__job_title__contains=self.query) | 
                            Q(cycle__client__first_name__contains=self.query) | 
                            Q(cycle__client__last_name__contains=self.query) | 
                            Q(cycle__cycle_title__contains=self.query) | 
                            Q(cycle__client__username__contains=self.query) |
                            Q(cycle__id__contains=self.query)
                            ).order_by(self.order_by)
        elif self.user.is_client:
            cycles = self.filter_by_client()
            cycles = cycles.filter(Q(cycle__job__job_title__contains=self.query) | 
                            Q(cycle__client__first_name__contains=self.query) | 
                            Q(cycle__client__last_name__contains=self.query) | 
                            Q(cycle__cycle_title__contains=self.query) | 
                            Q(cycle__client__username__contains=self.query) |
                            Q(cycle__id__contains=self.query)
                            ).order_by(self.order_by)
            
        return cycles

    def search_pending_cycles(self):
        cycles = self.search_all_cycles()
        cycles = cycles.filter(pending=True).order_by(self.order_by)
        return cycles

    def search_cancelled_cycles(self):
        cycles = self.search_all_cycles()
        cycles = cycles.filter(cancelled=True).order_by(self.order_by)
        return cycles
        
    def search_completed_cycles(self):
        cycles = self.search_all_cycles()
        cycles = cycles.filter(complete=True).order_by(self.order_by)
        return cycles

    def search_active_cycles(self):
        cycles = self.search_all_cycles()
        cycles = cycles.exclude(Q(pending=True) | 
                                Q(complete=True) | 
                                Q(cancelled=True)
                                ).order_by(self.order_by)
        return cycles
