# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys
import numpy as np

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
print sys.argv[1],'->',sys.argv[2]

DirectorScale=float(sys.argv[3])
FractionOfPoints=float(sys.argv[4])


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


NumberOfPoints= calculator1.PointData.GetArray("nx").GetNumberOfTuples()

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Cylinder')
glyph1.OrientationArray = ['POINTS', 'n']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = DirectorScale
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution'
glyph1.MaximumNumberOfSamplePoints = int(NumberOfPoints*FractionOfPoints)
glyph1.Seed = 12121

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
glyph1Display.ScaleFactor = 4.500537884235382
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.2250268942117691
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

# get color transfer function/color map for 'S'
sLUT = GetColorTransferFunction('S')
sLUT.RGBPoints = [0.53286, 0.231373, 0.298039, 0.752941, 0.532921025686264, 0.865003, 0.865003, 0.865003, 0.5329820513725281, 0.705882, 0.0156863, 0.14902]
sLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'S'
sPWF = GetOpacityTransferFunction('S')
sPWF.Points = [0.53286, 0.0, 0.5, 0.0, 0.5329820513725281, 1.0, 0.5, 0.0]
sPWF.ScalarRangeInitialized = 1


Xmin,Xmax,Ymin,Ymax,Zmin,Zmax =calculator1.GetDataInformation().GetBounds()

deltaX=Xmax-Xmin
deltaY=Ymax-Ymin
deltaZ=Zmax-Zmin
deltaM=max(deltaX,deltaY,deltaZ)

Xavg=(Xmax+Xmin)/2
Yavg=(Ymax+Ymin)/2
Zavg=(Zmax+Zmin)/2

AspectRatio=deltaY/deltaX

renderView1.OrientationAxesVisibility = 1
glyph1Display.RescaleTransferFunctionToDataRange(True, True)
# current camera placement for renderView1

renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [Xavg,Yavg,Zavg+deltaM/2.]
renderView1.CameraFocalPoint = [Xavg,Yavg,Zavg]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraParallelProjection = 1
renderView1.CameraParallelScale = AspectRatio*deltaM/1.95


renderView1.Background = [.65, .65, .65]
# save screenshot

ImageRessX=4000
ImageRessY=int(ImageRessX*AspectRatio)
SaveScreenshot(sys.argv[2], renderView1, ImageResolution=[ImageRessX, ImageRessY],
    FontScaling='Do not scale fonts')

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
