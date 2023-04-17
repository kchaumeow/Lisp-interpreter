(begin
	(define factorial
		(lambda
			(x)
			(if
				(> x 1)
				(* x
					(factorial
						(- x 1)
					)
				) x)
		)
	)
	(print Enter number to get a "factorial" of)
	(define x (float (prompt)))
	(factorial x)
)