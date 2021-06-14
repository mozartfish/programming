#lang racket
(provide square-sum)

(define (square-sum numbers)
  (for/sum ([x numbers]) (* x x)))