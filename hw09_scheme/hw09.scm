
; Tail recursion

(define (replicate x n)
  (replicate-acc x n '())
)
(define (replicate-acc x n acc)
  (if (= n 0)
    acc
    (replicate-acc x (- n 1) (cons x acc))
  )
)

(define (accumulate combiner start n term)
  (accumulate-helper combiner start n term 1)
)
(define (accumulate-helper combiner start n term cur)
  (if (> cur n)
    start
    (accumulate-helper combiner (combiner start (term cur)) n term (+ cur 1))
  )
)

(define (accumulate-tail combiner start n term)
  (accumulate-helper combiner start n term 1)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
  (cond
    ((null? s) nil)
    ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
    ((> (car s) (car (cdr-stream s))) (cons-stream (list (car s)) (nondecreastream (cdr-stream s))))
    (else (cons-stream (cons (car s) (car (nondecreastream (cdr-stream s)))) (cdr-stream (nondecreastream (cdr-stream s)))))
  )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))