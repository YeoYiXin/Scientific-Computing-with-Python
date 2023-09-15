import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number >= len(self.contents):
      return self.contents
    drawn = random.sample(self.contents, number)
    for ball in drawn:
      self.contents.remove(ball)
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)  #return a list of balls drawn

    meets_criteria = True
    for color, count in expected_balls.items():
      #count the balls according to colour and compared it with the expected balls value
      if balls_drawn.count(color) < count:
        meets_criteria = False
        break

    if meets_criteria:
      success_count += 1

  return success_count / num_experiments
