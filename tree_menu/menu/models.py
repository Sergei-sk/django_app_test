from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return str(self.name)


class MenuPoint(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_point')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Подпункты'
        verbose_name_plural = 'Подпункты'

    def __str__(self):
        return str(self.name)
