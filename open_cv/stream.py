import cv2


class Webcam:
    def __init__(self,
                 camera_index: int = 0,
                 title: str = "ml tracking"):
        self.capture = cv2.VideoCapture(camera_index)
        self.title = title
        self.updated, self.frame = None, None
        self.color_spaces = {
            'rgb': cv2.COLOR_BGR2RGB,
            'bgr': cv2.COLOR_RGB2BGR
        }

    def update(self):
        self.updated, self.frame = self.capture.read()

    def set_color_space(self, space):
        self.frame = cv2.cvtColor(self.frame, self.color_spaces[space])

    def draw(self):
        cv2.imshow(self.title, cv2.flip(self.frame, 1))

    def exit_stream(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return True
        else:
            return False

    def __del__(self):
        self.capture.release()
        cv2.destroyAllWindows()


def main():
    stream = Webcam()
    while stream.capture.isOpened():
        stream.update()
        stream.set_color_space('rgb')
        stream.set_color_space('bgr')
        stream.draw()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    del stream


if __name__ == "__main__":
    main()
