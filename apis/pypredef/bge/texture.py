"""Module that allows to play video files on textures in GameBlender."""

getset_descriptor = None

class DeckLink:
	"""DeckLink objects"""

	def close(*argv):
		"""Close dynamic decklink and restore original"""

	extend = getset_descriptor
	"""DeckLink objects"""

	keying = getset_descriptor
	"""DeckLink objects"""

	level = getset_descriptor
	"""DeckLink objects"""

	def refresh(*argv):
		"""Refresh decklink from source"""

	right = getset_descriptor
	"""DeckLink objects"""

	source = getset_descriptor
	"""DeckLink objects"""


class FilterBGR24:
	"""Source filter BGR24 objects"""

	pass

class FilterBlueScreen:
	"""Filter for Blue Screen objects"""

	color = getset_descriptor
	"""Filter for Blue Screen objects"""

	limits = getset_descriptor
	"""Filter for Blue Screen objects"""

	previous = getset_descriptor
	"""Filter for Blue Screen objects"""


class FilterColor:
	"""Filter for color calculations"""

	matrix = getset_descriptor
	"""Filter for color calculations"""

	previous = getset_descriptor
	"""Filter for color calculations"""


class FilterGray:
	"""Filter for gray scale effect"""

	previous = getset_descriptor
	"""Filter for gray scale effect"""


class FilterLevel:
	"""Filter for levels calculations"""

	levels = getset_descriptor
	"""Filter for levels calculations"""

	previous = getset_descriptor
	"""Filter for levels calculations"""


class FilterNormal:
	"""Filter for Blue Screen objects"""

	colorIdx = getset_descriptor
	"""Filter for Blue Screen objects"""

	depth = getset_descriptor
	"""Filter for Blue Screen objects"""

	previous = getset_descriptor
	"""Filter for Blue Screen objects"""


class FilterRGB24:
	"""Source filter RGB24 objects"""

	pass

class FilterRGBA32:
	"""Source filter RGBA32 objects"""

	pass

IMB_BLEND_ADD = int
IMB_BLEND_ADD_ALPHA = int
IMB_BLEND_COLOR = int
IMB_BLEND_COLORBURN = int
IMB_BLEND_COLORDODGE = int
IMB_BLEND_COPY = int
IMB_BLEND_COPY_ALPHA = int
IMB_BLEND_COPY_RGB = int
IMB_BLEND_DARKEN = int
IMB_BLEND_DIFFERENCE = int
IMB_BLEND_ERASE_ALPHA = int
IMB_BLEND_EXCLUSION = int
IMB_BLEND_HARDLIGHT = int
IMB_BLEND_HUE = int
IMB_BLEND_LIGHTEN = int
IMB_BLEND_LINEARBURN = int
IMB_BLEND_LINEARLIGHT = int
IMB_BLEND_LUMINOSITY = int
IMB_BLEND_MIX = int
IMB_BLEND_MUL = int
IMB_BLEND_OVERLAY = int
IMB_BLEND_PINLIGHT = int
IMB_BLEND_SATURATION = int
IMB_BLEND_SCREEN = int
IMB_BLEND_SOFTLIGHT = int
IMB_BLEND_SUB = int
IMB_BLEND_VIVIDLIGHT = int
class ImageBuff:
	"""Image source from image buffer"""

	filter = getset_descriptor
	"""Image source from image buffer"""

	flip = getset_descriptor
	"""Image source from image buffer"""

	image = getset_descriptor
	"""Image source from image buffer"""

	def load(*argv):
		"""Load image from buffer"""

	def plot(*argv):
		"""update image buffer"""

	scale = getset_descriptor
	"""Image source from image buffer"""

	size = getset_descriptor
	"""Image source from image buffer"""

	valid = getset_descriptor
	"""Image source from image buffer"""


class ImageFFmpeg:
	"""FFmpeg image source"""

	filter = getset_descriptor
	"""FFmpeg image source"""

	flip = getset_descriptor
	"""FFmpeg image source"""

	image = getset_descriptor
	"""FFmpeg image source"""

	def refresh(*argv):
		"""Refresh image, i.e. load it"""

	def reload(*argv):
		"""Reload image, i.e. reopen it"""

	scale = getset_descriptor
	"""FFmpeg image source"""

	size = getset_descriptor
	"""FFmpeg image source"""

	status = getset_descriptor
	"""FFmpeg image source"""

	valid = getset_descriptor
	"""FFmpeg image source"""


class ImageMirror:
	"""Image source from mirror"""

	alpha = getset_descriptor
	"""Image source from mirror"""

	background = getset_descriptor
	"""Image source from mirror"""

	capsize = getset_descriptor
	"""Image source from mirror"""

	clip = getset_descriptor
	"""Image source from mirror"""

	depth = getset_descriptor
	"""Image source from mirror"""

	filter = getset_descriptor
	"""Image source from mirror"""

	flip = getset_descriptor
	"""Image source from mirror"""

	horizon = getset_descriptor
	"""Image source from mirror"""

	image = getset_descriptor
	"""Image source from mirror"""

	def refresh(*argv):
		"""Refresh image - invalidate its current content after optionally transferring its content to a target buffer"""

	def render(*argv):
		"""Render scene - run before refresh() to performs asynchronous render"""

	scale = getset_descriptor
	"""Image source from mirror"""

	size = getset_descriptor
	"""Image source from mirror"""

	updateShadow = getset_descriptor
	"""Image source from mirror"""

	valid = getset_descriptor
	"""Image source from mirror"""

	whole = getset_descriptor
	"""Image source from mirror"""

	zbuff = getset_descriptor
	"""Image source from mirror"""

	zenith = getset_descriptor
	"""Image source from mirror"""


class ImageMix:
	"""Image mixer"""

	filter = getset_descriptor
	"""Image mixer"""

	flip = getset_descriptor
	"""Image mixer"""

	def getSource(*argv):
		"""get image source"""

	def getWeight(*argv):
		"""get image source weight"""

	image = getset_descriptor
	"""Image mixer"""

	def refresh(*argv):
		"""Refresh image - invalidate its current content"""

	scale = getset_descriptor
	"""Image mixer"""

	def setSource(*argv):
		"""set image source"""

	def setWeight(*argv):
		"""set image source weight"""

	size = getset_descriptor
	"""Image mixer"""

	valid = getset_descriptor
	"""Image mixer"""


class ImageRender:
	"""Image source from render"""

	alpha = getset_descriptor
	"""Image source from render"""

	background = getset_descriptor
	"""Image source from render"""

	capsize = getset_descriptor
	"""Image source from render"""

	colorBindCode = getset_descriptor
	"""Image source from render"""

	depth = getset_descriptor
	"""Image source from render"""

	filter = getset_descriptor
	"""Image source from render"""

	flip = getset_descriptor
	"""Image source from render"""

	horizon = getset_descriptor
	"""Image source from render"""

	image = getset_descriptor
	"""Image source from render"""

	def refresh(*argv):
		"""Refresh image - invalidate its current content after optionally transferring its content to a target buffer"""

	def render(*argv):
		"""Render scene - run before refresh() to performs asynchronous render"""

	scale = getset_descriptor
	"""Image source from render"""

	size = getset_descriptor
	"""Image source from render"""

	updateShadow = getset_descriptor
	"""Image source from render"""

	valid = getset_descriptor
	"""Image source from render"""

	whole = getset_descriptor
	"""Image source from render"""

	zbuff = getset_descriptor
	"""Image source from render"""

	zenith = getset_descriptor
	"""Image source from render"""


class ImageViewport:
	"""Image source from viewport"""

	alpha = getset_descriptor
	"""Image source from viewport"""

	capsize = getset_descriptor
	"""Image source from viewport"""

	depth = getset_descriptor
	"""Image source from viewport"""

	filter = getset_descriptor
	"""Image source from viewport"""

	flip = getset_descriptor
	"""Image source from viewport"""

	image = getset_descriptor
	"""Image source from viewport"""

	position = getset_descriptor
	"""Image source from viewport"""

	def refresh(*argv):
		"""Refresh image - invalidate its current content"""

	scale = getset_descriptor
	"""Image source from viewport"""

	size = getset_descriptor
	"""Image source from viewport"""

	valid = getset_descriptor
	"""Image source from viewport"""

	whole = getset_descriptor
	"""Image source from viewport"""

	zbuff = getset_descriptor
	"""Image source from viewport"""


SOURCE_EMPTY = int
SOURCE_ERROR = int
SOURCE_PLAYING = int
SOURCE_READY = int
SOURCE_STOPPED = int
class Texture:
	bindId = getset_descriptor
	def close(*argv):
		"""Close dynamic texture and restore original"""

	invalid = getset_descriptor
	mipmap = getset_descriptor
	def refresh(*argv):
		"""Refresh texture from source"""

	source = getset_descriptor

class VideoDeckLink:
	"""DeckLink video source"""

	filter = getset_descriptor
	"""DeckLink video source"""

	flip = getset_descriptor
	"""DeckLink video source"""

	framerate = getset_descriptor
	"""DeckLink video source"""

	image = getset_descriptor
	"""DeckLink video source"""

	def pause(*argv):
		"""pause video"""

	def play(*argv):
		"""Play (restart) video"""

	def refresh(*argv):
		"""Refresh video - get its status"""

	scale = getset_descriptor
	"""DeckLink video source"""

	size = getset_descriptor
	"""DeckLink video source"""

	status = getset_descriptor
	"""DeckLink video source"""

	def stop(*argv):
		"""stop video (play will replay it from start)"""

	valid = getset_descriptor
	"""DeckLink video source"""


class VideoFFmpeg:
	"""FFmpeg video source"""

	deinterlace = getset_descriptor
	"""FFmpeg video source"""

	filter = getset_descriptor
	"""FFmpeg video source"""

	flip = getset_descriptor
	"""FFmpeg video source"""

	framerate = getset_descriptor
	"""FFmpeg video source"""

	image = getset_descriptor
	"""FFmpeg video source"""

	def pause(*argv):
		"""pause video"""

	def play(*argv):
		"""Play (restart) video"""

	preseek = getset_descriptor
	"""FFmpeg video source"""

	range = getset_descriptor
	"""FFmpeg video source"""

	def refresh(*argv):
		"""Refresh video - get its status"""

	repeat = getset_descriptor
	"""FFmpeg video source"""

	scale = getset_descriptor
	"""FFmpeg video source"""

	size = getset_descriptor
	"""FFmpeg video source"""

	status = getset_descriptor
	"""FFmpeg video source"""

	def stop(*argv):
		"""stop video (play will replay it from start)"""

	valid = getset_descriptor
	"""FFmpeg video source"""


def getLastError(*argv):
	"""Gets last error description"""

def imageToArray(*argv):
	"""get buffer from image source, color channels are selectable"""

def materialID(*argv):
	"""Gets object's Blender Material ID"""

def setLogFile(*argv):
	"""Sets log file name"""


