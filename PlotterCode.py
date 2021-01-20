# https://community.ultimaker.com/topic/12270-plugin-to-replace-the-extrusion-g-code-with-my-laser-onoff-function-m126m127/?do=findComment&comment=270682
# Copyright (c) 2020 Belin Fieldson
# PlotterCode is released under the terms of the AGPLv3 or higher.

from ..Script import Script

class PlotterCode(Script):
    version = "1.00"
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Plotter Code v.(""" + self.version + """)",
            "key":"PlotterCode",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "_pen_down":
                {
                    "label": "Pen down",
                    "description": "The code to use to lower the pen",
                    "type": "str",
                    "default_value": "M107"
                },
                "_pen_up":
                {
                    "label": "Pen up",
                    "description": "The code to use to lift the pen",
                    "type": "str",
                    "default_value": "M106"
                },
                "_delay":
                {
                    "label": "Delay after pen up/down",
                    "description": "delay after lifting the pen before moving",
                    "type": "float",
                    "default_value": 0.3
                },
                "_pen_down_move":
                {
                    "label": "GCODE for Pen down move",
                    "description": "The gcode that activates pen down movement",
                    "type": "str",
                    "default_value": "G1"
                },
                "_pen_up_move":
                {
                    "label": "GCODE for Pen up move",
                    "description": "The gcode that activates pen up movement",
                    "type": "str",
                    "default_value": "G0"
                }
            }
        }"""

    def execute(self, data):
        pen_down           = self.getSettingValueByKey("_pen_down");
        pen_up             = self.getSettingValueByKey("_pen_up");
        pen_down_move      = self.getSettingValueByKey("_pen_down_move");
        pen_up_move        = self.getSettingValueByKey("_pen_up_move");
        pen_move_delay     = float(self.getSettingValueByKey("_delay"));
        is_pen_down        = True
        is_real_layer_data = False
        
        # Declare output gcode
        for layer in data:
            index    = data.index(layer)
            lines    = layer.split("\n")
            new_data = ""
            
            for line in lines:
                if (pen_down in line or pen_up in line):
                    line = ";" + line + " removed by PlotterCode"
                else:
                    if (pen_down_move in line):
                        pos = line.find('E')    # remove extruder parameter
                        if (pos > 0):
                            line = line[0:pos - 1]
                    
                    if (";LAYER:0" in line):    # real layer data started?
                        is_real_layer_data = True

                    if (is_real_layer_data):    # from real layer data
                        pos = line.find('Z')    # remove Z move parameter
                        if (pos > 0):
                            line = line[0:pos - 1]
                
                    if (pen_down_move in line and not is_pen_down):
                        newline = pen_down + "\n"
                        is_pen_down = True
                        if (pen_move_delay > 0):
                            newline += "G4 P" + str(pen_move_delay) + "\n"
                        line = newline + line
                            
                    if (pen_up_move in line and is_pen_down):
                        newline = pen_up + "\n"
                        is_pen_down = False
                        if (pen_move_delay > 0):
                            newline += "G4 P" + str(pen_move_delay) + "\n"
                        line = newline + line    
                    
                    if (";End of Gcode" in line):
                        line = pen_down + "\n" + line
                    
                new_data += line + "\n"
            data[index] = new_data

        return data