from result.forms import InputForm
from result.models import Result,Input
from django.views.generic.list import ListView
from django.views.generic import FormView
....

@csrf_exempt

class InputFormView(FormView):
    ''' This is view return redirect.
        Redirect is GET request with status code 302.
    '''
    template_name = 'inputform.html'
    form = InputForm

    def get_success_url(self):  /*redirect to result page with submitted form information*/
        return ''.join(
            [
                reverse('result'),
                '?company=',self.request.POST.get('company'),
                '&region=',self.request.POST.get('region') # only first separator '?' all next is '&'
            ]
        )

class ResultView(ListView):
    context_object_name = 'result_list'
    template_name = 'result_list.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        if self.request.method == 'GET': # If this view is target on redirect must have GET data.
            form = InputForm(self.request.GET)
            if form.is_valid():
                company = form.cleaned_data['company']
                region = form.cleaned_data['region']

/---Based on form entry, do the filter on the database-----/

                queryset=Result.objects.filter(region=region,company=company)
                sales=queryset.aggregate(Sum('sales'))
                employee=queryset.aggregate(Sum('employee'))
                departments=queryset.aggregate(Sum('departments'))

                form.save()
                
                result_context = {
                    'company': company,
                    'region': region,
                    'employee': employee,
                    'sales': sales,
                    'departments': departments
                }

                return render(request,'result_list.html',result_context)

            else:
                print form.errors
        else:
            form=InputForm()                   
        return super(ResultView,self).get_queryset()
