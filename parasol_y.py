#!/dados/Renato/ParaView/5.6.0/bin/pvbatch


# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
print sys.argv[1],'->',sys.argv[2],
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
glyph1Display.ScaleFactor = 6.00762854218483
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

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'S'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)
# get color transfer function/color map for 'S'
sLUT = GetColorTransferFunction('S')
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
sLUTColorBar.TitleBold = 1
sLUTColorBar.TitleItalic = 0
sLUTColorBar.TitleShadow = 0
sLUTColorBar.TitleFontSize = 20
sLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
sLUTColorBar.LabelOpacity = 1.0
sLUTColorBar.LabelFontFamily = 'Arial'
sLUTColorBar.LabelBold = 1
sLUTColorBar.LabelItalic = 0
sLUTColorBar.LabelShadow = 0
sLUTColorBar.LabelFontSize = 20
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
sLUTColorBar.ScalarBarThickness = 20
sLUTColorBar.ScalarBarLength = .25

# get opacity transfer function/opacity map for 'S'
sPWF = GetOpacityTransferFunction('s')

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# current camera placement for renderView1
renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [55, 50, 50]
renderView1.CameraFocalPoint = [55,500,50]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
#renderView1.CameraParallelScale = z*0.9
renderView1.ResetCamera()

renderView1.Background = [0.7,0.7,0.7]
# save screenshot
SaveScreenshot(sys.argv[2], renderView1, ImageResolution=[1300, 1000],
    FontScaling='Do not scale fonts')

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
