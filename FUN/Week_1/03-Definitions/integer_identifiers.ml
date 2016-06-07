(*
 * Suppose that a variable x exists and is an integer.
 * Define a variable x_power_8 that uses three multiplications to calculate x
 * to the power of 8. The only function you are allowed to call is the *
 * operator. 
 *)


(* The given prelude *)
let x = Random.int 9 + 1 ;;

let x_power_8 = let x1 = x * x in 
  let x2 = x1 * x1 in 
  x2 * x2
;;

(* Alternate recursive solution *)
let x_power_8_rec n = 
  let rec aux idx = 
    if idx = 8
    then
      1
    else
      n * aux (idx+1)
  in aux 0
;;

x_power_8 ;;
