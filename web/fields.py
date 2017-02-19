
import flask_wtf
import wtforms.validators
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #')
    team_id = IntegerField('Team #')
    #Form Fields
    crossed_baseline = CheckboxButtonField('Crossed baseline?', col_md=2)
    auton_gears = CheckboxButtonField('Gear installed?', col_md=2)
    auton_techfouls = IntegerField('Techfouls', default=0)
    auton_fouls = IntegerField('Fouls', default=0)
    auton_highgoal = IntegerField('Fuel in high goal', default=0)
    auton_lowgoal = IntegerField('Fuel in low goal', default=0)

    teleop_gears = IntegerField('Gears installed', default=0)
    pickup_gears = CheckboxButtonField('Can it pick up gears?', col_md=3)
    teleop_highgoal = IntegerField('Fuel in high goal', default=0)
    teleop_lowgoal = IntegerField('Fuel in low goal', default=0)
    pickup_fuel = CheckboxButtonField('Can it pick up fuel?', col_md=3)
    teleop_techfouls = IntegerField('Techfouls', default=0)
    teleop_fouls = IntegerField('Fouls', default=0)
    hanging = CheckboxButtonField('Did it hang?', col_md=3)
    defense = IntegerField("Rank defense 1-10", default=0, validators=[wtforms.validators.NumberRange(min=1,max=10)])
    comments = TextAreaField('', col_md=12)
