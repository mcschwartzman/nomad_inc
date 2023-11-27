let charX = 300;
let charY = 200;

class Character {
  constructor() {
    this.x = 100;
    this.y = 250;
  }

  body() {
    ellipse(this.x, this.y, 50, 50);
  }

  move() {
    if (keyIsDown(LEFT_ARROW)) {
      this.x = this.x - 5;
    }

    if (keyIsDown(RIGHT_ARROW)) {
      this.x = this.x + 5;
    }

    if (keyIsDown(DOWN_ARROW)) {
      this.y = this.y + 5;
    }

    if (keyIsDown(UP_ARROW)) {
      this.y = this.y - 5;
    }
  }
}

function setup() {
  createCanvas(600, 600);
  console.log("canvas created");
  chars = new Character();
}

function draw() {
  console.log("draw function called");
  background(220);
  ellipse(50, 50, 80, 80);
  chars.body();
  chars.move();
}
