from manim import *
from manim.utils.unit import Percent, Pixels

class ImageWithZoomedScene(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        image = ImageMobject("smith-chart-001.png")
        self.add(image)
        image.shift(30*Pixels*(0.1*LEFT + UP))
        
        zoomed_camera = self.zoomed_camera
        frame = zoomed_camera.frame
        frame.set_color(PURPLE)
        frame.move_to(ORIGIN)

        zoomed_display = self.zoomed_display
        zoomed_display.shift(DOWN)

        zoomed_display_frame = zoomed_display.display_frame
        zoomed_display_frame.set_color(RED)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        self.play(Create(frame))

        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)

        scale_factor = [0.5, 1.5, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor)
        )
        self.wait()

        self.play(ScaleInPlace(zoomed_display, 2))
        self.wait()
        
        # self.play(frame.animate.shift(2.5 * DOWN))
        self.wait()
        # self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        # self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = ImageWithZoomedScene()
    scene.render()