from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Menu, MenuPoint


def index(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    print(splitted_path)
    if len(splitted_path)>1:
        point_path = splitted_path[-1]
        print(point_path)
        point = MenuPoint.objects.filter(parent=point_path)
        # point_chek = MenuPoint.objects.in_bulk()
        # for x in point_chek:
        #     print(x)
        print(point)
        # print(point_chek[11])
        print('pizda')
        context = {
        'point': point,
    }
        return render(request, 'menu/menu.html', context)
    # else:
    #     people2 = MenuPoint.objects.in_bulk()
    #     for id in people2:
    #         print(people2[id].parent)
        # return render(request, 'menu/menu.html', {'point':people2,})
    else:
        str_obj = ''.join(splitted_path)
        print('url: ', str_obj)
        menu_obj = Menu.objects.get(name=str_obj)
        id_menu = menu_obj.id
        print('id_menu: ', id_menu)
        point = MenuPoint.objects.filter(menu=id_menu, parent=None)
        print('point: ', point)
        context = {
            'point': point,
        }
        return render(request, 'menu/menu.html', context)
