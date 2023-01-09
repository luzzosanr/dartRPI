from django.http import HttpResponse
from memory.models import Shot, Game, GameType, Rule
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def add_shot(request):
    print(request.GET['gpio'])
    shot = Shot(request.GET['gpio'])
    return Response({"points" : shot.points})

@api_view(['GET'])
def start_game(request):
    try:
        Game.create(nb_players = 2, game_type_id = 1)
    except ValueError:
        return Response({"status" : "Error: nb_players and game_type must be integers must be an integer"})
    return Response({"status" : "Game Started"})

@api_view(['GET'])
def get_game_types(request):
    return Response({"game_types" : GameType.objects.all()})

@api_view(['GET'])
def new_game_type(request):
    gameType = GameType(name = request.GET['name'], description = request.GET['description'])
    gameType.save()
    
    for rule in request.GET['rules']:
        rule = Rule(game_type = gameType, _type = rule['type'], value = rule['value'])
        rule.save()
    
    return Response({"status" : "Game Type Created"})

@api_view(['GET'])
def current_game(request):
    return Response({"player" : Game.current().player, "score" : Game.current().total_points_as_text, "dummy" : Game.current().dummy_as_text})
    print(f"player : {Game.current().player}, total_points : {Game.current().total_points_as_text}")
    return HttpResponse(f"total_points : {Game.current().total_points_as_text}")

@api_view(['GET'])
def last_shot(request):
    return Response({"shot" : Shot.objects.order_by('-id')[0]})

@api_view(['GET'])
def fake_shot(request):
    shot = Shot(111)
    return Response({"points" : shot.points})