import re
import random
from errbot import BotPlugin, botcmd, re_botcmd

CONFIG_TEMPLATE = {
    'HERO_NAMES_GROUP_1': ['Beat',
                        'Big',
                        'Blast',
                        'Bold',
                        'Bolt',
                        'Brick',
                        'Buck',
                        'Buff',
                        'Butch',
                        'Dean',
                        'Crud',
                        'Crunch',
                        'Burt',
                        'Dirk',
                        'Fist',
                        'Flint',
                        'Fridge',
                        'Gristle',
                        'Grind',
                        'Hack',
                        'Colt',
                        'Major',
                        'Fury',
                        'Lump',
                        'Punch',
                        'Duke',
                        'Blaze',
                        'Blade',
                        'Red',
                        'Punt',
                        'Reef',
                        'Roll',
                        'Rip',
                        'Grim',
                        'Jab',
                        'Slab',
                        'Scream',
                        'Coal',
                        'Slate',
                        'Smash',
                        'Fire',
                        'Smoke',
                        'Flash',
                        'Steel',
                        'Captain',
                        'Splint',
                        'Stump',
                        'Rage',
                        'Thick',
                        'Touch',
                        'Trunk',
                        'Whip',
                        'Zap'],
 'HERO_NAMES_GROUP_2': ['Punch',
                        'Large',
                        'Hard',
                        'Thick',
                        'Big',
                        'Vander',
                        'Crank',
                        'Plank',
                        'Drink',
                        'Doom',
                        'Dead',
                        'Pound',
                        'Knuckle',
                        'Bone',
                        'Savage',
                        'Butt',
                        'Fire',
                        'Razor',
                        'Rock',
                        'Iron',
                        'Grunt',
                        'Grim',
                        'Mad',
                        'Thorn',
                        'Blow',
                        'Beef',
                        'Wrestle',
                        'Terror',
                        'Side',
                        'Rubble',
                        'Speed',
                        'Lightning',
                        'Grit',
                        'Slap',
                        'Blast',
                        'Fizzle',
                        'Scar',
                        'Granite',
                        'Steak',
                        'Tazer',
                        'Snarl',
                        'Bulk',
                        'Dagger',
                        'Squat',
                        'SaberFist',
                        'Slab',
                        'Lamp',
                        'Cram',
                        'Cannon',
                        'Tussle',
                        'Man',
                        'Chest',
                        'Gut',
                        'Rumble',
                        'Fury',
                        'Chunk',
                        'Wreck',
                        'Nail',
                        'Run',
                        'Rust',
                        'Slam',
                        'Slag',
                        'Thunder',
                        'Hazzard'],
 'HERO_NAMES_GROUP_3': ['Beef',
                        'Huge',
                        'Cheese',
                        'Neck',
                        'Flank',
                        'Meat',
                        'Delt',
                        'Abs',
                        'Heart',
                        'Chest',
                        'Roar',
                        'Lots',
                        'Back',
                        'Nail',
                        'Lift',
                        'Fury',
                        'Meal',
                        'Stalk',
                        'Steak',
                        'Pec',
                        'Bone',
                        'Stag',
                        'Body',
                        'Fist',
                        'Broth',
                        'Groin',
                        'Shot',
                        'Cake',
                        'Iron',
                        'Chunk',
                        'Face',
                        'Head',
                        'Thrust',
                        'Crunch',
                        'Rock',
                        'Wad',
                        'Jaw',
                        'Muscle',
                        'Hair',
                        'Knob',
                        'man',
                        'Fast',
                        'Rod',
                        'Stone',
                        'Cheek',
                        'Lash']
    }

class MyHero(BotPlugin):
    """Generates lunky hunky hero names in the spirit of MST3k's running joke in their Space Mutiny episode"""
    min_err_version = '3.0.0' # Optional, but recommended

    HERO_NAMES_PREFIXES = ['Mc','von ']

    def get_configuration_template(self):
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super(MyHero, self).configure(config)

    def get_prefix(self):
        if not (random.randrange(0, 7) == 0): return ""
        return self.HERO_NAMES_PREFIXES[(random.randrange(0, 3) == 2)]

    def get_hero_name(self):
        # every once in a while, thrown one of these complete in-jokes
        if (random.randrange(0,100) == 50): return "Bob Johnson"
        if (random.randrange(0,250) == 50): return "Rowsdower"
        return "{n1} {p}{n2}{n3}".format(
            n1=random.choice(self.config['HERO_NAMES_GROUP_1']),
            p=self.get_prefix(),
            n2=random.choice(self.config['HERO_NAMES_GROUP_2']),
            n3=random.choice(self.config['HERO_NAMES_GROUP_3'])
        )

    @botcmd()
    def myhero(self, msg, args):
        """Generates a special hunky hero name for you"""
        return self.get_hero_name()

    @re_botcmd(pattern=r"space mutiny|hero", prefixed=False, flags=re.IGNORECASE)
    def listen_for_talk_of_heroes(self, msg, match):
        """Talk of heroes prompts a Space Hero Name..."""
        return self.get_hero_name()
