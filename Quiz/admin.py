from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario

from .forms import ElegirInLineFormset

class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    can_delete =False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    min_num = ElegirRespuesta.MAXIMO_RESPUESTAS
    formset = ElegirInLineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto',]
    search_fields = ['texto', 'preguntas__texto']



class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

    class Meta:
        model = PreguntasRespondidas

admin.site.register(ElegirRespuesta)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(PreguntasRespondidas)
admin.site.register(QuizUsuario)