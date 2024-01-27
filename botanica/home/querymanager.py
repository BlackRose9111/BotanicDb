from django.http import HttpRequest


class QueryManager:

    query_parameters = {}
    query_keys = []

    def __init__(self,request):
        self.request = request

    def get_query_parameters(self):
        pass

class SearchQueryManager(QueryManager):
    query_keys = ["common_name",
                  "scientific_name",
                  "bonsai",
                  "maximum_height",
                  "min_temperature_resistance",
                  "max_temperature_resistance",
                  "arid_resistance",
                  "overwater_resistance",
                  "reproduction_with_single_plant_autogamy",
                  "reproduction_by_wind_anemogamy",
                  "edible_fruit",
                  "harmful_to_cats",
                  "hours_of_sunlight",
                  "litres_of_soil",
                  "woody_type",
                  "yearly_shoots",
                  "plan",
                  "soil_preference",
                  "disease_resistance",
                  "leaf_size",
                  "winter_leaf_shedding",]
    def __init__(self,request):
        super().__init__(request)
        self.query_parameters = self.get_query_parameters()

    def get_query_parameters(self):
        query_parameters = {}
        for key in self.query_keys:
            try:
                query_parameters[key] = self.request.GET.get(key=key)
            except:
                query_parameters[key] = "Not Specified"

        return query_parameters


    def get_query_keys(self):
        return self.query_keys





