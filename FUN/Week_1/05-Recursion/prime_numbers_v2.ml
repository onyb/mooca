(*
 * is_prime a takes a non-negative integer n and checks whether it is a
 * prime number.
 *)

let is_prime_v2 n =
  let multiple_of n d =
    if n mod d = 0
    then
      true
    else
      false
  in
  let rec multiple_upto n r =
    if r = 1
    then
      false
    else
    if multiple_of n r
    then
      true
    else
      multiple_upto n (r-1)
  in
  if multiple_upto n (n-1)
  then
    false
  else
    true
;;
