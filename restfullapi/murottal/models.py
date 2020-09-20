from django.db import models

class Surat(models.Model):
    no_surat = models.IntegerField()
    nama_surat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_surat
