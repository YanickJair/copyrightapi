from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Tipos de Obras
MUSICA = 1
IMAGEM = 2
VIDEO = 3
LIVRO = 4
PROGRAMA_COMPUTADOR = 5

# Create your models here.

class AreaAplicacao (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    state = models.BooleanField(default=False)
    data_creation = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class TipoPerfil (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    state  = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Perfil (models.Model):
    user = models.ForeignKey(User, related_name='perfil', on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='user/profile-image/', blank=True, null=True)
    state = models.BooleanField(default=False)
    area = models.ForeignKey(AreaAplicacao, related_name='area', on_delete=models.DO_NOTHING)
    data_creation = models.DateField(auto_now_add=True)
    profile_type = models.ForeignKey(TipoPerfil, verbose_name="Tipo de perfil do associado", 
    on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('data_creation', )

    def __str__(self):
        return self.user.username
    
class Licenca (models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField()
    state = models.BooleanField(default=False)
    data_creation = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name', )
    
    def __str__(self):
        return self.name

class TipoObra (models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField()
    state = models.BooleanField(default=False)
    data_creation = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    

class Obra (models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=True, null=True, default='Obra não possui descrição.')
    type_obra = models.ForeignKey(TipoObra, verbose_name="Tipo de obra", on_delete=models.DO_NOTHING)
    licenca = models.ForeignKey(Licenca, verbose_name="Disponivel sob a licença:", 
    on_delete=models.DO_NOTHING)
    url = models.FileField(upload_to=None, max_length=100)
    data_registered = models.DateField(auto_now_add=True)
    data_creation = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        folder = 'media/'
        if self.type_obra is MUSICA:
            fs = FileSystemStorage(location=folder+'obra_musica/')
            fs.save(self.url.name, self.url)
        elif self.type_obra is IMAGEM:
            fs = FileSystemStorage(location=folder+'obra_imagem/')
            fs.save(self.url.name, self.url)
        elif self.type_obra is VIDEO:
            fs = FileSystemStorage(location=folder+'obra_video/')
            fs.save(self.url.name, self.url)
        elif self.type_obra is LIVRO:
            fs = FileSystemStorage(location=folder+'obra_livro/')
            fs.save(self.url.name, self.url)
        elif self.type_obra is PROGRAMA_COMPUTADOR:
            pass
        
        super().save(*args, **kwargs) # Call the real save() method

class ObraAdquirida (models.Model):
    obra = models.ForeignKey(Obra, verbose_name="Obra adquirida sob licença", 
    on_delete=models.DO_NOTHING)
    data_aquisition = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Quem adquiriu a obra.", 
    on_delete=models.DO_NOTHING)
    signature = models.TextField(blank=False, null=False) # Assinatura de quem adquiri a obra

    class Meta:
        ordering = ('data_aquisition', )

    def __str__(self):
        return self.obra.name

class Commentary (models.Model):
    commentary = models.TextField()
    obra = models.ForeignKey(Obra, verbose_name="Comentario referente a obra:", 
    on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, verbose_name="Quem comentou a obra:", 
    on_delete=models.DO_NOTHING)
    data_commentary = models.DateField(auto_now_add=True)
    state = models.BooleanField(default=True)

    class Meta:
        ordering = ('data_commentary', )

    def __str__(self):
        return self.commentary
    
class CommentaryReply (models.Model):
    commentary = models.ForeignKey(Commentary, verbose_name="Referente a este comentario", 
    on_delete=models.DO_NOTHING)
    reply = models.TextField()
    user = models.ForeignKey(User, verbose_name="Quem respondeu ao comentario", 
    on_delete=models.DO_NOTHING)
    data_reply = models.DateField(auto_now_add=True)
    state = models.BooleanField(default=True)

    class Meta:
        ordering = ('data_reply', )

    def __str__(self):
        return self.reply