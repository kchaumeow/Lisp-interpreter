(begin
    (define counter 0)
    (while
        (< counter n)
        (begin
            (define counter (+ counter 1))
            (define x (* x 2))
        )
    )
    x
)