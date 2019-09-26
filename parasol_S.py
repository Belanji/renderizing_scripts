#!/dados/Renato/ParaView/5.6.0/bin/pvbatch
# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
print sys.argv[1],'->',sys.argv[2]

# create a new 'XML Unstructured Grid Reader'
time_48vtu = XMLUnstructuredGridReader(FileName=[sys.argv[1]])
time_48vtu.PointArrayStatus = ['S', 'P', 'n']


Smin, Smax= time_48vtu.PointData.GetArray("S").GetRange()
Sdefect=(0.9*Smax)

print "Smax=",Smax, ", Smin=",Smin
print "Sdefect=", Sdefect

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1405, 799]

# show data in view
time_48vtuDisplay = Show(time_48vtu, renderView1)

# trace defaults for the display properties.
time_48vtuDisplay.Representation = 'Surface'
time_48vtuDisplay.ColorArrayName = [None, '']
time_48vtuDisplay.OSPRayScaleArray = 'P'
time_48vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
time_48vtuDisplay.SelectOrientationVectors = 'None'
time_48vtuDisplay.ScaleFactor = 9.999999999999998e-08
time_48vtuDisplay.SelectScaleArray = 'None'
time_48vtuDisplay.GlyphType = 'Arrow'
time_48vtuDisplay.GlyphTableIndexArray = 'None'
time_48vtuDisplay.GaussianRadius = 4.9999999999999985e-09
time_48vtuDisplay.SetScaleArray = ['POINTS', 'P']
time_48vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
time_48vtuDisplay.OpacityArray = ['POINTS', 'P']
time_48vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
time_48vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
time_48vtuDisplay.SelectionCellLabelFontFile = ''
time_48vtuDisplay.SelectionPointLabelFontFile = ''
time_48vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
time_48vtuDisplay.ScalarOpacityUnitDistance = 2.9167437658633457e-08

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
time_48vtuDisplay.DataAxesGrid.XTitleFontFile = ''
time_48vtuDisplay.DataAxesGrid.YTitleFontFile = ''
time_48vtuDisplay.DataAxesGrid.ZTitleFontFile = ''
time_48vtuDisplay.DataAxesGrid.XLabelFontFile = ''
time_48vtuDisplay.DataAxesGrid.YLabelFontFile = ''
time_48vtuDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
time_48vtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
time_48vtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
time_48vtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
time_48vtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# change solid color
time_48vtuDisplay.DiffuseColor = [1.0, 0.0, 0.4980392156862745]

# Properties modified on time_48vtuDisplay
time_48vtuDisplay.Opacity = 0.48

# Properties modified on time_48vtuDisplay
time_48vtuDisplay.Opacity = 0.4

# create a new 'Contour'
contour1 = Contour(Input=time_48vtu)
contour1.ContourBy = ['POINTS', 'P']
contour1.Isosurfaces = [-0.1286960671394213]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'S']
contour1.Isosurfaces = [Sdefect]

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 8.062689798816957e-08
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = 4.031344899408479e-09
contour1Display.SetScaleArray = ['POINTS', 'Normals']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'Normals']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# change solid color
contour1Display.DiffuseColor = [0.0, 0.3333333333333333, 1.0]

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 3.3460652149512314e-06]
renderView1.CameraParallelScale = 8.660254037844385e-07

# save screenshot
SaveScreenshot(sys.argv[2], renderView1, ImageResolution=[2810, 1596])
