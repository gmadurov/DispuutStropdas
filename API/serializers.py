from agenda.models import AgendaClient, Event, NIEvent
from documents.models import Document
from finance.models import Boekstuk, Decla
from rest_framework import serializers
from users.models import Lid


class AgendaClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaClient
        fields = "__all__"


class LidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lid
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class DeclaSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = Decla
        fields = "__all__"
class BoekstukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boekstuk
        fields = "__all__"


class NIEventSerializer(serializers.ModelSerializer):
    # event = EventSerializer(many=False)
    # lid = LidSerializer(many=False)

    class Meta:
        model = NIEvent
        fields = "__all__"


class DsaniSerializer(serializers.ModelSerializer):
    dsani_ev = NIEventSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    owner = LidSerializer(many=False)
    # reviews = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = "__all__"
