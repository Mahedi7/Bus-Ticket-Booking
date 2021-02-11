from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import Bus
from .models import BusSeat
from .models import Passenger
from .models import Contact

admin.site.register(SignUp)
admin.site.register(Bus)
admin.site.register(BusSeat)
admin.site.register(Passenger)
admin.site.register(Contact)
