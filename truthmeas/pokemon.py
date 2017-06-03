def dict_creator(json_list, key_type):
    return {typep['name']: typep['resource_uri'] for typep in json_list[key_type]}


class DateObject(object):
    def __init__(self, json_list):
        self.name = json_list['name']
        self.resource_uri = json_list['resource_uri']
        self.created = json_list['created']
        self.modified = json_list['modified']


class Pokemon(DateObject):
    def __init__(self, json_list):
        super(Pokemon, self).__init__(json_list)
        self.id = json_list['national_id']
        self.abilities = dict_creator(json_list, 'abilities')
        self.egg_groups = dict_creator(json_list, 'egg_groups')
        self.evolutions = {
            f['to']: f['resource_uri'] for f in json_list['evolutions']}
        self.descriptions = dict_creator(json_list, 'descriptions')
        self.moves = dict_creator(json_list, 'moves')
        self.types = dict_creator(json_list, 'types')
        self.catch_rate = json_list['catch_rate']
        self.species = json_list['species']
        self.hp = json_list['hp']
        self.attack = json_list['attack']
        self.defense = json_list['defense']
        self.sp_atk = json_list['sp_atk']
        self.sp_def = json_list['sp_def']
        self.speed = json_list['speed']
        self.total = json_list['total']
        self.egg_cycles = json_list['egg_cycles']
        self.ev_yield = json_list['ev_yield']
        self.exp = json_list['exp']
        self.growth_rate = json_list['growth_rate']
        self.height = json_list['height']
        self.weight = json_list['weight']
        self.happiness = json_list['happiness']
        self.male_female_ratio = json_list['male_female_ratio']
        self.sprites = dict_creator(json_list, 'sprites')

    def __repr__(self):
        return '<Pokemon - %s>' % self.name.capitalize()
