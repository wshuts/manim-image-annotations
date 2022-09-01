from manim import *

class ImageWithMovingCamera(MovingCameraScene):
    def construct(self):
        image = ImageMobject("smith-chart-001.png")
        self.add(image)
        camera = self.camera
        frame = camera.frame
        initial_state = frame.save_state()

        for _ in range(0,5):
            self.play(frame.animate.move_to(_*RIGHT+_*UP))
            self.wait()
        self.play(Restore(initial_state))

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = ImageWithMovingCamera()
    scene.render()