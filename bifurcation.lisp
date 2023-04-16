(begin
	(define x3
		(float 0.01)
	)
	(define s
		(list)
	)
	(define c
		(list)
	)
	(define step
		(float 0.0001)
	)
	(define j 0)
	(while
		(< j 200)
		(begin
			(define x0 x3)
			(define i 0)
			(while
				(< i 200)
				(begin
					(define x0
						(- 1
							(*
								(* step x0) x0)
						)
					)
					(call s append x0)
					(call c append step)
					(define i
						(+ i 1)
					)
				)
			)
			(define j
				(+ j 1)
			)
			(define x3 x0)
			(define step
				(+ step
					(float 0.01)
				)
			)
		)
	)
	(draw_bifur c s)
)