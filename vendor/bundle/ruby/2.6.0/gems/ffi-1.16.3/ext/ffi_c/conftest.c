#include "ruby.h"

/*top*/
extern int t(void);
int main(int argc, char **argv)
{
  if (argc > 1000000) {
    int (* volatile tp)(void)=(int (*)(void))&t;
    printf("%d", (*tp)());
  }

  return 0;
}
int t(void) { void ((*volatile p)()); p = (void ((*)()))ffi_raw_call; return !p; }
