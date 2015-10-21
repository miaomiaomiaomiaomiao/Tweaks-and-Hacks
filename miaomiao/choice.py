# Try this
class ResultView(ListView):
    context_object_name = 'result_list'
    template_name = 'result_list.html'
    model = Result

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context["sales"] = self.get_queryset().aggregate(Sum('sales'))
        context["employee"] = self.get_queryset().aggregate(Sum('employee'))
        context["departments"] = self.get_queryset().aggregate(Sum('departments'))
        context["region"] = self.request.POST.get("region")  # if form action target this view, else "GET"
        context["company"] = self.request.POST.get("company")  # if form action target this view, else "GET"
        return context

    def get_queryset(self):
        if self.request.method == 'POST':  # if form action target this view, else "GET"
            form = InputForm(self.request.POST)  # if form action target this view, else "GET"
            if form.is_valid():
                company = form.cleaned_data['company']
                region = form.cleaned_data['region']
                queryset=Result.objects.filter(region=region, company=company)
                return queryset               
        return super(ResultView,self).get_queryset()
        
# or this
class ResultView(ListView):
    context_object_name = 'result_list'
    template_name = 'result_list.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context["sales"] = self.get_queryset().aggregate(Sum('sales'))
        context["employee"] = self.get_queryset().aggregate(Sum('employee'))
        context["departments"] = self.get_queryset().aggregate(Sum('departments'))
        context["region"] = self.request.POST.get("region")  # if form action target this view, else "GET"
        context["company"] = self.request.POST.get("company")  # if form action target this view, else "GET"
        return context

    def get_queryset(self):
        if self.request.method == 'POST':  # if form action target this view, else "GET"
            form = InputForm(self.request.POST)  # if form action target this view, else "GET"
            if form.is_valid():
                company = form.cleaned_data['company']
                region = form.cleaned_data['region']
                queryset=Result.objects.filter(region=region, company=company)
                return queryset               
        return Result.objects.all()
