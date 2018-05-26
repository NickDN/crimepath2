import simplejson as simplejson
from django.shortcuts import render
from django.http import HttpResponse
from hello.graph import G
import osmnx as ox
import networkx as nx
from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def get_shortest_path(request):
    hour = 19
    longitude_original = float(request.GET.get('longitude_original'))
    latitude_original = float(request.GET.get('latitude_original'))

    longitude_destination = float(request.GET.get('longitude_destination'))
    latitude_destination = float(request.GET.get('latitude_destination'))
    # origin_point = (37.789, -122.41)
    origin_point = (longitude_original, latitude_original)
    #  destination_point = (37.789, -122.41)
    destination_point = (longitude_destination, latitude_destination)
    origin_node = ox.get_nearest_node(G, origin_point)
    destination_node = ox.get_nearest_node(G, destination_point)
    #path = nx.shortest_path(G, origin_node, destination_node, weight='h{0}'.format(hour))
    path = nx.shortest_path(G, origin_node, destination_node, weight='h19')
    #path = nx.shortest_path(G, origin_node, destination_node)

    print(G.node[path[0]])
    nodes = []
    for node in path:
        nodes.append(G.node[node])
    json_stuff = simplejson.dumps({"nodes": nodes})
    return HttpResponse(json_stuff, content_type="application/json")
