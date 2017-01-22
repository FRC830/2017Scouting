import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #', buttons=False)
    team_id = IntegerField('Team #', buttons=False)
    #Form Fields
    crossed_baseline = RadioField('Crossed Baseline',choices = [('Yes','Yes'),('No','No')], default='No')
    auton_gears = IntegerField('Gears Installed #', buttons=False)
    teleop_gears = IntegerField('Gears Installed #',buttons=False)
    hanging = RadioField('Did it hang?',choices = [('Yes','Yes'),('No','No')], default='No')
    
    auton_highgoal = IntegerField('Fuel in High goal',buttons=False)
    auton_lowgoal = IntegerField('Fuel in Low goal',buttons=False)
    teleop_highgoal = IntegerField('Fuel in High goal',buttons=False)
    teleop_lowgoal = IntegerField('Fuel in Low goal',buttons=False)
    
    auton_techfouls = IntegerField('Techfouls #', buttons=False)
    auton_fouls = IntegerField('Fouls #', buttons=False)
    teleop_techfouls = IntegerField('Techfouls #',buttons=False)
    teleop_fouls = IntegerField('Fouls #', buttons=False)

    missed_stuff = RadioField('Did you miss any fuel scoring?',choices = [('Yes','Yes'),('No','No')], default='No')
    comments = TextAreaField('', col_md=12)
