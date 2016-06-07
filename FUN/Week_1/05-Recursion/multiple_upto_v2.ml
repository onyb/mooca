(*
 * multiple_upto : int -> int -> bool that takes two non-negative integers
 * n and r, and that tells whether n admits at least one divisor between
 * 2 and r, inclusive. In other words that there exists a number d >= 2
 * and <= r, such that the remainder of the division of n by d is zero.
 *)

let multiple_upto n r =
  let rec aux idx =
    if idx > r
    then
      false
    else
    if n mod idx = 0 then
      true
    else
      aux (idx + 1)
  in aux 2
;;

