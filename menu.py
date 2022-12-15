import nuke

##Dot in straight corner
import Dots

toolbar = nuke.toolbar("Nodes")
toolbar.addCommand('Other/DotU','Dots.DotU()','shift+`')
toolbar.addCommand('Other/DotD','Dots.DotD()','ctrl+`')

##hotbox
import W_hotbox, W_hotboxManager

##FrameHold on current frame
nuke.menu('Nodes').addCommand( "Time/FrameHold", "nuke.createNode('FrameHold')['first_frame'].setValue(nuke.frame())", icon='FrameHold.png')

##FrameHold_current
def frameHold_current():
    n=nuke.selectedNode()
    if n.Class() == "FrameHold":
        n['first_frame'].setValue(nuke.frame())
    else :
        pass

nuke.menu('Nuke').addCommand( 'Edit/frameHold_current', frameHold_current, "shift+f")

##Transform = motion blur 1 + shutter offset centered
#menu_scripts.addCommand("Enable Motion BLur", "import motionblurenable; motionblurenable.motionblur_enable()", "CTRL+M")



##setLabel
import setLabel
nuke.menu('Nuke').addCommand( 'Edit/setLabel', 'setLabel.setLabel()', "shift+n")


##CloseFloating windows
def CloseFloating():
    for n in nuke.allNodes():
        n.hideControlPanel()

nuke.menu('Nodes').addCommand('Other/CloseFloating',CloseFloating,'alt+q')


##autocrop
import autoCrop_MB
nuke.menu( 'Nuke' ).addCommand( 'Extra/Run Auto Crop on Selected', autoCrop_MB.autoCrop_MB )



##readTools
import readTools

#Python menu
nuke.menu( 'Nuke' ).addCommand( 'Extra/readTools/Select Read Nodes', 'readTools.selectRead()', index=0)
nuke.menu( 'Nuke' ).addCommand( 'Extra/readTools/Set nodes localization', 'readTools.setLocalize()')
nuke.menu( 'Nuke' ).addCommand( 'Extra/readTools/Set read nodes frame range', 'readTools.setFrameRange()')
nuke.menu( 'Nuke' ).addCommand( 'Extra/readTools/Missing frames setting', 'readTools.setError()')



##autobackdrop Black & white
from autoBackdropBW import autoBackdropBW
toolbar = nuke.menu('Nodes')
toolbar.addCommand('Other/Backdrop', 'autoBackdropBW()', 'alt+b', icon='Backdrop.png')



###Offbranch
import Offbranch
nuke.menu('Nuke').addCommand('Extra/Offbranch', "Offbranch.Offbranch()", "shift+g", shortcutContext=2)


##Shortcut for different Merge
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Divide', 'nuke.createNode("Merge2", "operation divide", False)', "alt+'", shortcutContext=2)
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Multiply', 'nuke.createNode("Merge2", "operation multiply", False)', "'", shortcutContext=2)
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('Plus', 'nuke.createNode("Merge2", "operation plus", False)', ",", shortcutContext=2)
nuke.menu('Nodes').addMenu('Merge/Merges').addCommand('From', 'nuke.createNode("Merge2", "operation from", False)', "alt+,", shortcutContext=2)


#noViewer at nuke startUp
# def killViewers():
#     for v in nuke.allNodes("Viewer"):
#         nuke.delete(v)
# nuke.addOnScriptLoad(killViewers)


##font Size increase
def font_increase():
    for i in nuke.selectedNodes():
        size = i['note_font_size'].getValue() + 10
        i['note_font_size'].setValue(size)

nuke.menu('Nuke').addCommand( 'Edit/font_size_increase', font_increase, "ctrl+]")

##font Size decrease
def font_decrease():
    for i in nuke.selectedNodes():
        size = i['note_font_size'].getValue() - 10
        i['note_font_size'].setValue(size)
nuke.menu('Nuke').addCommand( 'Edit/font_size_decrease', font_decrease, "ctrl+[")


##size_increase
def size_increase():
    for i in nuke.selectedNodes():
        if i['size'].getValue() < -9 or i['size'].getValue() > 9  :
            newsize = i['size'].getValue() + 10
        else :
            newsize = i['size'].getValue() + 1
            
        i['size'].setValue(newsize)

nuke.menu('Nuke').addCommand( 'Edit/size_increase', size_increase, "alt+]")


##size_increase
def size_decrease():
    for i in nuke.selectedNodes():
        if i['size'].getValue() < -9 or i['size'].getValue() > 9  :
            newsize = i['size'].getValue() - 10
        else :
            newsize = i['size'].getValue() - 1

        i['size'].setValue(newsize)

nuke.menu('Nuke').addCommand( 'Edit/size_decrease', size_decrease, "alt+[")


##Toggle between opposite operation in transform and Merge
def operationSwitcher():
    node = nuke.selectedNode()
    merge_ops = {'stencil': 'mask', 'over': 'under', 'from': 'plus', 'out': 'in', 'multiply': 'divide'}
    if node.Class() == "Merge2":
        current_op = node['operation'].value()
        if current_op in merge_ops.keys():
            node['operation'].setValue(merge_ops[node['operation'].value()])
        elif current_op in merge_ops.values():
            node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])

    if node.Class() == "Transform":
        if node.knob('invert_matrix').value() == 1:
           node.knob('invert_matrix').setValue(0)
           node['label'].setValue("Matchmove")
        else :
           node.knob('invert_matrix').setValue(1)
           node['label'].setValue("Stabilize")

    if node.Class() == "Log2Lin":
        if node.knob('operation').value() == 'lin2log':
           node.knob('operation').setValue('log2lin')
        else :
           node.knob('operation').setValue('lin2log')


    if node.Class() == "CornerPin2D":
        if node.knob('invert').value() == 1:
           node.knob('invert').setValue(0)
           node['label'].setValue("Matchmove")
        else :
           node.knob('invert').setValue(1)
           node['label'].setValue("Stabilize")


nuke.menu('Nuke').addCommand( 'Edit/Switch Operation', operationSwitcher, "alt+l")


##Cornerpin Relative/Absolute
import cornerpin_set_relative
nuke.menu('Nuke').addCommand('Extra/set cornerpin to relative','cornerpin_set_relative.setCornerpinToRelative()','alt+v',icon='CornerPin.png')


##bm_ViwerToggle
import bm_ViewerToggle
nuke.menu("Viewer").addCommand("Toggle Viewer Gain & Gamma", 'bm_ViewerToggle.bm_ViewerToggle()', "shift+h")
nuke.menu("Nuke").addCommand("Viewer/Toggle Viewer Gain & Gamma", 'bm_ViewerToggle.bm_ViewerToggle()', "shift+h")

##bm_NodeSandwich
import bm_NodeSandwich
nuke.menu('Nodes').addCommand('Color/Log Sandwich', 'bm_NodeSandwich.bm_NodeSandwich("Log2Lin", "Log2Lin")', "ctrl+shift+l", icon="bm_NodeSandwich.png")
nuke.menu('Nodes').addCommand('Merge/Premult Sandwich', 'bm_NodeSandwich.bm_NodeSandwich("Unpremult", "Premult")', "ctrl+shift+p", icon="bm_NodeSandwich.png")

##X_Tools
##m = toolbar.addMenu("X_Tools", icon="X_Tools.png")






##PushNodes
push_menu = nuke.menu('Nuke').addMenu('Extra/Push')  # Adjust to match your setup.

push_menu.addCommand(
     'Down',
     'from nuke_move_nodes import push_nodes; push_nodes.push(down=True)',
     'ctrl+PgDown',
     shortcutContext=2  # Remove this line for Nuke < 9
)
push_menu.addCommand(
     'Up',
     'from nuke_move_nodes import push_nodes; push_nodes.push(up=True)',
     'ctrl+PgUp',
     shortcutContext=2  # Remove this line for Nuke < 9
)
push_menu.addCommand(
     'Left',
     'from nuke_move_nodes import push_nodes; push_nodes.push(left=True)',
     'ctrl+-',
     shortcutContext=2
)
push_menu.addCommand(
     'Right',
     'from nuke_move_nodes import push_nodes; push_nodes.push(right=True)',
     'ctrl+=',
     shortcutContext=2
)






#######SmoothScrub viewer Hack
# use smooth scrubbing (temporarily playing at 0fps)
useSmooth = True

# scrub only in timeline, as opposed to taking over mouse anywhere in viewer
timelineScrubOnly = False

# speed multiplier for scrubbing (1.0x = full frame range start-end in width of viewer)
scrubSpeed = 2.0

# keyboard shortcut
shortcutKey = "Ctrl+Space"


# load into nukeunder 'Viewer' right-click context
import SmoothScrub
nuke.menu('Viewer').addCommand('Smooth Scrub', lambda: SmoothScrub.SmoothScrub(useSmooth, timelineScrubOnly, scrubSpeed), shortcutKey)


import KnobScripter
