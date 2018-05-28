from bpy import types, props, context
from Slides import GestionSlides
from Managers.XMLParser import XMLNodes

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):

    gestSlide = GestionSlides()
    nbSlide = 0

    def updateProp(self, context):
        """S'exécute quand la valeur change"""
        self.nbSlide = self.gestSlide.getNbSlides()

        if self.Active_Slide == 0:
            self.Active_Slide = 1
        if self.Active_Slide > self.nbSlide:
            self.Active_Slide = self.Active_Slide - 1
            
        self.gestSlide.setActiveSlide(self.Active_Slide)

    Active_Slide = props.IntProperty(
            name = XMLNodes[2]["SlideSize"],
            description = XMLNodes[3]["SlideSizeDesc"],
            default = 0, max = 10, min=0, update = updateProp
    )
def registerProps():
    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)