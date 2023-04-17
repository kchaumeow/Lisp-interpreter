(begin
	(define factorial
		(lambda
			(x)
			(begin
				(define r x)
				(while
					(> x 1)
					(begin
						(define r
							(* r
								(- x 1)
							)
						)
						(define x
							(- x 1)
						)
					)
				) r)
		)
	)
	(print Enter number to get a "factorial" of)
	(define x (float (prompt)))
	(factorial x)
)