# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'


dropletSize=int(sys.argv[-3])
dimensionReduction=int(sys.argv[-2])
InputFile="./"+str(sys.argv[-1])
OutputFile= InputFile[0:-3]+'png'


paraview.simple._DisableFirstRenderCameraReset()



# create a new 'CSV Reader'
director_field_0csv = CSVReader(FileName=[InputFile])

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

## update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Table To Structured Grid'
tableToStructuredGrid1 = TableToStructuredGrid(Input=director_field_0csv)
## Properties modified on tableToStructuredGrid1
tableToStructuredGrid1.WholeExtent = [dropletSize/2 - 1, dropletSize/2+1, 0, dropletSize/dimensionReduction, 0, dropletSize/dimensionReduction]
tableToStructuredGrid1.XColumn = 'x'
tableToStructuredGrid1.YColumn = 'y'
tableToStructuredGrid1.ZColumn = 'z'
#
#
## update the view to ensure updated data information
spreadSheetView1.Update()

## create a new 'Slice'
slice1 = Slice(Input=tableToStructuredGrid1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

## init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin =[dropletSize/2 , dropletSize/(dimensionReduction*2), dropletSize/(dimensionReduction*2)]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]


## update the view to ensure updated data information
spreadSheetView1.Update()
#
## create a new 'Threshold'
threshold1 = Threshold(Input=slice1)
#
## Properties modified on threshold1
threshold1.Scalars = ['POINTS', 'S']
threshold1.ThresholdRange = [0.0, 0.95]


## update the view to ensure updated data information
spreadSheetView1.Update()

## create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'n'
calculator1.Function = 'nx*iHat+ny*jHat+nz*kHat'


## update the view to ensure updated data information
spreadSheetView1.Update()
#
## create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Cylinder')
glyph1.OrientationArray = ['POINTS', 'n']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 1.0
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

## Properties modified on glyph1.GlyphType
glyph1.GlyphType.Radius = 0.25
#
## Properties modified on glyph1.GlyphTransform
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]
#

## update the view to ensure updated data information
spreadSheetView1.Update()
#
## destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1
#


## find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
## uncomment following to set a specific view size
## renderView1.ViewSize = [1352, 799]
#
## set active view
SetActiveView(renderView1)
#
## set active source
SetActiveSource(glyph1)
#
## show data in view
glyph1Display = Show(glyph1, renderView1)
#
## trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.DiffuseColor = [1.0, 0.6666666666666666, 1.0]
glyph1Display.OSPRayScaleArray = 'Normals'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 10.111634457111359
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.5055817228555679
glyph1Display.SetScaleArray = ['POINTS', 'Normals']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Normals']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()


# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'S'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)


# get opacity transfer function/opacity map for 'S'
sPWF = GetOpacityTransferFunction('S')
sPWF.Points = [0.478, 0.0, 0.5, 0.0, 0.4780610203742981, 1.0, 0.5, 0.0]
sPWF.ScalarRangeInitialized = 1


# Rescale transfer function
sPWF.RescaleTransferFunction(0.2, 0.6)
layout1.SetSplitFraction(0, 0.50)


# get color transfer function/color map for 'S'
sLUT = GetColorTransferFunction('S')
sLUT.RGBPoints = [0.478, 0.231373, 0.298039, 0.752941, 0.47803051018714904, 0.865003, 0.865003, 0.865003, 0.4780610203742981, 0.705882, 0.0156863, 0.14902]
sLUT.ScalarRangeInitialized = 1.0



# get color legend/bar for sLUT in view renderView1
sLUTColorBar = GetScalarBar(sLUT, renderView1)
sLUTColorBar.AutoOrient = 1
sLUTColorBar.Orientation = 'Vertical'
sLUTColorBar.WindowLocation = 'LowerRightCorner'
sLUTColorBar.Position = [0.89, 0.02]
sLUTColorBar.Title = 'S'
sLUTColorBar.ComponentTitle = ''
sLUTColorBar.TitleJustification = 'Centered'
sLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
sLUTColorBar.TitleOpacity = 1.0
sLUTColorBar.TitleFontFamily = 'Arial'
sLUTColorBar.TitleBold = 0
sLUTColorBar.TitleItalic = 0
sLUTColorBar.TitleShadow = 0
sLUTColorBar.TitleFontSize = 10
sLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
sLUTColorBar.LabelOpacity = 1.0
sLUTColorBar.LabelFontFamily = 'Arial'
sLUTColorBar.LabelBold = 0
sLUTColorBar.LabelItalic = 0
sLUTColorBar.LabelShadow = 0
sLUTColorBar.LabelFontSize = 10
sLUTColorBar.AutomaticLabelFormat = 1
sLUTColorBar.LabelFormat = '%4.2f'
sLUTColorBar.DrawTickMarks = 1
sLUTColorBar.DrawTickLabels = 1
sLUTColorBar.UseCustomLabels = 0
sLUTColorBar.CustomLabels = []
sLUTColorBar.AddRangeLabels = 1
sLUTColorBar.RangeLabelFormat = '%4.2f'
sLUTColorBar.DrawAnnotations = 1
sLUTColorBar.AddRangeAnnotations = 0
sLUTColorBar.AutomaticAnnotations = 0
sLUTColorBar.DrawNanAnnotation = 0
sLUTColorBar.NanAnnotation = 'NaN'
sLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
sLUTColorBar.ScalarBarThickness = 10
sLUTColorBar.ScalarBarLength = 0.25



# current camera placement for renderView1
renderView1.CameraPosition = [dropletSize, dropletSize/(dimensionReduction*2), dropletSize/(dimensionReduction*2)]
renderView1.CameraFocalPoint = [ dropletSize/2, dropletSize/(dimensionReduction*2), dropletSize/(dimensionReduction*2)]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = dropletSize/(dimensionReduction*1.97)
renderView1.CameraParallelProjection = 1
renderView1.Background=[0.6,0.6,0.6]

# save screenshot
SaveScreenshot(OutputFile, renderView1, SaveAllViews=0,
    ImageResolution=[3052, 3052],
    FontScaling='Scale fonts proportionally',
    SeparatorWidth=0,
    SeparatorColor=[0.0, 0.0, 0.0],
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)


