import nuke

def setLabel():
	
	'''Quick edit the label for the selected node'''
	
	try:
		sn = nuke.selectedNodes()[-1]
		snLabel = sn['label'].value()
		snName = sn.name()
	except:
		sn = None
		return
	
	p = nuke.Panel( 'Edit Label' )
	p.setTitle( 'Label: %s' % snName )
	p.setWidth( 350 )
	p.addSingleLineInput('Label', snLabel)
	result = p.show()
	
	if result:
		label = p.value('Label')
		try:
			sn['label'].setValue(label)
		except:
			return