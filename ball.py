from pico2d import load_image, get_canvas_width

import game_world


class Ball:
    image = None    # 모든 공이 같은 이미지를 공유 (한 번만 로드)

    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.velocity = velocity    # 갱신 1회당 x 이동량 (+ 오른쪽, - 왼쪽)

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 완전히 나가면 게임 월드에서 제거
        if self.x < -25 or self.x > get_canvas_width() + 25:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
