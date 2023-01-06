import datetime
from django.db import models
import json
import ast

# All game models are defined here

# Models are :
# - Game : with an id, a date, game type (id of the game type), and number of players
# - GameType : with an id (0 for no game type), a name, a description (rules)
# - ShotType : with an id, a number (25 for center), a multiplier, a GPIO custom pin
# - Shot : with an id, a game id, a player id, a shot type
# - Rule : with an id, a game type id, a type (0 : dummy init, 1 : reset value each turn, 2 : condition and action each shot, 3 : winning condition), and a value (value to run)

class GameType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateTimeField('time')
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    nb_players = models.IntegerField(default=1)
    player = models.IntegerField(default=0)
    dummy_as_text = models.TextField(default="{}")
    total_points_as_text = models.TextField(default="[]")
    
    @staticmethod
    def end():
        # Start a new game
        return Game.create(nb_players = Game.current().nb_players, game_type_id = 0)
    
    @staticmethod
    def create(nb_players = 1, game_type_id = 0):        
        self = Game(
            date = datetime.datetime.now(),
            game_type = GameType.objects.get(pk=game_type_id),
            nb_players = nb_players,
            total_points_as_text = json.dumps([0 for i in range(nb_players)])
        )
        
        self.load_vars()
        
        for raw_rule in Rule.objects.filter(game_type=self.game_type, _type=0):
            exec(raw_rule.value)
        
        self.save_vars()
        self.save()
        
        return self
    
    

    @staticmethod
    def current():
        return Game.objects.order_by('-date')[0]

    def test_next_turn(self, shot):
        for raw_rule in Rule.objects.filter(game_type=self.game_type, _type=2):
            rule = ast.literal_eval(raw_rule.value)
            if eval(rule[0]):
                exec(rule[1])
                if rule[2] == 1:
                    return True
                elif rule[2] == 2:
                    return False
        
        return False
            
    def apply_next_turn(self):
        for raw_rule in Rule.objects.filter(game_type=self.game_type, _type=1):
            exec(raw_rule.value)
        self.player = (self.player + 1) % self.nb_players
        

    def winning(self):
        for raw_rule in Rule.objects.filter(game_type=self.game_type, _type=3):
            if eval(raw_rule.value):
                return True
        
        return False
    
    def save_vars(self):
        self.dummy_as_text = json.dumps(self.dummy)
        self.total_points_as_text = json.dumps(self.total_points)
        self.save()
    
    def load_vars(self):
        self.dummy = json.loads(self.dummy_as_text)
        self.total_points = json.loads(self.total_points_as_text)
    
    def shot_done(self, shot):
        self.load_vars()
        p = self.player
        
        if self.game_type.id == 0:
            return p
        
        next = self.test_next_turn(shot)
        
        if self.winning():
            self.save_vars()
            self.end()
            return p
        
        if next:
            self.apply_next_turn()
        
        self.save_vars()
        return p
    

class ShotType(models.Model):
    number = models.IntegerField()
    multiplier = models.IntegerField(default=1)
    gpio_pins = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Shot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET(0))
    player = models.IntegerField(default=1)
    shot_type = models.ForeignKey(ShotType, on_delete=models.CASCADE)
    
    @property
    def points(self):
        return self.shot_type.multiplier * self.shot_type.number
    
    def __init__(self, gpio):
        # Handle error if gpio is not a list
        
        super().__init__()
        
        self.shot_type = ShotType.objects.get(gpio_pins=gpio)
        self.game = Game.current()
        self.player = self.game.shot_done(self)
        
        self.save()

class Rule(models.Model):
    """_summary_ : This class is used to define rules to exec for a game type.

    :param models: for type (value template): 
        - 0 : dummy init (dummy.name = value)
        - 1 : reset value each turn (dummy.name = value)
        - 2 : condition and action each shot ([condition, action, {0 : continue code, 1 : returns true, 2 : returns false}])
        - 3 : winning condition (condition), each condition is a or of the others
    """
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    _type = models.CharField(max_length=100) # Shot turn, point, end of game, etc.
    value = models.CharField(max_length=500) # Value to run
        