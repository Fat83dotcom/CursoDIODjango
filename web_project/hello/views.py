from django.shortcuts import render, HttpResponse


# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, você tem {idade} anos.</h1>')


def operacao(request, oper, n1, n2):
    if oper == 'soma':
        soma = n1 + n2
        return HttpResponse(f'<h1>A soma {n1} + {n2} = {soma}</h1>')
    elif oper == 'sub':
        sub = n1 - n2
        return HttpResponse(f'<h1>A subtração {n1} - {n2} = {sub}</h1>')
    elif oper == 'multp':
        mult = n1 * n2
        return HttpResponse(f'<h1>A multiplicação {n1} x {n2} = {mult}</h1>')
    else:
        if n2 == 0:
            return HttpResponse('<h1>Não é possivel divisão por zero.</h1>')
        else:
            div = n1 / n2
            return HttpResponse(f'<h1>A divisão {n1} / {n2} = {div}</h1>')
