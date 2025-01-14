# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Novation_Impulse/__init__.py
# Compiled at: 2018-04-23 20:27:04
# Novation_Impulse2
from __future__ import absolute_import, print_function, unicode_literals
from .Novation_Impulse2 import Novation_Impulse2

def create_instance(c_instance):
    return Novation_Impulse2(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[
                         25], model_name='Impulse 25'), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 inport(props=[NOTES_CC, REMOTE]),
                 outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
