class FourierSeriesData {
  float[] real;
  float[] imag;
  int size = 0;
  int span = 0;
  
  int[] order;
  
  void setSize(int s) {
    real = new float[s];
    imag = new float[s];
    size = s;
    span = (s-1) / 2;
    order = new int[s];
    //defaultOrder();
    calcOrder();
    //printOrder();
  }
  
  void defaultOrder() {
    for (int i = 0; i < order.length; i++) {
      order[i] = i;
    }
  }
  
  void printOrder() {
    for (int i = 0; i < order.length; i++) {
      println("i: " + i + "\t" + order[i]);
    }
  }
  
  void calcOrder() {
    int n = 0;
    for (int i = 0; i < order.length; i++) {
      int j = n + span;
      
      order[i] = j;
      
      n = (n > 0) ? (n * -1) : (n * -1 + 1);
    }
  }
}
