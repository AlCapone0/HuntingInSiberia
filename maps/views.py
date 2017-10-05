from django.shortcuts import render, get_object_or_404
from .models import Map


def maps_list(request): #возращаем ответ на запрос, рендереную страницу
    maps = Map.objects.all() # переменой maps пресваиваем все объекты из БД
    return render(request, "maps/maps_list.html", {"maps":maps}) # возращаем от рендереную страницу

def map_detail(request, map_id): #запрос посетителя к странице map_detail
    map = get_object_or_404(Map, id=map_id) # переменой map пресваиваем все БД обекты с ID есле нет то 404
    return render(request, "maps/map_detail.html", {"map": map})  #возращаем ответ на запрос, рендереную страницу