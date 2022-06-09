# Create your views here.


from datetime import datetime, date, time
import doctest
from django.http import JsonResponse
from .utils import future_events, paginateEvents, searchEvents
from finance.models import Decla
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.forms import LidForm
from .serializers import (
    DeclaSerializer,
    DocumentSerializer,
    DsaniSerializer,
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
        {"GET": API_URL + "/events"},
        {"PUT": API_URL + "/event/id"},
        {"POST": API_URL + "/event"},
        {"POST": API_URL + "/addevents"},
        # {"POST": API_URL + "/event/id"},
        # {"POST": API_URL + "/NIEvent/id"},
        # {"GET": API_URL + "/NIEvent/lid_id/nievent_id"},
        # {"GET": API_URL + "/NIEvents"},
        # {"GET": API_URL + "/documents"},
        # {"POST": API_URL + "/decla"},
        # {'GET': API_URL+'/document/id'},
        # {"POST": API_URL + "/add_document"},
    ]
    return Response(routes)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getLeden(request):
    leden = Lid.objects.filter(active=True)
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
# @permission_classes([IsAuthenticated])
def getEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk).delete()
    # serializer = EventSerializer(event, many=False)
    return Response()


@api_view(["PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def editEvent(request, pk):
    data = request.data
    event = Event.objects.get(id=pk)
    event.summary = data["summary"] or ""
    event.description = data["description"] or ""
    event.start_date = date.fromisoformat(data["start_date"]) or ""
    event.start_time = time.fromisoformat(data["start_time"]) or ""
    event.end_date = date.fromisoformat(data["end_date"]) or ""
    event.end_time = time.fromisoformat(data["end_time"]) or ""
    event.recuring = data["recuring"] or ""
    event.location = data["location"] or ""
    event.kartrekkers = data["kartrekkers"] or ""
    event.info = data["info"] or ""
    event.budget = data["budget"] or ""
    event.bijzonderheden = data["bijzonderheden"] or ""
    kokers = set(data["kokers"])

    event.save()
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(["POST", "GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def addEvents(request):
    data = request.data
    event = Event.objects.create(
        summary=data["summary"] or "",
        description=data["description"] or "",
        start_date=date.fromisoformat(data["start_date"]) or "",
        start_time=time.fromisoformat(data["start_time"]) or "",
        end_date=date.fromisoformat(data["end_date"]) or "",
        end_time=time.fromisoformat(data["end_time"]) or "",
        recuring=data["recuring"] or "",
        location=data["location"] or "",
        kartrekkers=data["kartrekkers"] or "",
        info=data["info"] or "",
        budget=data["budget"] or "",
        bijzonderheden=data["bijzonderheden"] or "",
        # kokers=data["kokers"] or [],
    )
    event.save()
    # print("saved")
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getDsaniS(request, pagenum=None):
    if pagenum:events = paginateEvents(request, page=pagenum, results=20)
    else: events= Event.objects.all()
    serializer = DsaniSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getDsani(request, nievent_id):
    events = NIEvent.objects.get(id=nievent_id)
    serializer = NIEventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def editDsani(request, nievent_id):
    event = NIEvent.objects.get(id=nievent_id)
    event.note = request.data["note"]
    event.points = request.data["points"]
    event.save()
    serializer = NIEventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteDsani(request, nievent_id):
    events = NIEvent.objects.get(id=nievent_id).delete()
    return Response()


@api_view(["GET"])
def getDecla(request, decla_id):
    events = Decla.objects.get(id=decla_id)
    serializer = DeclaSerializer(events, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def makeDecla(request):
    data = request.data
    print(data)
    decla = Decla.objects.create(
        owner=Lid.objects.get(id=data["owner"]),
        event=Event.objects.get(id=data["event"]),
        content=data["content"] or None,
        total=data["total"] or None,
        present=data["present"],
        senate_year=data["senate_year"] or None,
        receipt=data["receipt"] or None,
        reunist=data["reunist"] or None,
        kmters=data["kmters"] or None,
        verwerkt=data["verwerkt"] or None,
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
