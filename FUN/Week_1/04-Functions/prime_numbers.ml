(* Let's define some usual arithmetical functions:
 * 
 * gcd that takes two non-negative integers n and m, and that returns the
 * greatest common divisor of n and m, following Euclid's algorithm.
 * 
 * multiple_upto : int -> int -> bool that takes two non-negative integers
 * n and r, and that tells whether n admits at least one divisor between
 * 2 and r, inclusive. In other words that there exists a number d >= 2
 * and <= r, such that the remainder of the division of n by d is zero.
 *
 * is_prime a takes a non-negative integer n and checks whether it is a
 * prime number.
 *)



let rec gcd n m =
  if m = 0 
  then 
    n 
  else 
    gcd m (n mod m)
;;

let multiple_of n d =
  if n mod d = 0
  then
    true
  else
    false
;;

let rec multiple_upto n r =
  if r = 1 then
    false
  else
  if multiple_of n r
  then
    true
  else
    multiple_upto n (r - 1)
;;

let is_prime n = 
  if multiple_upto n (n-1)
  then
    false
  else
    true
;;
