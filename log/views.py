import json
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from diary.models import Diary
from .models import Log
from accounts.views import get_role


def diary_log_list(request):
    use_pagination = True
    paginate_by = 5
    template_name = 'log/diary_log_list.html'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    user = request.user
    role = get_role(request)  # NOQA, to be used
    is_supervisor = user.groups.filter(name='Supervisors').exists()
    diary_logs = Log.objects.all().order_by('-created_at')
    print(diary_logs)
    diary_logs = [diary_log for diary_log in diary_logs if json.loads(diary_log.data).get('created_by') == request.user.id]
    paginator = Paginator(diary_logs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # temp solution for "all pages" view.
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else diary_logs
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, 'is_supervisor': is_supervisor, }
    return render(request, template_name, context)
