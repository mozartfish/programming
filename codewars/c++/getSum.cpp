int get_sum(int a, int b)
{
  int sum = 0;
  if (a == b) {
    return a;
  } else if (a > b) {
    for (int j = b; j <= a; j++) {
      sum += j;
    }
    return sum;
  } else {
    for (int k = a; k <= b; k++) {
      sum += k;
    }
    return sum;
  }
}