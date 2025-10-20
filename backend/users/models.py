from django.db import models
# AbstractBaseUser ->  Es un modelo de usuario base, con Email, Username, Password
# BaseUserManager  ->  Para la autentificacion el usuario base necesita un manager, contiene metodos para crear usuario y super usuario
# PermissionMinxin ->  Maneja los permisos, el ocupa el atributo is_superuser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Es el manager, tiene los metodos para crear un usuario y un super usuario
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electronico")
        email = self.normalize_email(email)
        user = self.model(email = email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, username, password, **extra_fields)
    
# Este es el modelo en si, y este usa los metdos del manager
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    age = models.PositiveIntegerField(blank=True, null=True)
    height_cm = models.FloatField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    goal = models.CharField(
        max_length=50, 
        choices=[
            ('mantener', 'Mantener peso'),
            ('perder', 'Perder grasa'),
            ('ganar', 'Ganar masa muscular'),
        ],
        default='mantener'
    )
    
    # Campos del sistema
    is_active = models.BooleanField(default=True) # Puede iniciar sesion?
    is_staff = models.BooleanField(default=False) # Se puede acceder al panel de admin?
    date_joined = models.DateTimeField(auto_now_add=True) # Cuando se registro

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"