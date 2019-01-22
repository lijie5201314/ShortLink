from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from .models import Links
from .number_utils import _10_to_62


def index(request):
    count = request.COOKIES.get('count')
    if not count:
        count = 1
    else:
        count = int(count)
        count += 1
    response = render_to_response('short_url/index.html', {'count':count})
    response.set_cookie('count', count)
    return response



def longtoshort(request):
    longlink = request.POST.get('longlink')
    key = ''
    try:
        url = Links.objects.get(url=longlink)
        global key
        key = url.keyword
    except Exception:
        last = Links.objects.all().order_by('-id')[:1]
        if len(last) == 0:
            id = 1
        else:
            id = int(last[0].pk + 1)

        keyword = _10_to_62(str(id))
        global key
        key = keyword
        link = Links.createLinks(url=longlink,keyword=keyword)
        link.save()


    url = 'https://dwz.cn/'+key

    return HttpResponse('原网站：'+longlink+' 短网站：'+url)



def shorttolong(request,shorturl):
    try:
        url = Links.objects.get(keyword=shorturl)
        return redirect(url.url)
    except Exception:
        error = '短网址不存在，请检查是否正确'
        return HttpResponse(error)


def shortcustom(request):
    shortlink = request.POST.get('shortlink')
    url = request.POST.get('url')
    try:
        Links.objects.get(url=url)
        link = Links.createLinks(url=url, keyword=shortlink, type=1)
        link.save()
        urlshort = 'https://dwz.cn/' + shortlink
        return HttpResponse('设置成功   ' + '原网站：' + url + ' 短网站：' + urlshort)

    except:
        return HttpResponse('已存在短链，请重新设置')
