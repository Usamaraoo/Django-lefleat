from django.shortcuts import render, redirect
from .models import Pakistan, Areas


def area_view(request):
    areas = Pakistan.objects.all()
    selected_areas = [one_area for areas in Areas.objects.all() for one_area in areas.area.all()]
    tags_list = Areas.objects.all()
    if request.method == "POST":
        color = request.POST.get('color')
        tag = request.POST.get('tag')
        tags = request.POST.get('tags_from_list')
        tag_to_use = tag if tag != '' else tags
        got_tag, created_tag = Areas.objects.get_or_create(tag=tag_to_use)
        areas_got = request.POST.get('selected_areas').split(',')
        for i in areas_got[1:]:
            area = Pakistan.objects.get(name=i)
            got_tag.area.add(area)
            area.selected_color = color if created_tag is True \
                else Areas.objects.filter(tag=got_tag)[0].area.all()[0].selected_color
            area.tag = got_tag.tag
            area.save()
        return redirect('areas')

    context = {'areas': areas, 'selected_areas': selected_areas, 'tags': tags_list}
    return render(request, 'shape_app/pakistan_areas.html', context)
