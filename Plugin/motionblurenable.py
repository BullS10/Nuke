#menu_scripts.addCommand("Enable Motion BLur", "import motionblurenable; motionblurenable.motionblur_enable()", "CTRL+M")


import nuke

def motionblur_enable():

	nodes = nuke.selectedNodes()
	for n in nodes:
		if n.Class() == 'Transform' :
			n['motionblur'].setValue(1)
			n['shutteroffset'].setValue(0)
		else :
			nuke.message("This is not a transform node")