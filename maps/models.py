from django.db import models



class Map(models.Model):                                 #класс поля БД
    name = models.CharField("название",max_length=50)    #Создали поле name
    description = models.TextField("описание")           #Создали поле description
    updated = models.DateTimeField(auto_now= True)
    photomap = models.ImageField("фотография карты", upload_to="maps/photosmap", default="", blank=True)
    class Meta:
        verbose_name = "карта"              #задает имя поля на страницах встроенного админ сайта
        verbose_name_plural = "карты"       #задает имя поля на страницах встроенного админ сайта
        ordering = ["name"]                 #сортировка

    def __str__(self):                      #изменяем имя полей в админ сайте

        return self.name                    #возращаем имя поле БД namehelp