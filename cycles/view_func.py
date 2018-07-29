from django.contrib import messages
from search.search import SearchCycles

## Helper Function/s for Cycles Views ##

## Get Searched Cycles via Search App Class SearchCycles ##
def get_searched_cycles(request, username):
    kwargs = {'search': request.GET['search'],
            'order': request.GET['order']}
    print(request.GET['sort'])
    cycles = SearchCycles(request, username, **kwargs)
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