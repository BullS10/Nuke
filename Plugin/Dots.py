############### copy this in menu.py########################

# import Dots
# toolbar = nuke.toolbar("Nodes")
# toolbar.addCommand('Other/DotU','Dots.DotU()','shift+`')
# toolbar.addCommand('Other/DotD','Dots.DotD()','ctrl+`')

############################################################



import nuke
###create dot on upper side

def DotU():
	node=[]
	for s in nuke.selectedNodes():
		node.append(s)
	one=node[0]
	two=node[1]
	dot = nuke.nodes.Dot()
	node.append(dot)
	nxs = two.screenWidth()
	nys = one.screenHeight()
	nxp = two.xpos() + nxs/2
	nyp = one.ypos() + nys/2
	dot.setXpos(nxp)
	dot.setYpos(nyp)
	dot.setInput(0,one)
	nuke.autoplaceSnap(dot)

	if two.Class() == ("Merge2"):
	    two.setInput(1,dot)
	elif two.Class() == ("ChannelMerge"):
	    two.setInput(1,dot)
	elif two.Class() == ("ShuffleCopy"):
	    two.setInput(1,dot)
	elif two.Class() == ("Keymix"):
	    two.setInput(1,dot)
	elif two.Class() == ("Addmix"):
	    two.setInput(1,dot)
	elif two.Class() == ("CopyBBox"):
	    two.setInput(1,dot)
	elif two.Class() == ("Switch"):
	    two.setInput(1,dot)
	elif two.Class() == ("Dissolve"):
	    two.setInput(1,dot)
	elif two.Class() == ("Blend"):
	    two.setInput(1,dot)
	elif two.Class() == ("Copy"):
	    two.setInput(1,dot)
	else:
	    two.setInput(0,dot)

	for sel in node:
	    sel['selected'].setValue(True)



###create dot on down side
def DotD():
	node=[]
	for s in nuke.selectedNodes():
		node.append(s)
	one=node[0]
	two=node[1]
	dot = nuke.nodes.Dot()
	node.append(dot)
	nxs = one.screenWidth()
	nys = two.screenHeight()
	nxp = one.xpos() + nxs/2
	nyp = two.ypos() + nys/2
	dot.setXpos(nxp)
	dot.setYpos(nyp)
	dot.setInput(0,one)
	nuke.autoplaceSnap(dot)

	if two.Class() == ("Merge2"):
	    two.setInput(1,dot)
	elif two.Class() == ("ChannelMerge"):
	    two.setInput(1,dot)
	elif two.Class() == ("ShuffleCopy"):
	    two.setInput(1,dot)
	elif two.Class() == ("Keymix"):
	    two.setInput(1,dot)
	elif two.Class() == ("Addmix"):
	    two.setInput(1,dot)
	elif two.Class() == ("CopyBBox"):
	    two.setInput(1,dot)
	elif two.Class() == ("Switch"):
	    two.setInput(1,dot)
	elif two.Class() == ("Dissolve"):
	    two.setInput(1,dot)
	elif two.Class() == ("Blend"):
	    two.setInput(1,dot)
	elif two.Class() == ("Copy"):
	    two.setInput(1,dot)
	else:
	    two.setInput(0,dot)

	for sel in node:
		sel['selected'].setValue(True)
