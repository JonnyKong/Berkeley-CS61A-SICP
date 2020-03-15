; from: https://www.nyx.net/~gthompso/quine.htm

(define quine
  ((lambda (x) (list x (list (quote quote) x)))
      (quote (lambda (x) (list x (list (quote quote) x))))))