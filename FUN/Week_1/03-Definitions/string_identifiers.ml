(*
 * Suppose that a variable word exists and is a string.
 * Define a variable sentence that uses 5 string concatenations to create a
 * string containing 9 times word, separated by commas.
 *)


let word = "foo";;

let x = word ^ ",";; (* One *)

let sentence = 
  let x1 = x^x^x in  (* Three *)
  let x2 = x1^x1 in  (* Four *)
  x2^x1              (* Five *)
;;
