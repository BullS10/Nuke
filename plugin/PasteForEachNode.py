# Max van Leeuwen - maxvanleeuwen.com
# PasteForEachNode - 1.0
#
# Paste nodes from the clipboard for each currently selected node.


import nuke
from nukescripts import *


def PasteForEachNode():
	# make empty lists for selected nodes and new nodes
	selNodes = []
	newNodes = []

	# for each selected node, deselect it (but add it to the selected nodes list)
	for i in nuke.selectedNodes():
		selNodes.append(i)
		i['selected'].setValue(False)

	# for each node in the selected nodes list (which used to be selected)
	for i in selNodes:

		# temporarily select it
		i['selected'].setValue(True)

		# run nuke's built-in node paste script
		nuke.nodePaste(nukescripts.cut_paste_file())

		# deselect all selected nodes, but add them to the newnodes list
		for unselect in nuke.selectedNodes():
			newNodes.append(unselect)
			unselect['selected'].setValue(False)

	# reselect each node in the new nodes list
	for i in newNodes:
		i['selected'].setValue(True)


# autostart (if not imported)
if __name__ == "__main__":
	PasteForEachNode()