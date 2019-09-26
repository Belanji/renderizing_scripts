#!/home/souzarf/Programas/ParaView/5.4.1/bin/pvbatch

#### import the simple module from the paraview
from paraview.simple import *
import sys

dropletSize=int(sys.argv[-2])
InputFile="./"+str(sys.argv[-1])
OutputFile= InputFile[0:-3]+'png'


SS=0.3

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
director_field_42csv = CSVReader(FileName=[InputFile])

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L


# show data in view
director_field_42csvDisplay = Show(director_field_42csv, spreadSheetView1)
director_field_42csvDisplay.FieldAssociation = 'Row Data'



renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
tableToStructuredGrid1 = TableToStructuredGrid(Input=director_field_42csv)
tableToStructuredGrid1.XColumn = 'x'
tableToStructuredGrid1.YColumn = 'y'
tableToStructuredGrid1.ZColumn = 'z'
tableToStructuredGrid1.WholeExtent = [0, dropletSize, 0, dropletSize, 0, dropletSize]

# reset view to fit data
renderView1.Update()
Hide(tableToStructuredGrid1, renderView1)

# create a new 'Contour'
contour1 = Contour(Input=tableToStructuredGrid1)
contour1.ContourBy = ['POINTS', 'S']
contour1.Isosurfaces = [SS]
contour1.PointMergeMethod = 'Uniform Binning'


# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [0.0, 0.0, 0.0]
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 8.897135416666668
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.GaussianRadius = 4.448567708333334
contour1Display.SetScaleArray = ['POINTS', 'P']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'P']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]


# update the view to ensure updated data information

renderView1.Update()

contour1Display = Show(contour1, renderView1)
# change solid color

contour1Display.DiffuseColor = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(tableToStructuredGrid1)

# get color transfer function/color map for 'S'
sLUT = GetColorTransferFunction('S')
sLUT.LockDataRange = 0
sLUT.InterpretValuesAsCategories = 0
sLUT.ShowCategoricalColorsinDataRangeOnly = 0
sLUT.RescaleOnVisibilityChange = 0
sLUT.EnableOpacityMapping = 0
sLUT.RGBPoints = [0.533, 0.231373, 0.298039, 0.752941, 0.5330610313415527, 0.865003, 0.865003, 0.865003, 0.5331220626831055, 0.705882, 0.0156863, 0.14902]
sLUT.UseLogScale = 0
sLUT.ColorSpace = 'Diverging'
sLUT.UseBelowRangeColor = 0
sLUT.BelowRangeColor = [0.0, 0.0, 0.0]
sLUT.UseAboveRangeColor = 0
sLUT.AboveRangeColor = [1.0, 1.0, 1.0]
sLUT.NanColor = [1.0, 1.0, 0.0]
sLUT.Discretize = 1
sLUT.NumberOfTableValues = 256
sLUT.ScalarRangeInitialized = 1.0
sLUT.HSVWrap = 0
sLUT.VectorComponent = 0
sLUT.VectorMode = 'Magnitude'
sLUT.AllowDuplicateScalars = 1
sLUT.Annotations = []
sLUT.ActiveAnnotatedValues = []
sLUT.IndexedColors = []


# get color transfer function/color map for 'GlyphScale'
glyphScaleLUT = GetColorTransferFunction('GlyphScale')
glyphScaleLUT.RGBPoints = [0.14000000059604645, 0.231373, 0.298039, 0.752941, 0.31199999898672104, 0.865003, 0.865003, 0.865003, 0.48399999737739563, 0.705882, 0.0156863, 0.14902]
glyphScaleLUT.ScalarRangeInitialized = 1.0


sPWF = GetOpacityTransferFunction('S')
sPWF.Points = [0.14, 0.0, 0.5, 0.0, 0.484, 1.0, 0.5, 0.0]
sPWF.ScalarRangeInitialized = 1

# Rescale transfer function
sPWF.RescaleTransferFunction(0.0, 0.6)

# get color legend/bar for sLUT in view renderView1
sLUTColorBar = GetScalarBar(sLUT, renderView1)
sLUTColorBar.Title = 'S'
sLUTColorBar.ComponentTitle = ''
sLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
sLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# change scalar bar placement
sLUTColorBar.WindowLocation = 'AnyLocation'
sLUTColorBar.Position = [0.75, 0.015037593984962405]








# create a new 'Slice'
slice1 = Slice(Input=tableToStructuredGrid1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.SliceType.Origin = [50.0, 50.0, 50.0]


# create a new 'Threshold'
threshold1 = Threshold(Input=slice1)
threshold1.Scalars = ['POINTS', 'S']
threshold1.ThresholdRange = [0.0, 0.9]


# create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'n'
calculator1.Function = 'nx*iHat+ny*jHat+nz*kHat'


# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Cylinder')
glyph1.Scalars = ['POINTS', 'S']
glyph1.Vectors = ['POINTS', 'n']
glyph1.ScaleFactor = 1.0
glyph1.GlyphMode = 'All Points'
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]
glyph1.GlyphType.Height = 0.9
glyph1.GlyphType.Radius = 0.25


# show data in view
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.AmbientColor = [0.0, 0.0, 0.0]
glyph1Display.ColorArrayName = ['POINTS', 'GlyphScale']
glyph1Display.LookupTable = glyphScaleLUT
glyph1Display.OSPRayScaleArray = 'GlyphScale'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'GlyphVector'
glyph1Display.ScaleFactor = 1.
glyph1Display.SelectScaleArray = 'S'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'S'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.GaussianRadius = 5.049871079623699
glyph1Display.SetScaleArray = ['POINTS', 'GlyphScale']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'GlyphScale']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# show color bar/color legend

ColorBy(glyph1Display, ('POINTS', 'S'))


# current camera placement for renderView1
renderView1.CameraPosition = [dropletSize, dropletSize/2, dropletSize/2]
renderView1.CameraFocalPoint = [ dropletSize/2, dropletSize/2, dropletSize/2]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = dropletSize/(1.97)
renderView1.CameraParallelProjection = 1

sLUT.RescaleTransferFunction(0.0, 0.6)
# save screenshot
SaveScreenshot('/home/souzarf/x_plane.png', renderView1, ImageResolution=[3076, 3076],FontScaling='Scale fonts proportionally',
    SeparatorWidth=0,
    SeparatorColor=[0.0, 0.0, 0.0],
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)


Hide(glyph1, renderView1)












SetActiveSource(tableToStructuredGrid1)

# create a new 'Slice'
slice2 = Slice(Input=tableToStructuredGrid1)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]
slice2.SliceType.Origin = [50.0, 50.0, 50.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]


# create a new 'Threshold'
threshold2 = Threshold(Input=slice2)
threshold2.Scalars = ['POINTS', 'S']
threshold2.ThresholdRange = [0.0, 0.9]

# create a new 'Calculator'
calculator2 = Calculator(Input=threshold2)
calculator2.ResultArrayName = 'n'
calculator2.Function = 'nx*iHat+ny*jHat+nz*kHat'

# create a new 'Glyph'
glyph2 = Glyph(Input=calculator2,
    GlyphType='Cylinder')
glyph2.Scalars = ['POINTS', 'S']
glyph2.Vectors = ['POINTS', 'n']
glyph2.ScaleFactor = 1.0
glyph2.GlyphMode = 'All Points'
glyph2.GlyphTransform = 'Transform2'
glyph2.GlyphType.Height = 0.9
glyph2.GlyphType.Radius = 0.25
glyph2.GlyphTransform.Rotate = [0.0, 0.0, 90.0]

# get color transfer function/color map for 'GlyphScale'
glyphScaleLUT = GetColorTransferFunction('GlyphScale')
glyphScaleLUT.RGBPoints = [0.14000000059604645, 0.231373, 0.298039, 0.752941, 0.31199999898672104, 0.865003, 0.865003, 0.865003, 0.48399999737739563, 0.705882, 0.0156863, 0.14902]
glyphScaleLUT.ScalarRangeInitialized = 1.0

# show data in view
glyph2Display = Show(glyph2, renderView1)
# trace defaults for the display properties.
glyph2Display.Representation = 'Surface'
glyph2Display.AmbientColor = [0.0, 0.0, 0.0]
glyph2Display.ColorArrayName = ['POINTS', 'GlyphScale']
glyph2Display.LookupTable = glyphScaleLUT
glyph2Display.OSPRayScaleArray = 'GlyphScale'
glyph2Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph2Display.SelectOrientationVectors = 'GlyphVector'
glyph2Display.ScaleFactor = 10.099742159247398
glyph2Display.SelectScaleArray = 'GlyphScale'
glyph2Display.GlyphType = 'Arrow'
glyph2Display.GlyphTableIndexArray = 'GlyphScale'
glyph2Display.DataAxesGrid = 'GridAxesRepresentation'
glyph2Display.PolarAxes = 'PolarAxesRepresentation'
glyph2Display.GaussianRadius = 5.049871079623699
glyph2Display.SetScaleArray = ['POINTS', 'GlyphScale']
glyph2Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph2Display.OpacityArray = ['POINTS', 'GlyphScale']
glyph2Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]


# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph2Display, ('POINTS', 'S'))

SetActiveSource(glyph2)
# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(glyphScaleLUT, renderView1)
glyph2Display.SetScalarBarVisibility(renderView1, True)

# current camera placement for renderView1
renderView1.CameraPosition = [dropletSize/2, dropletSize, dropletSize/2]
renderView1.CameraFocalPoint = [ dropletSize/2, dropletSize/2, dropletSize/2]
renderView1.CameraViewUp = [1.0, 0.0, 0.0]
renderView1.CameraParallelProjection = 1


sLUT.RescaleTransferFunction(0.0, 0.6)
# save screenshot
SaveScreenshot('/home/souzarf/y_plane.png', renderView1, ImageResolution=[3076, 3076],FontScaling='Scale fonts proportionally',
    SeparatorWidth=0,
    SeparatorColor=[0.0, 0.0, 0.0],
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)


Hide(glyph2, renderView1)


# set active source
SetActiveSource(tableToStructuredGrid1)

# create a new 'Slice'
slice3 = Slice(Input=tableToStructuredGrid1)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]
slice3.SliceType.Origin = [50.0, 50.0, 50.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]


# create a new 'Threshold'
threshold3 = Threshold(Input=slice3)
threshold3.Scalars = ['POINTS', 'S']
threshold3.ThresholdRange = [0.0, 0.9]


# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator3 = Calculator(Input=threshold3)
calculator3.ResultArrayName = 'n'
calculator3.Function = 'nx*iHat+ny*jHat+nz*kHat'


# create a new 'Glyph'
glyph3 = Glyph(Input=calculator3,
    GlyphType='Cylinder')
glyph3.Scalars = ['POINTS', 'S']
glyph3.Vectors = ['POINTS', 'n']
glyph3.ScaleFactor = 1.0
glyph3.GlyphMode = 'All Points'
glyph3.GlyphTransform = 'Transform2'
glyph3.GlyphTransform.Rotate = [0.0, 0.0, 90.0]
glyph3.GlyphType.Height = 0.9
glyph3.GlyphType.Radius = 0.25


# show data in view
glyph3Display = Show(glyph3, renderView1)
# trace defaults for the display properties.
glyph3Display.Representation = 'Surface'
glyph3Display.AmbientColor = [0.0, 0.0, 0.0]
glyph3Display.ColorArrayName = ['POINTS', 'S']
glyph3Display.LookupTable = sLUT
glyph3Display.OSPRayScaleArray = 'GlyphScale'
glyph3Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph3Display.SelectOrientationVectors = 'GlyphVector'
glyph3Display.ScaleFactor = 1.
glyph3Display.SelectScaleArray = 'GlyphScale'
glyph3Display.GlyphTableIndexArray = 'GlyphScale'
glyph3Display.DataAxesGrid = 'GridAxesRepresentation'
glyph3Display.PolarAxes = 'PolarAxesRepresentation'
glyph3Display.GaussianRadius = 5.050078421831131
glyph3Display.SetScaleArray = ['POINTS', 'GlyphScale']
glyph3Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph3Display.OpacityArray = ['POINTS', 'GlyphScale']
glyph3Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
glyph3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
glyph3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
glyph3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
glyph3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]


ColorBy(glyph3Display, ('POINTS', 'S'))


# current camera placement for renderView1
renderView1.CameraPosition = [dropletSize/2,dropletSize/2 ,dropletSize]
renderView1.CameraFocalPoint = [dropletSize/2,dropletSize/2,dropletSize/2]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraParallelScale = dropletSize/(1.97)
renderView1.CameraParallelProjection = 1
sLUT.RescaleTransferFunction(0.0, 0.6)
# save screenshot

sLUT.RescaleTransferFunction(0.0, 0.6)
# save screenshot
SaveScreenshot('/home/souzarf/z_plane.png', renderView1, ImageResolution=[3076, 3076],FontScaling='Scale fonts proportionally',
    SeparatorWidth=0,
    SeparatorColor=[0.0, 0.0, 0.0],
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)
