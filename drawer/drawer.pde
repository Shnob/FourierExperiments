String workingShape = "jake";
PGraphics image;
float SCL = 15;
int downScale = 1;
int DPF = 1; // Dots Per Frame
int fadeInterval = 10;

boolean followTip = false;
float zoom = 1;

PVector prev;

FourierSeriesData shape;

void setup() {
  //if (followTip)
    //SCL *= zoom;
  
  size(980, 980);
  //smooth(2);

  frameRate(30);

  image = createGraphics(width * downScale, height * downScale);

  image.beginDraw();
  image.background(0);
  image.endDraw();

  shape = new FourierSeriesData();
  setupShape(shape, workingShape);

  println("Shape: " + workingShape);
  println("Span: " + shape.span);

  //prev = pointAt(shape, 0);
}

int frame = 0;
float t = 0;
float dt = 0.001 / DPF;

void draw() {
  image.beginDraw();
  image.stroke(255, 255, 255);
  image.strokeWeight(1.5 * downScale);
  PVector p = new PVector();
  for (int i = 0; i < DPF; i++) {
    p = pointAt(shape, t);
    p.add( new PVector(image.width/2, image.height/2) );
    if (prev != null)
      image.line(p.x, p.y, prev.x, prev.y);
    prev = p;
    t += dt;
  }
  image.endDraw();
  
  pushMatrix();
  if (followTip) {
    scale(zoom);
    
    translate(-p.x, -p.y);
    
    translate(width/2/zoom, height/2/zoom);
  }
  background(0);
  
  image(image, 0, 0, width, height);
  //fade(image);
  drawSeries(shape, t);
  frame++;
  popMatrix();
}

void drawSeries(FourierSeriesData shape, float t) {
  ellipseMode(CENTER);
  noFill();
  pushMatrix();
  translate(width/2, height/2);

  for (int i = 0; i < shape.size; i++) {
    int j = shape.order[i];
    int n = j - shape.span;

    float x = 2.0 * n * PI * t;
    float re = shape.real[j];
    float im = shape.imag[j];

    PVector end = new PVector( re * cos(x) - im * sin(x), re * sin(x) + im * cos(x) );
    float mag = end.mag();
    end.mult(SCL);

      stroke(100, 100, 255, 100);
    ellipse(0, 0, SCL * mag * 2, SCL * mag * 2);
    
    stroke(100, 255, 100);
    line(0, 0, end.x, end.y);

    translate(end.x, end.y);
  }
  popMatrix();
}

PVector pointAt(FourierSeriesData shape, float t) {
  PVector pos = new PVector(0, 0);

  for (int i = 0; i < shape.size; i++) {
    int n = i - shape.span;

    float x = 2.0 * n * PI * t;
    float re = shape.real[i];
    float im = shape.imag[i];

    PVector tmp = new PVector( re * cos(x) - im * sin(x), re * sin(x) + im * cos(x) );

    pos.add(tmp);
  }

  pos.mult(SCL * downScale);

  return pos;
}

void fade(PGraphics image) {
  if (frame % fadeInterval == 0) {
    image.beginDraw();
    image.blendMode(SUBTRACT);
    image.noStroke();
    image.fill(255, 4);
    image.rect(0, 0, image.width, image.height);
    image.blendMode(BLEND);
    image.endDraw();
  }
}

void setupShape(FourierSeriesData shape, String ws) {
  String[] lines = loadStrings("../fourierSeries/" + ws + ".fsd");
  shape.setSize(lines.length / 2);

  for (int i = 0; i < lines.length/2; i++) {
    shape.real[i] = Float.valueOf(lines[2 * i + 0]);
    shape.imag[i] = Float.valueOf(lines[2 * i + 1]);

    //println("i" + i + ": " + shape.real[i] + ", " + shape.imag[i]);
  }
}
