from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import logout

def index(request):


    return render(request, "home/index.html", {})


def plant(request):
    plant_id = request.GET.get("plant_id")
    plant = models.Plant.objects.get(id=plant_id)
    return render(request, "home/plant.html", {"plant":plant})


def logout_view(request):
    #logout the user and then render the homepage
    logout(request)
    #return to the current page
    return redirect(request.META['HTTP_REFERER'])

def login_view(request):
    #redirect to the admin login page for now
    return redirect('admin:index')
def register(request):
    return "Hello world"

def search(request,common_name=None,scientific_name=None,description=None,most_fertile_type=None,bonsai=None,available_in_turkey=None,maximum_height=None,min_temperature_resistance=None,max_temperature_resistance=None,arid_resistance=None,overwater_resistance=None,reproduction_with_single_plant_autogamy=None,reproduction_by_wind_anemogamy=None,edible_fruit=None,harmful_to_cats=None,hours_of_sunlight=None,litres_of_soil=None,woody_type=None,yearly_shoots=None,plan=None,soil_preference=None,disease_resistance=None,leaf_size=None,winter_leaf_shedding=None,updated_at=None,created_at_=None):
    search_parameters = {}
    #for parameters common_name, scientific_namme, description and most fertile we will use the contains operator since these are string fields
    if common_name is not None:
        search_parameters["common_name__contains"] = common_name
    if scientific_name is not None:
        search_parameters["scientific_name__contains"] = scientific_name
    if description is not None:
        search_parameters["description__contains"] = description
    if most_fertile_type is not None:
        search_parameters["most_fertile_type__contains"] = most_fertile_type
    #for parameters bonsai, available_in_turkey, reproduction_with_single_plant_autogamy, reproduction_by_wind_anemogamy, edible_fruit, harmful_to_cats, yearly_shoots, winter_leaf_shedding we will use the exact operator since these are boolean fields. These can be NULL too so if the field is send as NONE text we will assume we are searching for the instances that this field is NUlL but since this field may not have been ssearched for, if the field is null we will not add it to the search parameters
    if bonsai is not None:
        if bonsai == "NONE":
            search_parameters["bonsai__isnull"] = True
        else:
            search_parameters["bonsai"] = bonsai
    if available_in_turkey is not None:
        if available_in_turkey == "NONE":
            search_parameters["available_in_turkey__isnull"] = True
        else:
            search_parameters["available_in_turkey"] = available_in_turkey
    if reproduction_with_single_plant_autogamy is not None:
        if reproduction_with_single_plant_autogamy == "NONE":
            search_parameters["reproduction_with_single_plant_autogamy__isnull"] = True
        else:
            search_parameters["reproduction_with_single_plant_autogamy"] = reproduction_with_single_plant_autogamy
    if reproduction_by_wind_anemogamy is not None:
        if reproduction_by_wind_anemogamy == "NONE":
            search_parameters["reproduction_by_wind_anemogamy__isnull"] = True
        else:
            search_parameters["reproduction_by_wind_anemogamy"] = reproduction_by_wind_anemogamy
    if edible_fruit is not None:
        if edible_fruit == "NONE":
            search_parameters["edible_fruit__isnull"] = True
        else:
            search_parameters["edible_fruit"] = edible_fruit
    if harmful_to_cats is not None:
        if harmful_to_cats == "NONE":
            search_parameters["harmful_to_cats__isnull"] = True
        else:
            search_parameters["harmful_to_cats"] = harmful_to_cats
    if yearly_shoots is not None:
        if yearly_shoots == "NONE":
            search_parameters["yearly_shoots__isnull"] = True
        else:
            search_parameters["yearly_shoots"] = yearly_shoots
    if winter_leaf_shedding is not None:
        if winter_leaf_shedding == "NONE":
            search_parameters["winter_leaf_shedding__isnull"] = True
        else:
            search_parameters["winter_leaf_shedding"] = winter_leaf_shedding
    #for parameters maximum_height, min_temperature_resistance, max_temperature_resistance, hours_of_sunlight, litres_of_soil we will use the exact operator
    if maximum_height is not None:
        search_parameters["maximum_height"] = maximum_height
    if min_temperature_resistance is not None:
        search_parameters["min_temperature_resistance"] = min_temperature_resistance
    if max_temperature_resistance is not None:
        search_parameters["max_temperature_resistance"] = max_temperature_resistance
    if hours_of_sunlight is not None:
        search_parameters["hours_of_sunlight"] = hours_of_sunlight
    if litres_of_soil is not None:
        search_parameters["litres_of_soil"] = litres_of_soil
    #for parameters arid_resistance, overwater_resistance, disease_resistance, leaf_size we will use the exact operator
    if arid_resistance is not None:
        search_parameters["arid_resistance"] = arid_resistance
    if overwater_resistance is not None:
        search_parameters["overwater_resistance"] = overwater_resistance
    if disease_resistance is not None:
        search_parameters["disease_resistance"] = disease_resistance
    if leaf_size is not None:
        search_parameters["leaf_size"] = leaf_size
    #for parameters woody_type, plan we will use the exact operator
    if woody_type is not None:
        search_parameters["woody_type"] = woody_type
    if plan is not None:
        search_parameters["plan"] = plan
    #for parameters updated_at, created_at we will use the exact operator
    if updated_at is not None:
        search_parameters["updated_at"] = updated_at
    if created_at_ is not None:
        search_parameters["created_at_"] = created_at_
    #for parameters soil_preference we will use the contains operator since this is a string field
    if soil_preference is not None:
        search_parameters["soil_preference__contains"] = soil_preference
    #now we will search for the plants that match the search parameters
    if len(search_parameters) == 0:
        plants = models.Plant.objects.all()
    else:
        plants = models.Plant.objects.filter(**search_parameters)
    return render(request, "home/search.html", {"plants":plants})


