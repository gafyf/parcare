from django.contrib.auth.models import User
from .models import Profil
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver


@ receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user=instance
        profil = Profil.objects.create(
            user=user,
            pk=user.id,
            email=user.email,
            prenume=user.first_name,
            nume=user.last_name,
        )
        profil.save()
        # print("Signal creat user si profil: ",instance)

@ receiver(post_save, sender=Profil)
def updateUser(sender, instance, created, **kwargs):
    # print("Signal update profil ",instance)
    if created == False:
        profil = instance
        user = profil.user
        user.id = profil.id
        # user.id = profil.id
        user.first_name = profil.prenume
        user.last_name = profil.nume
        user.email = profil.email
        user.save()
        # print("Signal update profil si user: ",instance)

@ receiver(pre_delete, sender=Profil)
def deleteUser(sender, instance, **kwargs):
    print('Sigur vrei sa stergi userul ', instance,'?')


@ receiver(post_delete, sender=Profil)
def deleteUser(sender, instance, **kwargs):
    print('Userul', instance, 'a fost sters cu succes!')
    try:
        user = instance.user
        user.delete()
    except:
        pass

@receiver(pre_save, sender=Profil)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).imagine.path
        try:
            new_img = instance.imagine.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass

@receiver(post_delete, sender=Profil)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.imagine.delete(save=False)
    except:
        pass



