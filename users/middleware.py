
from django.shortcuts import redirect
from django.contrib import messages


class AssignSalaryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path == '/register/' and request.method == 'POST':
            qualification = request.POST.get('qualification')
            if qualification not in ['Junior', 'Middle', 'Senior']:
                messages.error(request, 'Некорректный уровень квалификации!')
                return redirect('/register/')

            salary_mapping = {
                'Junior': 300,
                'Middle': 1000,
                'Senior': 2000,
            }
            request.POST = request.POST.copy()
            request.POST['salary'] = salary_mapping[qualification]

        return self.get_response(request)
