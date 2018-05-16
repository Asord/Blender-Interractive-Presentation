from bpy import types, props
from Slides import GestionSlides

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):

    gestSlide = GestionSlides()
    nbSlide = 0



    def updateProp(self, context):
        """S'exécute quand la valeur change"""
        self.nbSlide = self.gestSlide.getNbSlides()
        print(self.Active_Slide)
        print('UpdateProp')
        if self.Active_Slide > self.nbSlide:
            self.Active_Slide = self.Active_Slide - 1
            self.gestSlide.setActiveSlide(self.Active_Slide)

    """def setProp(self, value):
        PropNumberSlide.nbSlide = PropNumberSlide.gestSlide.getNbSlides()
        print("Valeur : ")
        print(value)
        print("Slide : ")
        print(PropNumberSlide.nbSlide)
        if 0 <= value < PropNumberSlide.nbSlide:
            PropNumberSlide.Active_Slide = value
        else :
            return None

        print(PropNumberSlide.nbSlide)"""

    Active_Slide = props.IntProperty(
            name = "Active slide",
            description = "size of the object to add",
            default = 0, max = 10, min=0, update = updateProp
    )









