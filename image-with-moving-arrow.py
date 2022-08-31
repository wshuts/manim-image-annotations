from manim import *

ARROW_TIP_TO_CENTER = 0.75

class ImageWithMovingArrow(Scene):
    def construct(self):
        grid = NumberPlane()

        image_text = ImageMobject("manual-cooking.png")
        image_text.scale_to_fit_height(8)

        pointer = Arrow(color=BLUE).move_to(5*LEFT + 1.4*UP)

        self.add(image_text, pointer, grid)
        self.remove(grid)

        self.play(FadeIn(pointer))
        self.play(pointer.animate.move_to(5*LEFT + 1.2*UP))
        self.play(pointer.animate.move_to(5*LEFT + 0.3*UP))
        self.play(pointer.animate.move_to(5*LEFT + 0.4*DOWN))
        self.play(pointer.animate.move_to(5*LEFT + 1.2*DOWN))
        self.play(FadeOut(pointer))

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = ImageWithMovingArrow()
    scene.render()