# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self, m, x, y):
        self.mass = m
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(0, 100)
        ellipse(self.position.x, self.position.y, self.mass*24, self.mass*24)

    def attract(self, m, g=0.4):
        force = PVector.sub(self.position, m.position)
        distance = force.mag()
        distance = constrain(distance, 5.0, 25.0)
        force.normalize();

        strength = (g * self.mass * m.mass)/float(distance * distance)
        force.mult(strength)
        return force