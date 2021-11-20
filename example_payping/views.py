from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from payping.authentication import Bearer
from payping.payment import make_payment_code, get_url_payment, verify_payment


def send_request(request):
    header = Bearer(token='')
    code = make_payment_code(header=header, amount=2000, returnUrl='http://localhost:8000/verify/',
                             payerName='mohammad', clientRefId='22')
    redirect_to_pay_url = get_url_payment(code)
    return redirect(redirect_to_pay_url)


def verify(request):
    clientrefid = request.GET.get('clientrefid')
    refid = request.GET.get('refid')
    if refid is not 1:
        header = Bearer(token='')
        res = verify_payment(header, refid=refid, amount=2000)
        if res is 200:
            return HttpResponse('successful')
        else:
            raise Http404()
