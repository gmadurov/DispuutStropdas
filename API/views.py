# Create your views here.


from datetime import date, datetime, time

from agenda.models import AgendaClient, Event, NIEvent
from django.http import JsonResponse
from documents.models import Document
from finance.models import Boekstuk, Decla
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.forms import LidForm
from users.models import Lid

from .serializers import (
    BoekstukSerializer,
    DeclaSerializer,
    DocumentSerializer,
    DsaniSerializer,
    EventSerializer,
    LidSerializer,
    NIEventSerializer,
)
from .utils import future_events, paginateEvents, searchEvents

API_URL = "/api/"


def senate_jaar():
    date = datetime.today()
    month = int(date.strftime("%m"))
    year = int(date.strftime("%Y")) - 1990
    if month >= 9:
        out = year + 1
    else:
        out = year
    return out


def ledenlist():
    leden = {}
    for lid in Lid.objects.all():
        leden[lid.initials.lower()] = lid.id
        leden[lid.name.lower()] = lid.id
        try:
            leden[lid.name.split()[0].lower()] = lid.id
            leden[lid.initials.split()[1].lower()] = lid.id
        except:
            pass
        try:
            leden[lid.name.split()[1].lower()] = lid.id
        except:
            pass
    return leden


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET": API_URL + "leden/"},
        {"GET": API_URL + "leden/id"},
        # {"PUT": API_URL + "leden/id"},
        {"GET": API_URL + "events/"},
        {"POST": API_URL + "events/"},
        {"GET": API_URL + "events/id"},
        {"PUT": API_URL + "events/id"},
        {"DELETE": API_URL + "events/id"},
        {"GET": API_URL + "dsani/"},
        {"GET": API_URL + "dsani/pages/<int:pagenum>"},
        {"GET": API_URL + "dsani/id"},
        {"GET": API_URL + "users/token/"},
        {"GET": API_URL + "users/token/refresh/"},
        # {"POST": API_URL + "event/id"},
        # {"POST": API_URL + "NIEvent/id"},
        # {"GET": API_URL + "NIEvent/lid_id/nievent_id"},
        # {"GET": API_URL + "NIEvents"},
        # {"GET": API_URL + "documents"},
        {"GET": API_URL + "decla/"},
        {"POST": API_URL + "decla/"},
        {"GET": API_URL + "decla/id"},
        # {'GET': API_URL+'/document/id'},
        # {"POST": API_URL + "/add_document"},
    ]
    return Response(routes)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getLeden(request):
    # try: print(request.user.lid)
    # except: pass
    leden = Lid.objects.filter(active=True)
    serializer = LidSerializer(leden, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])  # , "POST"
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
@permission_classes([IsAuthenticated])
def getDocuments(request):
    docs = Document.objects.all()
    serializer = DocumentSerializer(docs, many=True)

    return Response(serializer.data)


# path("events/", views.getEvents),
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def getEvents(request):
    if request.method == "GET":
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        data = request.data
        event = Event.objects.create(
            summary=data["summary"] or "",
            description=data["description"] or "",
            start_date=date.fromisoformat(
                data["start_date"] or date.today().isoformat()
            )
            or date.today(),
            start_time=time.fromisoformat(data["start_time"]),
            end_date=date.fromisoformat(data["end_date"] or date.today().isoformat())
            or date.today(),
            end_time=time.fromisoformat(data["end_time"]),
            recuring=data["recuring"] or "",
            location=data["location"] or "",
            kartrekkers=data["kartrekkers"] or "",
            info=data["info"] or "",
            budget=data["budget"] or "",
            bijzonderheden=data["bijzonderheden"] or "",
            # kokers=data["kokers"] or [],
        )
        if data["kokers"]:
            event.kokers.set([Lid.objects.get(id=lid) for lid in data["kokers"]])
        event.save()
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)


# path("events/<str:pk>", views.getEvent),
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def getEvent(request, pk):
    if request.method == "GET":
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
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
        if data["kokers"]:
            event.kokers.set([Lid.objects.get(id=lid) for lid in data["kokers"]])

        event.save()
        serializer = EventSerializer(instance=event)
        return Response(serializer.data)
    if request.method == "DELETE":
        event = Event.objects.get(id=pk).delete()
        # serializer = EventSerializer(event, many=False)
        return Response()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Dsani(request, pagenum=None):
    if pagenum:
        events = paginateEvents(request, page=pagenum, results=20)
    else:
        events = Event.objects.all()
    serializer = DsaniSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def boekstuken(request):
    if request.method == "GET":
        bookstuk = Boekstuk.objects.all()
        serializer = BoekstukSerializer(bookstuk, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        print(request.data)
        bookstuk = Boekstuk.objects.create(name=request.data["name"])
        serializer = BoekstukSerializer(bookstuk, many=False)
        return Response(serializer.data)


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def getDsani(request, nievent_id):
    if request.method == "GET":
        events = NIEvent.objects.get(id=nievent_id)
        serializer = NIEventSerializer(events, many=True)
        return Response(serializer.data)
    if request.method == "PUT":
        event = NIEvent.objects.get(id=nievent_id)
        event.note = request.data["note"]
        event.points = request.data["points"]
        event.save()
        serializer = NIEventSerializer(event, many=False)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def getDeclas(request):
    if request.method == "GET":
        events = Decla.objects.all()
        serializer = DeclaSerializer(events, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        data = request.data
        print(request.user)
        print(data)
        decla = Decla.objects.create(
            owner=Lid.objects.get(id=data["owner"]),
            event=Event.objects.get(id=data["event"]),
            content=data["content"] or "",
            total=data["total"] or 0,
            senate_year=senate_jaar(),
            receipt=data["receipt"] or None,
            reunist=data["reunist"] or 0,
            kmters=data["kmters"] or 0,
            verwerkt=True
                if data["verwerkt"] == "true" and "verwerkt" in data.keys()
                else False,
            boekstuk=Boekstuk.objects.get(id=data["boekstuk"]),
        )
        if "present" in data.keys():
            decla.present.set(
                [Lid.objects.get(id=lid) for lid in data["present"].split(",")]
            )
        # print(10)
        decla.save()
        serializer = DeclaSerializer(decla, many=False)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def getDecla(request, decla_id):
    decla = Decla.objects.get(id=decla_id)
    try:
        if request.method == "GET":
            serializer = DeclaSerializer(decla, many=False)
            return Response(serializer.data)

        if request.method == "PUT":

            data = request.data
            # print(data)
            if "event" in data.keys():
                decla.event = (
                    Event.objects.get(id=data["event"]["id"])
                    if type(data["event"]) == dict
                    else Event.objects.get(id=data["event"])
                )
            # print(1)
            # print("content")
            decla.content = (
                data["content"] if "content" in data.keys() else decla.content
            )
            # print("total")
            decla.total = data["total"] if "total" in data.keys() else decla.total
            # print("senate_year")
            decla.senate_year = senate_jaar() or decla.senate_year
            # print("reunist")
            decla.reunist = (
                data["reunist"] if "reunist" in data.keys() else decla.reunist
            )
            # print("kmters")
            decla.kmters = data["kmters"] if "kmters" in data.keys() else decla.kmters
            # print("verwerkt")
            decla.verwerkt = (
                True
                if data["verwerkt"] == "true" and "verwerkt" in data.keys()
                else False
            )
            if "receipt" in data.keys():
                decla.receipt = data["receipt"] or decla.receipt
            if "boekstuk" in data.keys():
                if data["boekstuk"] != None:
                    decla.boekstuk = (
                        Boekstuk.objects.get(id=data["boekstuk"]) or decla.boekstuk
                    )
            if "present" in data.keys():
                decla.present.set(
                    [Lid.objects.get(id=int(lid)) for lid in data["present"].split(",") if lid != '']
                )
            decla.save()
            serializer = DeclaSerializer(decla, many=False)
            return Response(serializer.data)
        if request.method == "DELETE":
            serializer = DeclaSerializer(decla, many=False)
            decla.delete()
            return Response(serializer.data)
    except Exception as e:
        print(e)


# @api_view(["POST"])
# def makeDecla(request):
#     data = request.data
#     print(data)
#     decla = Decla.objects.create(
#         owner=Lid.objects.get(id=data["owner"]),
#         event=Event.objects.get(id=data["event"]),
#         content=data["content"] or None,
#         total=data["total"] or None,
#         present=data["present"],
#         senate_year=data["senate_year"] or None,
#         receipt=data["receipt"] or None,
#         reunist=data["reunist"] or None,
#         kmters=data["kmters"] or None,
#         verwerkt=data["verwerkt"] or None,
#     )
#     decla.save()
#     serializer = DeclaSerializer(decla, many=False)
#     return Response(serializer.data)


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
