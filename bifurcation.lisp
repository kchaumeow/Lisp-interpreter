(begin
    (define x3 0.01)
    (define s (list))
    (define c (list))
    (define step 0.0001)
    (define j 0)
    (while (j < 200) (begin
        (define x0 x3)
        (define i 0)
        (while (i < 200)(begin
            (define x0 (- 1 (*(*step x0) x0)))
            (call s append x0)
            (call c append step)
            )
        (define x3 x0)
        (define step (+ step 0.01))
        )
    (plt.plot c s b. 1)
    (plt.show)
)