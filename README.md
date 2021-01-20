# cura_plugin

## PlotterCode.py
**cura plugin for Plotter using 3D printer**
 - pen movement with cooling fan (eliminating z and extruder movements)
 - lift pen up when fan is on and drop pen down when fan is off
 - pen up is added before moving with G0
 - pen down is added before moving with G1
 - delay for pen movement can be added
 - copy it to C:\Program Files\Ultimaker Cura 4.8.0\plugins\PostProcessingPlugin\scripts\
<img src="https://github.com/PingguSoft/cura_plugin/blob/main/pics/PlotterCode_1.png?raw=true" width="40%">

**hardware**
 - pen is moved up and down by using fan signal to speed up
 - pen is moved by solenoid and gravity and move up when solenoid is on (=fan is on)
<img src="https://github.com/PingguSoft/3dp_hotplug_tools/blob/main/pics/3dp_hotplug_tools_pinout_plotter.png?raw=true" width="50%">
<img src="https://github.com/PingguSoft/3dp_hotplug_tools/blob/main/pics/3dp_hotplug_tools_plotter_1.png?raw=true" width="50%">
<img src="https://github.com/PingguSoft/3dp_hotplug_tools/blob/main/pics/3dp_hotplug_tools_plotter_2.png?raw=true" width="50%">
https://github.com/PingguSoft/3dp_hotplug_tools