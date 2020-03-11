(define (partial-sums stream)
  (helper 0 stream)
)

(define (helper n stream)
  (cond
    ((null? stream) '())
    (else (cons-stream (+ n (car stream)) (helper (+ n (car stream)) (cdr-stream stream))))
  )
)