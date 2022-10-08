from django.shortcuts import render
from django.http import JsonResponse,response
from .calculation_dict_template import calculation_dict_template,calculation_dict,text_calc_dict,calculation
from .text_sum import text_sum
def home(request):
    return render(request, 'home.html')



def calculations(request):
    inputs={}
    calculations_json={}
    sum_all=0
    text_sum_all=''

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        for key in calculation_dict_template:
             inputs[key]=request.POST.get(key)
        for key,value in calculation_dict.items():
            calculations_json[key]=calculation(request.POST.get(value),float(value[6:]))
            sum_all+=float(calculation(request.POST.get(value),float(value[6:])))
        for key,value in text_calc_dict.items():
            calculations_json[key]=text_sum(calculations_json[value])
        sum_all=round(sum_all,2)
        text_sum_all=text_sum(str(sum_all))
        ajax_response={'inputs':inputs,'calculations_json':calculations_json,'sum_all':sum_all,'text_sum_all':text_sum_all}
        return JsonResponse({'ajax_response':ajax_response })
    return JsonResponse({'nie bardzo działą':'nie bardzo działą' })
