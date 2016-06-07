(*
 * Let's define two functions working with integers:
 *
 * multiple_of that takes two integer parameters, n and d, and determines
 * whether n is a multiple of d. The function must return a boolean value.
 * This function can be written without recursion.
 *
 * integer_square_root that calculates the integer square root of a positive
 * integer n, that is the largest integer r such that r * r <= n
 *)

let multiple_of n d = 
  if n mod d = 0 then true else false;;

let integer_square_root n =
  int_of_float (sqrt (float_of_int n));;

