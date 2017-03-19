
import flask_wtf
import wtforms.validators
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #')
    team_id = IntegerField('Team #')
    #Form Fields
    crossed_baseline = CheckboxButtonField('Crossed baseline?', col_md=3)
    try_lft_auton_gears = CheckboxButtonField('Left gear attempted (failed)?', col_md=3)
    try_cen_auton_gears = CheckboxButtonField('Center gear attempted (failed)?', col_md=3)
    try_rgt_auton_gears = CheckboxButtonField('Right gear attempted (failed)?', col_md=3)
    lft_auton_gears = CheckboxButtonField('Left gear installed?', col_md=3)
    cen_auton_gears = CheckboxButtonField('Center gear installed?', col_md=3)
    rgt_auton_gears = CheckboxButtonField('Right gear installed?', col_md=3)
    auton_highgoal = IntegerField('Fuel in high goal', default=0)
    auton_lowgoal = IntegerField('Fuel in low goal', default=0)

    teleop_gears = IntegerField('Gears installed', default=0)
    pickup_gears = CheckboxButtonField('Get gears off ground?', col_md=3)
    dropped_gears = IntegerField('Gears dropped?', default=0)
    teleop_highgoal = IntegerField('Fuel in high goal', default=0)
    teleop_lowgoal = IntegerField('Fuel in low goal', default=0)
    caught_rope = CheckboxButtonField('Did it grab the rope?', col_md=3)
    hanging = CheckboxButtonField('Did it hang?', col_md=3)
    comments = TextAreaField('', col_md=12)
