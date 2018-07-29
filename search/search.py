from cyclestatus.models import CycleStatus
from django.db.models import Q



class SearchCycles:
    
    def __init__(self, request, username, **kwargs):
        self.request = request
        self.username = username
        self.query = kwargs.get('search')
        self.filter = kwargs.get('filter')
        self.direction = kwargs.get('direction')


    def search_member_cycles(self):
        cycles = CycleStatus.objects.filter(cycle__member__username=self.username).filter(
                                            Q(cycle__job__job_title__contains=self.query) | 
                                            Q(cycle__client__first_name__contains=self.query) | 
                                            Q(cycle__client__last_name__contains=self.query) | 
                                            Q(cycle__cycle_title__contains=self.query) | 
                                            Q(cycle__client__username__contains=self.query) |
                                            Q(cycle__id__contains=self.query)
                                            )   
        return cycles