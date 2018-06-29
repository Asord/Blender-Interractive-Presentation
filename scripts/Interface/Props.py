from bpy import types, props
from Managers.SlidesManager import SlidesManager

from Managers.XMLParser import XMLData

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):
    gestSlide = SlidesManager()
    nbSlide = 0

    def updateProp(self, context):
        """
        S'exécute quand la valeur change

        :arg context: context where the prop exists
        """
        self.nbSlide = self.gestSlide.getNbSlides()

        if self.Active_Slide == 0:
            self.Active_Slide = 1
        if self.Active_Slide > self.nbSlide:
            self.Active_Slide = self.Active_Slide - 1
            
        self.gestSlide.setActiveSlide(self.Active_Slide)

    Active_Slide = props.IntProperty(
            name = XMLData["prop@SlideSize"],
            description = XMLData["desc@SlideSizeDesc"],
            default = 0, max = 10, min=0, update = updateProp
    )

class PropCustomMotion(Property):

    is_Enable = props.BoolProperty(
    )

def registerProps():
    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)
    types.Scene.prop_custom_motion = props.PointerProperty(type=PropCustomMotion)