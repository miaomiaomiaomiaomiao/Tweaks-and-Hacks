class ResultView(ListView):
    context_object_name = 'result_list'
    template_name = 'result_list.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context["sales"] = self.get_queryset().aggregate(Sum('sales'))
        context["employee"] = self.get_queryset().aggregate(Sum('employee'))
        context["departments"] = self.get_queryset().aggregate(Sum('departments'))
        return context

    def get_queryset(self):
        if self.request.method == 'POST':  # if form action target this view, else "GET"
            form = InputForm(self.request.POST)  # if form action target this view, else "GET"
            if form.is_valid():
                company = form.cleaned_data['company']
                region = form.cleaned_data['region']

/---Based on form entry, do the filter on the database-----/

                queryset=Result.objects.filter(region=region,company=company)

                form.save()

                return queryset               
        return super(ResultView,self).get_queryset()
