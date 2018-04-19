'''This is the Python API for the game engine of Rasterizer'''

HDR_FULL_FLOAT = int
HDR_HALF_FLOAT = int
HDR_NONE = int
KX_BLENDER_GLSL_MATERIAL = int
KX_BLENDER_MULTITEX_MATERIAL = int
LEFT_EYE = int
RAS_MIPMAP_LINEAR = int
RAS_MIPMAP_NEAREST = int
RAS_MIPMAP_NONE = int
RIGHT_EYE = int
VSYNC_ADAPTIVE = int
VSYNC_OFF = int
VSYNC_ON = int
def autoDebugList(*argv):
	'''enable or disable auto adding debug properties to the debug  list'''

def clearDebugList(*argv):
	'''clears the debug property list'''

def disableMotionBlur(*argv):
	'''disable motion blur'''

def drawLine(*argv):
	'''draw a line on the screen'''

def enableMotionBlur(*argv):
	'''enable motion blur'''

def enableVisibility(*argv):
	'''enableVisibility doc'''

error = str
def getAnisotropicFiltering(*argv):
	'''get the anisotropic filtering level'''

def getDisplayDimensions(*argv):
	'''Get the actual dimensions, in pixels, of the physical display (e.g., the monitor).'''

def getEyeSeparation(*argv):
	'''get the eye separation for stereo mode'''

def getFocalLength(*argv):
	'''get the focal length for stereo mode'''

def getFullScreen(*argv):
	pass

def getGLSLMaterialSetting(*argv):
	'''get the state of a GLSL material setting'''

def getMaterialMode(*argv):
	'''get the material mode being used for OpenGL rendering'''

def getMipmapping(*argv):
	pass

def getStereoEye(*argv):
	'''get the current stereoscopy eye being rendered'''

def getVsync(*argv):
	pass

def getWindowHeight(*argv):
	'''getWindowHeight doc'''

def getWindowWidth(*argv):
	'''getWindowWidth doc'''

def makeScreenshot(*argv):
	'''make Screenshot doc'''

def setAnisotropicFiltering(*argv):
	'''set the anisotropic filtering level (must be one of 1, 2, 4, 8, 16)'''

def setBackgroundColor(*argv):
	'''set Background Color (rgb)'''

def setEyeSeparation(*argv):
	'''set the eye separation for stereo mode'''

def setFocalLength(*argv):
	'''set the focal length for stereo mode'''

def setFullScreen(*argv):
	pass

def setGLSLMaterialSetting(*argv):
	'''set the state of a GLSL material setting'''

def setMaterialMode(*argv):
	'''set the material mode to use for OpenGL rendering'''

def setMipmapping(*argv):
	pass

def setMousePosition(*argv):
	'''setMousePosition(int x,int y)'''

def setVsync(*argv):
	pass

def setWindowSize(*argv):
	pass

def showFramerate(*argv):
	'''show or hide the framerate'''

def showMouse(*argv):
	'''showMouse(bool visible)'''

def showProfile(*argv):
	'''show or hide the profile'''

def showProperties(*argv):
	'''show or hide the debug properties'''


