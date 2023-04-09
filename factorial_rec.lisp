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
	(factorial 3)
)