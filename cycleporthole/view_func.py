from django.shortcuts import get_object_or_404
from cycles.models import Cycles
from accounts.models import AllUser


## View helper_functions ##

## Get Cycle Info for Porthole Template ##
def get_porthole_info(username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    member = get_object_or_404(AllUser, username=username)
    client = get_object_or_404(AllUser, username=client_username)

    porthole_info = {'cycle':cycle, 'member':member, 'client':client}
    return porthole_info