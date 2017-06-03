from beckett.resources import BaseResource


class PokemonResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon'
        resource_name = 'pokemon'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'national_id',
            'abilities',
            'egg_groups',
            'evolutions',
            'descriptions',
            'moves',
            'types',
            'catch_rate',
            'species',
            'hp',
            'attack',
            'defense',
            'name',
            'sp_atk',
            'sp_def',
            'speed',
            'total',
            'egg_cycles',
            'ev_yield',
            'exp',
            'growth_rate',
            'height',
            'weight',
            'happiness',
            'male_female_ratio',
            'sprites',
        )
