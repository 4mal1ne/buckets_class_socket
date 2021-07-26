class Bucket:
    def __init__(self):
        self.water_value = 0


class ThreeLBucket(Bucket):
    def draw_water_in_a_bucket(self):
        self.water_value = 3

    def empty_the_bucket(self):
        self.water_value = 0

    def pour_water_out_of_the_bucket(self, five_bucket):
        free_value_of_five_bucket = 5 - five_bucket.water_value
        if self.water_value >= free_value_of_five_bucket:
            five_bucket.water_value += free_value_of_five_bucket
            self.water_value -= free_value_of_five_bucket
        else:
            five_bucket.water_value += self.water_value
            self.water_value -= self.water_value

