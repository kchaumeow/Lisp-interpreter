(begin
	(define mandelbrot
		(lambda
			(c)
			(begin
				(define z 0)
				(define n 0)
				(while
					(&&
						(<=
							(abs z) 2)
						(< n 255)
					)
					(begin
						(define z
							(+
								(* z z) c)
						)
						(define n
							(+ n 1)
						)
					)
				)
				(if
					(== n 255)
					(define res #FFFFFF)
					(define res
						(+ #
							(call {0:02x}{1:02x}{2:02x} format n n n)
						)
					)
				) res)
		)
	)
	(draw_mandelbrot mandelbrot)
)