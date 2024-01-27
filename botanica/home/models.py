from django.db import models

# Create your models here.

class Plant(models.Model):

    class Meta:
        verbose_name = "Bitki"
        verbose_name_plural = "Bitkiler"


    class resistance(models.TextChoices):
        LOW = "Düşük", "Düşük"
        MEDIUM = "Orta", "Orta"
        HIGH = "Yüksek", "Yüksek"
        UNKNOWN = "Bilinmiyor", "Bilinmiyor"

    class woody_type(models.TextChoices):
        odunsu = "Odunsu", "Odunsu"
        otsu = "Otsu", "Otsu"
        bilinmiyor = "Bilinmiyor",  "Bilinmiyor"

    class plan_types(models.TextChoices):
        main_plant = "Ana Bitki" , "Ana Bitki"
        under_the_pot = "Saksı Altı" , "Saksı Altı"
        no_plan = "Plan Yok", "Plan Yok"

    class leaf_size(models.TextChoices):
        small = "Küçük", "Küçük"
        medium = "Orta", "Orta"
        large = "Büyük", "Büyük"
        unknown = "Bilinmiyor", "Bilinmiyor"

    common_name = models.CharField(max_length=1000,blank=True, null=True, unique=True,verbose_name="Bilinen Adı")
    scientific_name = models.CharField(max_length=1000,blank=True, null=True, unique=True,verbose_name="Bilimsel Adı")
    description = models.TextField(blank=True, null=True,verbose_name="Açıklama")
    most_fertile_type = models.CharField(max_length=1000,blank=True, null=True,verbose_name="En Verimli Türü")
    bonsai = models.BooleanField(default=False,verbose_name="Bonsai İçin Uygun")
    #available_in_turkey = models.BooleanField(default=False,verbose_name="Türkiye'de Bulunabilir")
    maximum_height = models.IntegerField(null=True,verbose_name="Max Yükseklik")
    min_temperature_resistance = models.IntegerField(null=True,verbose_name="Min Sıcaklık Direnci")
    max_temperature_resistance = models.IntegerField(null=True,verbose_name="Max Sıcaklık Direnci")
    arid_resistance = models.CharField(max_length=10, choices=resistance.choices, default=resistance.UNKNOWN,verbose_name="Kuraklığa Direnç")
    overwater_resistance = models.CharField(max_length=10, choices=resistance.choices, default=resistance.UNKNOWN,verbose_name="Aşırı Sulamaya Direnç")
    reproduction_with_single_plant_autogamy = models.BooleanField(default=False,verbose_name="Tek Bitki ile Üreme (Otogami)")
    reproduction_by_wind_anemogamy = models.BooleanField(default=False,verbose_name="Rüzgar ile Tozlaşam (Anemogami)")
    edible_fruit = models.BooleanField(default=False, null=True,verbose_name="Yenilebilir Meyve")
    harmful_to_cats = models.BooleanField(default=False, null=True,verbose_name="Kediler İçin Zararlı")
    hours_of_sunlight = models.IntegerField(null=True,verbose_name="Kaç Saat Güneş Işığı Alabilir",default=0)
    litres_of_soil = models.IntegerField(null=True,verbose_name="Kaç Litre Toprak İhtiyacı Var",default=0)
    woody_type = models.CharField(max_length=10, choices=woody_type.choices, default=woody_type.bilinmiyor,verbose_name="Odunsu/Otsu")
    yearly_shoots = models.BooleanField(default=False,verbose_name="Her Yıl Yeni Sürgün")
    plan = models.CharField(max_length=10, choices=plan_types.choices, default=plan_types.no_plan,verbose_name="Plan")
    soil_preference = models.CharField(max_length=1000,blank=True, null=True,verbose_name="Toprak İsteği")
    disease_resistance = models.CharField(max_length=10, choices=resistance.choices, default=resistance.UNKNOWN,verbose_name="Hastalık Direnci")
    leaf_size = models.CharField(max_length=10, choices=leaf_size.choices, default=leaf_size.unknown,verbose_name="Yaprak Boyutu")
    winter_leaf_shedding = models.BooleanField(null=True,default=None,verbose_name="Kışın Yaprak Döküyor")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Güncelleme Tarihi")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",null=True)
    image = models.ImageField(upload_to="home/media/plants/", blank=True, null=True,verbose_name="Resim")

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"





class PlantOfTheDay(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,verbose_name="Bitki")
    date = models.DateField(verbose_name="Tarih")

    def __str__(self):
        return str(self.plant)

    class Meta:
        verbose_name = "Günün Bitkisi"
        verbose_name_plural = "Günün Bitkileri"
        ordering = ["-date"]

class AvailableInTurkey(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,verbose_name="Bitki",unique=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",null=True)
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return str(self.plant)

    class Meta:
        verbose_name = "Türkiye'de Bulunabilir Bitki"
        verbose_name_plural = "Türkiye'de Bulunabilir Bitkiler"