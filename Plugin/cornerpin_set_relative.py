
#--------------------------------------------------------------------
#	cornerpin_set_relative.py
#	Created by Gaetan Verheyen
#	Version: 1.0.0
#	Last updated: October 27th 2019
#--------------------------------------------------------------------
import nuke

def setCornerpinToRelative():
	#variables
	myCornerpin = nuke.selectedNode()
	ref = str(nuke.frame())
	#copy to 
	myCornerpin['from1'].setExpression('to1')
	myCornerpin['from2'].setExpression('to2')
	myCornerpin['from3'].setExpression('to3')
	myCornerpin['from4'].setExpression('to4')

	#kill animation on from
	myCornerpin['from1'].clearAnimated()
	myCornerpin['from2'].clearAnimated()
	myCornerpin['from3'].clearAnimated()
	myCornerpin['from4'].clearAnimated()
	#set label
	myCornerpin['label'].setValue("ref"+ str(ref))

