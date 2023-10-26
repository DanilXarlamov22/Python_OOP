class Gun:
    def __init__(self):
        self.shot_count = 0

    def shoot(self):
        if self.shot_count % 2 == 0:
            print("pif")
        else:
            print("paf")
        self.shot_count += 1


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()