from datetime import datetime

from django.db import models

from cousine.models import Ingredient


class Indirizzo(models.Model):
    via = models.CharField(max_length=80)
    citta = models.CharField(max_length=50)
    prov = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)


class Contatto(models.Model):
    tel = models.CharField(max_length=50)
    email = models.EmailField()


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    indirizzo = models.OneToOneField(Indirizzo, related_name='indirizzo', on_delete=models.CASCADE, null=True)
    contatto = models.OneToOneField(Contatto, related_name='contatto', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unitaArrivo = models.IntegerField()
    giacenza_in_gr = models.FloatField()
    prezzo_al_kg= models.FloatField()


class Invoice(models.Model):
    invoiceNumber = models.CharField(max_length=50)
    invoicedate = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    totfood = models.FloatField()
    totnonfood = models.FloatField()
    note = models.TextField

    class meta:
        ordering = ["supplier_name", "-invoicedate"]

    def __str__(self):
        return 'fattura n. ' + str(self.invoiceNumber) + ' del ' + str(self.invoicedate) + ' di ' + self.supplier.name


class ArrivoFood(models.Model):
    incomingdate = models.DateField(default=datetime.now)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    conforme = models.BooleanField(default=True)
    scadenza = models.DateField()

    def __str__(self):
        return self.incomingdate.strftime(
            "%m/%d/%Y") + ' - ' + self.article.name + ' (' + self.article.supplier.name + ')' + 'qta ' + str(
            self.quantity)

class OrdineFornitore(models.Model):
    data = models.DateField(default=datetime.now)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    dataPrevista = models.DateField()
    dataConsegna = models.DateField()
    altreRichieste = models.TextField()

class VociOrdineFornitore(models.Model):
    ordine = models.ForeignKey(OrdineFornitore, on_delete=models.CASCADE)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    quantity = models.FloatField()
    note = models.TextField()