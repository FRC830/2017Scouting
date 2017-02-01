import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #')
    team_id = IntegerField('Team #')
    #Form Fields
    crossed_baseline = CheckboxButtonField('Crossed Baseline?', col_md=2)
    auton_gears = CheckboxButtonField('Gear Installed?', col_md=2)
    teleop_gears = IntegerField('Gears Installed', default=0)
    hanging = CheckboxButtonField('Did it hang?', col_md=4)
    
    auton_highgoal = IntegerField('Fuel in High goal', default=0)
    auton_lowgoal = IntegerField('Fuel in Low goal', default=0)
    teleop_highgoal = IntegerField('Fuel in High goal', default=0)
    teleop_lowgoal = IntegerField('Fuel in Low goal', default=0)
    
    auton_techfouls = IntegerField('Techfouls', default=0)
    auton_fouls = IntegerField('Fouls', default=0)
    teleop_techfouls = IntegerField('Techfouls', default=0)
    teleop_fouls = IntegerField('Fouls', default=0)

    missed_stuff = CheckboxButtonField('Did you fall asleep?', col_md=3)
    comments = TextAreaField('', col_md=12)
