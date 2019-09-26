#!/home/souzarf/Programas/ParaView/5.4.1/bin/pvbatch

#### import the simple module from the paraview
from paraview.simple import *
import sys


dropletSize=int(sys.argv[-3])
dimensionReduction=int(sys.argv[-2])
InputFile="./"+str(sys.argv[-1])
OutputFile= InputFile[0:-3]+'png'


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
a0csv = CSVReader(FileName=[InputFile])
a0csv.DetectNumericColumns = 1
a0csv.UseStringDelimiter = 1
a0csv.HaveHeaders = 1
a0csv.FieldDelimiterCharacters = ','
a0csv.MergeConsecutiveDelimiters = 0


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1513, 798]

# Properties modified on renderView1
renderView1.CameraParallelProjection = 1

# Properties modified on renderView1
renderView1.HiddenLineRemoval = 1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.UseCache = 0
spreadSheetView1.ViewSize = [400, 400]
spreadSheetView1.CellFontSize = 9
spreadSheetView1.HeaderFontSize = 9
spreadSheetView1.SelectionOnly = 0
spreadSheetView1.GenerateCellConnectivity = 0
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.SelectedComponent = -1
spreadSheetView1.InvertOrder = 0
spreadSheetView1.BlockSize = 1024L
spreadSheetView1.ColumnVisibility = []

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
a0csvDisplay = Show(a0csv, spreadSheetView1)
# trace defaults for the display properties.
a0csvDisplay.FieldAssociation = 'Row Data'
a0csvDisplay.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Table To Structured Grid'
tableToStructuredGrid1 = TableToStructuredGrid(Input=a0csv)
tableToStructuredGrid1.WholeExtent = [0, 200, 0, 200, 0, 200]
tableToStructuredGrid1.XColumn = 'P'
tableToStructuredGrid1.YColumn = 'P'
tableToStructuredGrid1.ZColumn = 'P'

# Properties modified on tableToStructuredGrid1
tableToStructuredGrid1.WholeExtent = [0, dropletSize/(dimensionReduction),  0, dropletSize/(dimensionReduction), dropletSize/2 -1 , dropletSize/2+1]
tableToStructuredGrid1.XColumn = 'x'
tableToStructuredGrid1.YColumn = 'y'
tableToStructuredGrid1.ZColumn = 'z'

# show data in view
tableToStructuredGrid1Display = Show(tableToStructuredGrid1, spreadSheetView1)
# trace defaults for the display properties.
tableToStructuredGrid1Display.FieldAssociation = 'Point Data'
tableToStructuredGrid1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(a0csv, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=tableToStructuredGrid1)
slice1.SliceType = 'Plane'
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [dropletSize/(dimensionReduction*2), dropletSize/(dimensionReduction*2), dropletSize/2]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]
slice1.SliceType.Offset = 0.0

# show data in view
slice1Display = Show(slice1, spreadSheetView1)
# trace defaults for the display properties.
slice1Display.FieldAssociation = 'Point Data'
slice1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=slice1)
calculator1.AttributeMode = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'n'
calculator1.Function = 'nx*iHat+ny*jHat+nz*kHat'
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0

# show data in view
calculator1Display = Show(calculator1, spreadSheetView1)
# trace defaults for the display properties.
calculator1Display.FieldAssociation = 'Point Data'
calculator1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(slice1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Threshold'
threshold1 = Threshold(Input=calculator1)
threshold1.Scalars = ['POINTS', 'P']
threshold1.ThresholdRange = [0.0, 0.0]
threshold1.AllScalars = 1
threshold1.UseContinuousCellRange = 0

# Properties modified on threshold1
threshold1.Scalars = ['POINTS', 'S']
threshold1.ThresholdRange = [0.0, 0.94396]

# show data in view
threshold1Display = Show(threshold1, spreadSheetView1)
# trace defaults for the display properties.
threshold1Display.FieldAssociation = 'Point Data'
threshold1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=threshold1,
    GlyphType='Cylinder')
glyph1.Scalars = ['POINTS', 's']
glyph1.Vectors = ['POINTS', 'n']

glyph1.ScaleFactor = 1.0
glyph1.GlyphType.Radius = 0.25
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]
glyph1.Orient = 1
glyph1.ScaleMode = 'off'
glyph1.GlyphMode = 'All Points'
glyph1.GlyphTransform = 'Transform2'


# init the 'Transform2' selected for 'GlyphTransform'
glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]
# Properties modified on glyph1.GlyphType
#glyph1.GlyphType.Radius = 0.25

# Properties modified on glyph1.GlyphTransform


glyph1Display = Show(glyph1, spreadSheetView1)
glyph1Display.FieldAssociation = 'Point Data'
glyph1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(glyph1)

# get color transfer function/color map for 'GlyphScale'
glyphScaleLUT = GetColorTransferFunction('GlyphScale')
glyphScaleLUT.LockDataRange = 0
glyphScaleLUT.InterpretValuesAsCategories = 0
glyphScaleLUT.ShowCategoricalColorsinDataRangeOnly = 0
glyphScaleLUT.RescaleOnVisibilityChange = 0
glyphScaleLUT.EnableOpacityMapping = 0
glyphScaleLUT.RGBPoints = [0.5329999923706055, 0.231373, 0.298039, 0.752941, 0.5330610275268555, 0.865003, 0.865003, 0.865003, 0.5331220626831055, 0.705882, 0.0156863, 0.14902]
glyphScaleLUT.UseLogScale = 0
glyphScaleLUT.ColorSpace = 'Diverging'
glyphScaleLUT.UseBelowRangeColor = 0
glyphScaleLUT.BelowRangeColor = [0.0, 0.0, 0.0]
glyphScaleLUT.UseAboveRangeColor = 0
glyphScaleLUT.AboveRangeColor = [1.0, 1.0, 1.0]
glyphScaleLUT.NanColor = [1.0, 1.0, 0.0]
glyphScaleLUT.Discretize = 1
glyphScaleLUT.NumberOfTableValues = 256
glyphScaleLUT.ScalarRangeInitialized = 1.0
glyphScaleLUT.HSVWrap = 0
glyphScaleLUT.VectorComponent = 0
glyphScaleLUT.VectorMode = 'Magnitude'
glyphScaleLUT.AllowDuplicateScalars = 1
glyphScaleLUT.Annotations = []
glyphScaleLUT.ActiveAnnotatedValues = []
glyphScaleLUT.IndexedColors = []

# show data in view
glyph1Display_1 = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display_1.Representation = 'Surface'
glyph1Display_1.AmbientColor = [1.0, 1.0, 1.0]
glyph1Display_1.ColorArrayName = ['POINTS', 'GlyphScale']
glyph1Display_1.DiffuseColor = [1.0, 1.0, 1.0]
glyph1Display_1.LookupTable = glyphScaleLUT
glyph1Display_1.MapScalars = 1
glyph1Display_1.InterpolateScalarsBeforeMapping = 1
glyph1Display_1.Opacity = 1.0
glyph1Display_1.PointSize = 2.0
glyph1Display_1.LineWidth = 1.0
glyph1Display_1.Interpolation = 'Gouraud'
glyph1Display_1.Specular = 0.0
glyph1Display_1.SpecularColor = [1.0, 1.0, 1.0]
glyph1Display_1.SpecularPower = 100.0
glyph1Display_1.Ambient = 0.0
glyph1Display_1.Diffuse = 1.0
glyph1Display_1.EdgeColor = [0.0, 0.0, 0.5]
glyph1Display_1.BackfaceRepresentation = 'Follow Frontface'
glyph1Display_1.BackfaceAmbientColor = [1.0, 1.0, 1.0]
glyph1Display_1.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
glyph1Display_1.BackfaceOpacity = 1.0
glyph1Display_1.Position = [0.0, 0.0, 0.0]
glyph1Display_1.Scale = [1.0, 1.0, 1.0]
glyph1Display_1.Orientation = [0.0, 0.0, 0.0]
glyph1Display_1.Origin = [0.0, 0.0, 0.0]
glyph1Display_1.Pickable = 1
glyph1Display_1.Texture = None
glyph1Display_1.Triangulate = 0
glyph1Display_1.NonlinearSubdivisionLevel = 1
glyph1Display_1.UseDataPartitions = 0
glyph1Display_1.OSPRayUseScaleArray = 0
glyph1Display_1.OSPRayScaleArray = 'GlyphScale'
glyph1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_1.Orient = 0
glyph1Display_1.OrientationMode = 'Direction'
glyph1Display_1.SelectOrientationVectors = 'GlyphVector'
glyph1Display_1.Scaling = 0
glyph1Display_1.ScaleMode = 'No Data Scaling Off'
glyph1Display_1.ScaleFactor = 6.0594621211290365
glyph1Display_1.SelectScaleArray = 'GlyphScale'
glyph1Display_1.GlyphType = 'Arrow'
glyph1Display_1.UseGlyphTable = 0
glyph1Display_1.GlyphTableIndexArray = 'GlyphScale'
glyph1Display_1.UseCompositeGlyphTable = 0
glyph1Display_1.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display_1.SelectionCellLabelBold = 0
glyph1Display_1.SelectionCellLabelColor = [0.0, 1.0, 0.0]
glyph1Display_1.SelectionCellLabelFontFamily = 'Arial'
glyph1Display_1.SelectionCellLabelFontSize = 18
glyph1Display_1.SelectionCellLabelItalic = 0
glyph1Display_1.SelectionCellLabelJustification = 'Left'
glyph1Display_1.SelectionCellLabelOpacity = 1.0
glyph1Display_1.SelectionCellLabelShadow = 0
glyph1Display_1.SelectionPointLabelBold = 0
glyph1Display_1.SelectionPointLabelColor = [1.0, 1.0, 0.0]
glyph1Display_1.SelectionPointLabelFontFamily = 'Arial'
glyph1Display_1.SelectionPointLabelFontSize = 18
glyph1Display_1.SelectionPointLabelItalic = 0
glyph1Display_1.SelectionPointLabelJustification = 'Left'
glyph1Display_1.SelectionPointLabelOpacity = 1.0
glyph1Display_1.SelectionPointLabelShadow = 0
glyph1Display_1.PolarAxes = 'PolarAxesRepresentation'
glyph1Display_1.GaussianRadius = 3.0297310605645182
glyph1Display_1.ShaderPreset = 'Sphere'
glyph1Display_1.Emissive = 0
glyph1Display_1.ScaleByArray = 0
glyph1Display_1.SetScaleArray = ['POINTS', 'GlyphScale']
glyph1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display_1.OpacityByArray = 0
glyph1Display_1.OpacityArray = ['POINTS', 'GlyphScale']
glyph1Display_1.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display_1.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Arrow' selected for 'GlyphType'
glyph1Display_1.GlyphType.TipResolution = 6
glyph1Display_1.GlyphType.TipRadius = 0.1
glyph1Display_1.GlyphType.TipLength = 0.35
glyph1Display_1.GlyphType.ShaftResolution = 6
glyph1Display_1.GlyphType.ShaftRadius = 0.03
glyph1Display_1.GlyphType.Invert = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display_1.DataAxesGrid.XTitle = 'X Axis'
glyph1Display_1.DataAxesGrid.YTitle = 'Y Axis'
glyph1Display_1.DataAxesGrid.ZTitle = 'Z Axis'
glyph1Display_1.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.XTitleFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.XTitleBold = 0
glyph1Display_1.DataAxesGrid.XTitleItalic = 0
glyph1Display_1.DataAxesGrid.XTitleFontSize = 12
glyph1Display_1.DataAxesGrid.XTitleShadow = 0
glyph1Display_1.DataAxesGrid.XTitleOpacity = 1.0
glyph1Display_1.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.YTitleFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.YTitleBold = 0
glyph1Display_1.DataAxesGrid.YTitleItalic = 0
glyph1Display_1.DataAxesGrid.YTitleFontSize = 12
glyph1Display_1.DataAxesGrid.YTitleShadow = 0
glyph1Display_1.DataAxesGrid.YTitleOpacity = 1.0
glyph1Display_1.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.ZTitleFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.ZTitleBold = 0
glyph1Display_1.DataAxesGrid.ZTitleItalic = 0
glyph1Display_1.DataAxesGrid.ZTitleFontSize = 12
glyph1Display_1.DataAxesGrid.ZTitleShadow = 0
glyph1Display_1.DataAxesGrid.ZTitleOpacity = 1.0
glyph1Display_1.DataAxesGrid.FacesToRender = 63
glyph1Display_1.DataAxesGrid.CullBackface = 0
glyph1Display_1.DataAxesGrid.CullFrontface = 1
glyph1Display_1.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.ShowGrid = 0
glyph1Display_1.DataAxesGrid.ShowEdges = 1
glyph1Display_1.DataAxesGrid.ShowTicks = 1
glyph1Display_1.DataAxesGrid.LabelUniqueEdgesOnly = 1
glyph1Display_1.DataAxesGrid.AxesToLabel = 63
glyph1Display_1.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.XLabelFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.XLabelBold = 0
glyph1Display_1.DataAxesGrid.XLabelItalic = 0
glyph1Display_1.DataAxesGrid.XLabelFontSize = 12
glyph1Display_1.DataAxesGrid.XLabelShadow = 0
glyph1Display_1.DataAxesGrid.XLabelOpacity = 1.0
glyph1Display_1.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.YLabelFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.YLabelBold = 0
glyph1Display_1.DataAxesGrid.YLabelItalic = 0
glyph1Display_1.DataAxesGrid.YLabelFontSize = 12
glyph1Display_1.DataAxesGrid.YLabelShadow = 0
glyph1Display_1.DataAxesGrid.YLabelOpacity = 1.0
glyph1Display_1.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
glyph1Display_1.DataAxesGrid.ZLabelFontFamily = 'Arial'
glyph1Display_1.DataAxesGrid.ZLabelBold = 0
glyph1Display_1.DataAxesGrid.ZLabelItalic = 0
glyph1Display_1.DataAxesGrid.ZLabelFontSize = 12
glyph1Display_1.DataAxesGrid.ZLabelShadow = 0
glyph1Display_1.DataAxesGrid.ZLabelOpacity = 1.0
glyph1Display_1.DataAxesGrid.XAxisNotation = 'Mixed'
glyph1Display_1.DataAxesGrid.XAxisPrecision = 2
glyph1Display_1.DataAxesGrid.XAxisUseCustomLabels = 0
glyph1Display_1.DataAxesGrid.XAxisLabels = []
glyph1Display_1.DataAxesGrid.YAxisNotation = 'Mixed'
glyph1Display_1.DataAxesGrid.YAxisPrecision = 2
glyph1Display_1.DataAxesGrid.YAxisUseCustomLabels = 0
glyph1Display_1.DataAxesGrid.YAxisLabels = []
glyph1Display_1.DataAxesGrid.ZAxisNotation = 'Mixed'
glyph1Display_1.DataAxesGrid.ZAxisPrecision = 2
glyph1Display_1.DataAxesGrid.ZAxisUseCustomLabels = 0
glyph1Display_1.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display_1.PolarAxes.Visibility = 0
glyph1Display_1.PolarAxes.Translation = [0.0, 0.0, 0.0]
glyph1Display_1.PolarAxes.Scale = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.Orientation = [0.0, 0.0, 0.0]
glyph1Display_1.PolarAxes.EnableCustomBounds = [0, 0, 0]
glyph1Display_1.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
glyph1Display_1.PolarAxes.EnableCustomRange = 0
glyph1Display_1.PolarAxes.CustomRange = [0.0, 1.0]
glyph1Display_1.PolarAxes.PolarAxisVisibility = 1
glyph1Display_1.PolarAxes.RadialAxesVisibility = 1
glyph1Display_1.PolarAxes.DrawRadialGridlines = 1
glyph1Display_1.PolarAxes.PolarArcsVisibility = 1
glyph1Display_1.PolarAxes.DrawPolarArcsGridlines = 1
glyph1Display_1.PolarAxes.NumberOfRadialAxes = 0
glyph1Display_1.PolarAxes.AutoSubdividePolarAxis = 1
glyph1Display_1.PolarAxes.NumberOfPolarAxis = 0
glyph1Display_1.PolarAxes.MinimumRadius = 0.0
glyph1Display_1.PolarAxes.MinimumAngle = 0.0
glyph1Display_1.PolarAxes.MaximumAngle = 90.0
glyph1Display_1.PolarAxes.RadialAxesOriginToPolarAxis = 1
glyph1Display_1.PolarAxes.Ratio = 1.0
glyph1Display_1.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.PolarAxisTitleVisibility = 1
glyph1Display_1.PolarAxes.PolarAxisTitle = 'Radial Distance'
glyph1Display_1.PolarAxes.PolarAxisTitleLocation = 'Bottom'
glyph1Display_1.PolarAxes.PolarLabelVisibility = 1
glyph1Display_1.PolarAxes.PolarLabelFormat = '%-#6.3g'
glyph1Display_1.PolarAxes.PolarLabelExponentLocation = 'Labels'
glyph1Display_1.PolarAxes.RadialLabelVisibility = 1
glyph1Display_1.PolarAxes.RadialLabelFormat = '%-#3.1f'
glyph1Display_1.PolarAxes.RadialLabelLocation = 'Bottom'
glyph1Display_1.PolarAxes.RadialUnitsVisibility = 1
glyph1Display_1.PolarAxes.ScreenSize = 10.0
glyph1Display_1.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.PolarAxisTitleOpacity = 1.0
glyph1Display_1.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
glyph1Display_1.PolarAxes.PolarAxisTitleBold = 0
glyph1Display_1.PolarAxes.PolarAxisTitleItalic = 0
glyph1Display_1.PolarAxes.PolarAxisTitleShadow = 0
glyph1Display_1.PolarAxes.PolarAxisTitleFontSize = 12
glyph1Display_1.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.PolarAxisLabelOpacity = 1.0
glyph1Display_1.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
glyph1Display_1.PolarAxes.PolarAxisLabelBold = 0
glyph1Display_1.PolarAxes.PolarAxisLabelItalic = 0
glyph1Display_1.PolarAxes.PolarAxisLabelShadow = 0
glyph1Display_1.PolarAxes.PolarAxisLabelFontSize = 12
glyph1Display_1.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.LastRadialAxisTextOpacity = 1.0
glyph1Display_1.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
glyph1Display_1.PolarAxes.LastRadialAxisTextBold = 0
glyph1Display_1.PolarAxes.LastRadialAxisTextItalic = 0
glyph1Display_1.PolarAxes.LastRadialAxisTextShadow = 0
glyph1Display_1.PolarAxes.LastRadialAxisTextFontSize = 12
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextBold = 0
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextItalic = 0
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextShadow = 0
glyph1Display_1.PolarAxes.SecondaryRadialAxesTextFontSize = 12
glyph1Display_1.PolarAxes.EnableDistanceLOD = 1
glyph1Display_1.PolarAxes.DistanceLODThreshold = 0.7
glyph1Display_1.PolarAxes.EnableViewAngleLOD = 1
glyph1Display_1.PolarAxes.ViewAngleLODThreshold = 0.7
glyph1Display_1.PolarAxes.SmallestVisiblePolarAngle = 0.5
glyph1Display_1.PolarAxes.PolarTicksVisibility = 1
glyph1Display_1.PolarAxes.ArcTicksOriginToPolarAxis = 1
glyph1Display_1.PolarAxes.TickLocation = 'Both'
glyph1Display_1.PolarAxes.AxisTickVisibility = 1
glyph1Display_1.PolarAxes.AxisMinorTickVisibility = 0
glyph1Display_1.PolarAxes.ArcTickVisibility = 1
glyph1Display_1.PolarAxes.ArcMinorTickVisibility = 0
glyph1Display_1.PolarAxes.DeltaAngleMajor = 10.0
glyph1Display_1.PolarAxes.DeltaAngleMinor = 5.0
glyph1Display_1.PolarAxes.PolarAxisMajorTickSize = 0.0
glyph1Display_1.PolarAxes.PolarAxisTickRatioSize = 0.3
glyph1Display_1.PolarAxes.PolarAxisMajorTickThickness = 1.0
glyph1Display_1.PolarAxes.PolarAxisTickRatioThickness = 0.5
glyph1Display_1.PolarAxes.LastRadialAxisMajorTickSize = 0.0
glyph1Display_1.PolarAxes.LastRadialAxisTickRatioSize = 0.3
glyph1Display_1.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
glyph1Display_1.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
glyph1Display_1.PolarAxes.ArcMajorTickSize = 0.0
glyph1Display_1.PolarAxes.ArcTickRatioSize = 0.3
glyph1Display_1.PolarAxes.ArcMajorTickThickness = 1.0
glyph1Display_1.PolarAxes.ArcTickRatioThickness = 0.5
glyph1Display_1.PolarAxes.Use2DMode = 0
glyph1Display_1.PolarAxes.UseLogAxis = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display_1.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
glyphScaleLUT.RescaleTransferFunction(0.2, 0.7)

# get opacity transfer function/opacity map for 'GlyphScale'
glyphScalePWF = GetOpacityTransferFunction('GlyphScale')
glyphScalePWF.Points = [0.5329999923706055, 0.0, 0.5, 0.0, 0.5331220626831055, 1.0, 0.5, 0.0]
glyphScalePWF.AllowDuplicateScalars = 1
glyphScalePWF.ScalarRangeInitialized = 1

# Rescale transfer function
glyphScalePWF.RescaleTransferFunction(0.2, 0.7)

# resize frame
layout1.SetSplitFraction(0, 0.506596306069)

# resize frame
layout1.SetSplitFraction(0, 0.529023746702)

# resize frame
layout1.SetSplitFraction(0, 0.534960422164)

# resize frame
layout1.SetSplitFraction(0, 0.54617414248)

# set scalar coloring
ColorBy(glyph1Display_1, ('POINTS', 'S'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(glyphScaleLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display_1.SetScalarBarVisibility(renderView1, True)

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

# reset view to fit data
renderView1.ResetCamera()

# resize frame
layout1.SetSplitFraction(0, 0.560026385224)

# resize frame
layout1.SetSplitFraction(0, 0.568601583113)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(a0csv)

# Properties modified on renderView1
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]

# Properties modified on renderView1
renderView1.OrientationAxesLabelColor = [0.3333333333333333, 0.0, 1.0]

# Properties modified on renderView1
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]

# Properties modified on renderView1
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]

# set active source
SetActiveSource(glyph1)

# set scalar coloring
ColorBy(glyph1Display_1, ('POINTS', 'S'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(glyphScaleLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display_1.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'S'
sLUT_1 = GetColorTransferFunction('S')
sLUT_1.LockDataRange = 0
sLUT_1.InterpretValuesAsCategories = 0
sLUT_1.ShowCategoricalColorsinDataRangeOnly = 0
sLUT_1.RescaleOnVisibilityChange = 0
sLUT_1.EnableOpacityMapping = 0
sLUT_1.RGBPoints = [0.533, 0.231373, 0.298039, 0.752941, 0.5330610313415527, 0.865003, 0.865003, 0.865003, 0.5331220626831055, 0.705882, 0.0156863, 0.14902]
sLUT_1.UseLogScale = 0
sLUT_1.ColorSpace = 'Diverging'
sLUT_1.UseBelowRangeColor = 0
sLUT_1.BelowRangeColor = [0.0, 0.0, 0.0]
sLUT_1.UseAboveRangeColor = 0
sLUT_1.AboveRangeColor = [1.0, 1.0, 1.0]
sLUT_1.NanColor = [1.0, 1.0, 0.0]
sLUT_1.Discretize = 1
sLUT_1.NumberOfTableValues = 256
sLUT_1.ScalarRangeInitialized = 1.0
sLUT_1.HSVWrap = 0
sLUT_1.VectorComponent = 0
sLUT_1.VectorMode = 'Magnitude'
sLUT_1.AllowDuplicateScalars = 1
sLUT_1.Annotations = []
sLUT_1.ActiveAnnotatedValues = []
sLUT_1.IndexedColors = []

# Rescale transfer function
sLUT_1.RescaleTransferFunction(0.2, 0.6)

# get opacity transfer function/opacity map for 'S'
sPWF = GetOpacityTransferFunction('S')
sPWF.Points = [0.533, 0.0, 0.5, 0.0, 0.5331220626831055, 1.0, 0.5, 0.0]
sPWF.AllowDuplicateScalars = 1
sPWF.ScalarRangeInitialized = 1

# Rescale transfer function
sPWF.RescaleTransferFunction(0.2, 0.6)


# resize frame
layout1.SetSplitFraction(0, 0.50)

# current camera placement for renderView1
renderView1.CameraPosition = [dropletSize/(dimensionReduction*2), dropletSize/(dimensionReduction*2),dropletSize]
renderView1.CameraFocalPoint = [dropletSize/(dimensionReduction*2),dropletSize/(dimensionReduction*2),dropletSize/2]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CameraParallelScale = dropletSize/(dimensionReduction*1.97)
renderView1.CameraParallelProjection = 1


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
sLUTColorBar.TitleFontSize = 12
sLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
sLUTColorBar.LabelOpacity = 1.0
sLUTColorBar.LabelFontFamily = 'Arial'
sLUTColorBar.LabelBold = 0
sLUTColorBar.LabelItalic = 0
sLUTColorBar.LabelShadow = 0
sLUTColorBar.LabelFontSize = 12
sLUTColorBar.AutomaticLabelFormat = 1
sLUTColorBar.LabelFormat = '%-#6.3g'
sLUTColorBar.DrawTickMarks = 1
sLUTColorBar.DrawTickLabels = 1
sLUTColorBar.UseCustomLabels = 0
sLUTColorBar.CustomLabels = []
sLUTColorBar.AddRangeLabels = 1
sLUTColorBar.RangeLabelFormat = '%-#6.1e'
sLUTColorBar.DrawAnnotations = 1
sLUTColorBar.AddRangeAnnotations = 0
sLUTColorBar.AutomaticAnnotations = 0
sLUTColorBar.DrawNanAnnotation = 0
sLUTColorBar.NanAnnotation = 'NaN'
sLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
sLUTColorBar.ScalarBarThickness = 16
sLUTColorBar.ScalarBarLength = 0.33


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

