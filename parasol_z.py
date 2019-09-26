#!/dados/Renato/ParaView/5.6.0/bin/pvbatch
# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
print sys.argv[1],'->',sys.argv[2]

directorScale=float(sys.argv[3])
# create a new 'CSV Reader'

cutycsv =  CSVReader(FileName=[sys.argv[1]])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=cutycsv)
tableToPoints1.XColumn = 'x'
tableToPoints1.YColumn = 'y'
tableToPoints1.ZColumn = 'z'

# Properties modified on tableToPoints1

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1058, 487]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=tableToPoints1)
calculator1.ResultArrayName = 'n'
calculator1.Function = 'nx*iHat+ny*jHat+nz*kHat'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Cylinder')
glyph1.OrientationArray = ['POINTS', 'n']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = directorScale
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.Radius = 0.2

# Properties modified on glyph1.GlyphTransform
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]

# show data in view
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.OSPRayScaleArray = 'Normals'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 0.000002
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.3003814271092415
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

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'S'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 's'
sLUT = GetColorTransferFunction('S')

# get opacity transfer function/opacity map for 's'
sPWF = GetOpacityTransferFunction('S')

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [28, 28,10024.5]
renderView1.CameraFocalPoint = [55,50,50]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraParallelScale = 29.176521789806596
renderView1.ResetCamera()

renderView1.Background = [0.7,0.7,0.7]
# save screenshot
SaveScreenshot(sys.argv[2], renderView1, ImageResolution=[1300,1000],
    FontScaling='Do not scale fonts')

