# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

# Load the OpenFOAM case
cT3foam = OpenFOAMReader(FileName='../droplet.foam')

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
cT3foam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cT3foamDisplay = Show(cT3foam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
cT3foamDisplay.Representation = 'Surface'
cT3foamDisplay.ColorArrayName = ['POINTS', 'p']
cT3foamDisplay.LookupTable = pLUT
cT3foamDisplay.SelectTCoordArray = 'None'
cT3foamDisplay.SelectNormalArray = 'None'
cT3foamDisplay.SelectTangentArray = 'None'
cT3foamDisplay.OSPRayScaleArray = 'p'
cT3foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cT3foamDisplay.SelectOrientationVectors = 'U'
cT3foamDisplay.ScaleFactor = 0.0004000000189989805
cT3foamDisplay.SelectScaleArray = 'p'
cT3foamDisplay.GlyphType = 'Arrow'
cT3foamDisplay.GlyphTableIndexArray = 'p'
cT3foamDisplay.GaussianRadius = 2.0000000949949027e-05
cT3foamDisplay.SetScaleArray = ['POINTS', 'p']
cT3foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cT3foamDisplay.OpacityArray = ['POINTS', 'p']
cT3foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cT3foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
cT3foamDisplay.PolarAxes = 'PolarAxesRepresentation'
cT3foamDisplay.ScalarOpacityFunction = pPWF
cT3foamDisplay.ScalarOpacityUnitDistance = 0.00015047277529609373
cT3foamDisplay.OpacityArrayName = ['POINTS', 'p']
cT3foamDisplay.SelectInputVectors = ['POINTS', 'U']
cT3foamDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cT3foamDisplay.ScaleTransferFunction.Points = [-2959.72998046875, 0.0, 0.5, 0.0, 932.2680053710938, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cT3foamDisplay.OpacityTransferFunction.Points = [-2959.72998046875, 0.0, 0.5, 0.0, 932.2680053710938, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
cT3foamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# set scalar coloring
ColorBy(cT3foamDisplay, ('POINTS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
cT3foamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cT3foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'alphawater'
alphawaterLUT = GetColorTransferFunction('alphawater')

# get opacity transfer function/opacity map for 'alphawater'
alphawaterPWF = GetOpacityTransferFunction('alphawater')

# get 2D transfer function for 'alphawater'
alphawaterTF2D = GetTransferFunction2D('alphawater')

renderView1.ResetActiveCameraToPositiveY()

# reset view to fit data
renderView1.ResetCamera(False)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=cT3foam)
threshold1.Scalars = ['POINTS', 'p']
threshold1.LowerThreshold = -2959.72998046875
threshold1.UpperThreshold = 932.2680053710938

# Properties modified on threshold1
threshold1.LowerThreshold = 0.5
threshold1.UpperThreshold = 1.5

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = -2.0000000000000002e+298
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = -1e+297
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.OpacityArrayName = ['FIELD', 'CasePath']
threshold1Display.SelectInputVectors = [None, '']
threshold1Display.WriteLog = ''

# hide data in view
Hide(cT3foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on threshold1
threshold1.Scalars = ['POINTS', 'alpha.water']

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=threshold1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0004996954812668264, 0.0, 0.0009187500108964741]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.0004996954812668264, 0.0, 0.0009187500108964741]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 1e-20]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 7.245580200105905e-05
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 3.6227901000529526e-06
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-1842.6600341796875, 0.0, 0.5, 0.0, 442.1445007324219, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-1842.6600341796875, 0.0, 0.5, 0.0, 442.1445007324219, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=slice1)
plotOverLine1.Point1 = [0.0, -2.5302100766566582e-05, 9.999999682655225e-21]
plotOverLine1.Point2 = [0.0007245580200105906, 2.5302100766566582e-05, 9.999999682655225e-21]

# Properties modified on plotOverLine1
plotOverLine1.SamplingPattern = 'Sample At Cell Boundaries'
plotOverLine1.Point2 = [0.004, 2.5302100766566582e-05, 9.999999682655225e-21]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display.LookupTable = pLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'p'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'U'
plotOverLine1Display.ScaleFactor = 0.0004000000189989805
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 2.0000000949949027e-05
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [-1842.6600341796875, 0.0, 0.5, 0.0, 442.1445007324219, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [-1842.6600341796875, 0.0, 0.5, 0.0, 442.1445007324219, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['alpha.water', 'p', 'p_rgh', 'U_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['alpha.water', 'alpha.water', 'arc_length', 'arc_length', 'p', 'p', 'p_rgh', 'p_rgh', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['alpha.water', '0', '0', '0', 'arc_length', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'p', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'p_rgh', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'U_Y', '1', '0.5000076295109483', '0', 'U_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Magnitude', '1', '0.5000076295109483', '0']
plotOverLine1Display_1.SeriesOpacity = ['alpha.water', '1.0', 'arc_length', '1.0', 'p', '1.0', 'p_rgh', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display_1.SeriesPlotCorner = ['alpha.water', '0', 'arc_length', '0', 'p', '0', 'p_rgh', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['alpha.water', '1', 'arc_length', '1', 'p', '1', 'p_rgh', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['alpha.water', '2', 'arc_length', '2', 'p', '2', 'p_rgh', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['alpha.water', '0', 'arc_length', '0', 'p', '0', 'p_rgh', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['alpha.water', '4', 'arc_length', '4', 'p', '4', 'p_rgh', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['alpha.water', '1', 'arc_length', '1', 'p', '1', 'p_rgh', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'alpha.water', '0', 'arc_length', '0', 'p', '0', 'p_rgh', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'alpha.water', '1', 'arc_length', '1', 'p', '1', 'p_rgh', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'alpha.water', '2', 'arc_length', '2', 'p', '2', 'p_rgh', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'alpha.water', '0', 'arc_length', '0', 'p', '0', 'p_rgh', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'alpha.water', '4', 'arc_length', '4', 'p', '4', 'p_rgh', '4', 'vtkValidPointMask', '4']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['alpha.water', 'arc_length', 'p', 'p_rgh', 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'U_Magnitude', 'U_X', 'U_Y', 'U_Z', 'vtkValidPointMask']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Points_X']

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
plotOverLine1Display_2 = Show(plotOverLine1, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=6)

# Properties modified on plotOverLine1Display_2
plotOverLine1Display_2.Assembly = ''

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = []

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'alpha.water', 'arc_length', 'p', 'p_rgh', 'Points', 'Points_Magnitude', 'U', 'U_Magnitude', 'vtkValidPointMask', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['alpha.water', 'arc_length', 'p', 'p_rgh', 'Points', 'Points_Magnitude', 'U', 'U_Magnitude', 'vtkValidPointMask', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['arc_length', 'p', 'p_rgh', 'Points', 'Points_Magnitude', 'U', 'U_Magnitude', 'vtkValidPointMask', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['arc_length', 'p', 'p_rgh', 'Points_Magnitude', 'U', 'U_Magnitude', 'vtkValidPointMask', 'Block Number']

# export view
ExportView('output/data/data_000.csv', view=spreadSheetView1)

# Get animation scene and all time steps
animationScene1 = GetAnimationScene()
timeKeeper = GetTimeKeeper()
timesteps = timeKeeper.TimestepValues

print(f"Found {len(timesteps)} timesteps")

# Loop through each timestep
for i, t in enumerate(timesteps):
    print(f"Processing timestep {i} at time {t}")

    # Set the time explicitly
    animationScene1.TimeKeeper.Time = t
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # Ensure the data updates for this time
    #spreadSheetView1.UpdatePipeline()
    SetActiveView(spreadSheetView1)

    # Export CSV for this timestep
    filename = f'output/data/data_{i:03d}.csv'
    ExportView(filename, view=spreadSheetView1)

print("Finished exporting all timesteps.")


#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1353, 773)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0019987800624221563, -0.010938177304004915, 0.0020000000949949026]
renderView1.CameraFocalPoint = [0.0019987800624221563, 0.0, 0.0020000000949949026]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.002831008604984617

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
