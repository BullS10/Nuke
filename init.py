###NukeSurvivalToolkit
nuke.pluginAddPath("./NukeSurvivalToolkit")

###nuke Stamps
import nuke
nuke.pluginAddPath("stamps")


###################
#Plugin path
nuke.pluginAddPath('./Plugin')

##Gizmo path
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')


# StickyNote
# StickyNote > default text size: 42pt 
nuke.knobDefault("StickyNote.note_font_size","42")


# Backdrop
# Backdrop > default text size: 42pt 
nuke.knobDefault("Backdrop.label",'''<center>''')
nuke.knobDefault("Backdrop.note_font_size","42")


# Copy
# Copy > default bbox set to A
nuke.knobDefault("Copy.bbox","A")


# ChannelMerge
# ChannelMerge > default bbox set to  A
nuke.knobDefault("ChannelMerge.bbox","A")
# ChannelMerge > label from operation
nuke.knobDefault("ChannelMerge.label",'[value operation]')
# ChannelMerge > label lifetime frame range
#nuke.knobDefault("ChannelMerge.label", "[value lifetimeStart] - [value lifetimeEnd]")

# Keymix
# Keymix > default bbox set to  B
nuke.knobDefault("Keymix.bbox","B")
# Keymix > channels -> rgba
nuke.knobDefault("Keymix.channels","rgb")
# Keymix > label lifetime frame range
#nuke.knobDefault("Keymix.label", "[value lifetimeStart] - [value lifetimeEnd]")

# Merge
# Merge > output only RGB
nuke.knobDefault("Merge.output","rgb")
# Merge > default bbox set to B
nuke.knobDefault("Merge.bbox", "B")
# Merge > label lifetime frame range
#nuke.knobDefault("Merge.label", "[value lifetimeStart] - [value lifetimeEnd]")


# Blur
# Blur -> Label Size
nuke.knobDefault("Blur.label",'[value size]')

# Erode Filter
# Erode Filter -> label size
nuke.knobDefault("FilterErode.label",'[value size]')


# Erode
# Erode -> label size
nuke.knobDefault("Erode.label",'[value size]')

# Laplacian
# Laplacian -> label size
nuke.knobDefault("Laplacian.label",'[value size]')

# Shuffle
# Shuffle > put the channel out in label
## nuke.knobDefault("Shuffle.label", '<font size = "5"> [value in]')
nuke.knobDefault("Shuffle.label", '[value in] -> [value out]')


# ShuffleCopy
# ShuffleCopy > put the channel out in label
## nuke.knobDefault("Shuffle.label", '<font size = "5"> [value in]')
nuke.knobDefault("ShuffleCopy.label", '[value in] -> [value out]')


# Colorspace
# Colorspace > put the Colorspace in/out in label
nuke.knobDefault("Colorspace.label", '[value colorspace_in] -> [value colorspace_out]')


# Switch
# Switch > 1 by default
nuke.knobDefault("Switch.which", "1")


# Noise
# Noise > Clip to BBox and not format
nuke.knobDefault("Noise.cliptype","bbox")


#Invert
#Invert > channels to Alpha and not RGBA
nuke.knobDefault("Invert.channels","alpha")

##Remove
##Remove > remove to keep rgba only
nuke.knobDefault("Remove.operation","keep")
nuke.knobDefault("Remove.channels","rgba")

##Tracker
##Tracker > label show reference frame

nuke.knobDefault("Tracker.label", '[value reference_frame]')

##Clamp
##Clamp > alpha
nuke.knobDefault("Clamp.channels","alpha")


##Stmap
##Stmap > channels
nuke.knobDefault("STMap.channels","rgba")
nuke.knobDefault("STMap.uv","rgb")

