# Create your views here.


import doctest
from django.http import JsonResponse
from finance.models import Decla
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.forms import LidForm
from .serializers import (
    DeclaSerializer,
    DocumentSerializer,
    EventSerializer,
    LidSerializer,
    NIEventSerializer,
)
from documents.models import Document
from agenda.models import AgendaClient, Event, NIEvent
from users.models import Lid

API_URL = "/api"


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": API_URL + "/leden"},
        {"GET": API_URL + "/lid/id"},
        {"POST": API_URL + "/lid/id"},
        {"POST": API_URL + "/Event/id"},
        {"POST": API_URL + "/NIEvent/id"},
        {"GET": API_URL + "/NIEvent/lid_id/nievent_id"},
        {"GET": API_URL + "/NIEvents"},
        {"GET": API_URL + "/documents"},
        {"POST": API_URL + "/decla"},
        # {'GET': API_URL+'/document/id'},
        {"POST": API_URL + "/add_document"},
    ]
    return Response(routes)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getLeden(request):
    leden = Lid.objects.all()
    serializer = LidSerializer(leden, many=True)
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated]), "POST"
def getLid(request, pk):
    lid = Lid.objects.get(id=pk)
    serializer = LidSerializer(lid, many=False)
    # data = request.data
    # lid_edit = lid.update(
    # initials=data['initials'],
    # name=data['name'],
    # birth_date=data['birth_date'],
    # educations=data['educations'],
    # lichting=data['lichting'],
    # vertical=data['vertical'],
    # email=data['email'],
    # phone=data['phone'],
    # short_intro= data['short_intro'],
    # )
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getDocuments(request):
    docs = Document.objects.all()
    serializer = DocumentSerializer(docs, many=True)

    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNIEvents(request):
    events = NIEvent.objects.all()
    serializer = NIEventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNIEvent(request, nievent_id):
    events = NIEvent.objects.get(id=nievent_id)
    serializer = NIEventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getDecla(request, decla_id):
    events = Decla.objects.get(id=decla_id)
    serializer = DeclaSerializer(events, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def makeDecla(request):
    data = request.data
    decla = Decla.objects.create(
        owner=data["owner"],
        event=data["event"],
        content=data["content"],
        total=data["total"],
        present=data["present"],
        senate_year=data["senate_year"],
        receipt=data["receipt"],
        reunist=data["reunist"],
        kmters=data["kmters"],
        verwerkt=data["verwerkt"],
    )
    decla.save()
    serializer = DeclaSerializer(decla, many=False)
    return Response(serializer.data)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def NI_points(request, lid_id, nievent_id):
    event = Event.objects.get(id=nievent_id)
    user = Lid.objects.get(id=lid_id)
    data = request.data
    points, created = NIEvent.objects.get_or_create(
        event=event,
        lid=user,
    )
    points.points = data["value"]
    points.note = data["note"]

    points.save()
    serializer = NIEventSerializer(points, many=False)
    return Response(serializer.data)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def add_Document(request):
    # user = request.user.lid
    data = request.data
    doc = Document.objects.create(
        owner=Lid.objects.get(id=data["lid"]),
        name=data["name"],
        file=data["file"],
        senate_year=data["senate_year"],
        show=data["show"],
    )
    serializer = DocumentSerializer(doc, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def postDocument(request):
#     user = request.user.lid
#     document = Document.objects.create(
#         owner = user

#     )
#     serializer = DocumentSerializer(Document, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getProject(request, pk):
#     project = Project.objects.get(id=pk)
#     serializer = ProjectSerializer(project, many=False)
#     return Response(serializer.data)
