from agenda.models import AgendaClient, Event, NIEvent
from documents.models import Document
from finance.models import Boekstuk, Decla, Stand
from rest_framework import serializers
from users.models import Lid


class AgendaClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaClient
        fields = "__all__"


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = "__all__"


class LidSerializer(serializers.ModelSerializer):

    stand = serializers.SerializerMethodField()
    def get_stand(self, lid):
        stand_set = StandSerializer(Stand.objects.get(owner_id=lid.id), many=False)
        return stand_set.data

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
