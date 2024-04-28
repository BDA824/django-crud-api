from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Estos son los campos de mi tabla Project que voy a mostrar en la respuesta al cliente
        fields = ('id', 'tittle', 'description', 'technology', 'create_at')
        # Este campo solo se podra visualizar y no editar
        read_only_fields = ('create_at',)
